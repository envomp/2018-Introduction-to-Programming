"""Deck."""
from typing import Optional, List
import requests
import random
import json


class Card:
    """Simple dataclass for holding card information."""

    def __init__(self, value: str, suit: str, code: str):
        """Constructor."""
        self.value = value
        self.suit = suit
        self.code = code
        self.top_down = False

    def __str__(self):
        """Str."""
        return "??" if self.top_down else f"{self.__repr__()}"

    def __repr__(self) -> str:
        """Repr."""
        return self.code

    def __eq__(self, o) -> bool:
        """Eq."""
        return True if isinstance(o, Card) and self.code == o.code else False


class Deck:
    """Deck."""

    DECK_BASE_API = "https://deckofcardsapi.com/api/deck/"

    def __init__(self, deck_count: int = 1, shuffle: bool = False):
        """Constructor."""
        self._backup_deck = self._generate_backup_pile(deck_count, shuffle)
        self.deck_count = deck_count
        self.is_shuffled = shuffle
        self.remaining = len(self._backup_deck)
        self.deck_id = ""

        if shuffle:
            self._request(self.DECK_BASE_API + 'new/shuffle/?deck_count=' + str(deck_count))
        else:
            self._request(self.DECK_BASE_API + 'new/?deck_count=' + str(deck_count))

    def shuffle(self) -> None:
        """Shuffle the deck."""
        if self.deck_id != 'offline':
            self._request(self.DECK_BASE_API + self.deck_id + '/shuffle/')
        self._backup_deck = self._generate_backup_pile(self.deck_count, True)
        self.remaining = len(self._backup_deck)
        self.is_shuffled = True

    def draw_card(self, top_down: bool = False) -> Optional[Card]:
        """Draw card from the deck."""
        if self.remaining:
            if self.deck_id != 'offline':
                loaded_json = self._request(self.DECK_BASE_API + self.deck_id + '/draw/?count=1')
            else:
                loaded_json = None

            if loaded_json is None:
                # Drawing from Backup
                new = self._backup_deck.pop(0)
                self.remaining = len(self._backup_deck)
                new.top_down = top_down
                return new
            else:
                # Drawing from API
                for card in self._backup_deck:
                    if card.code == loaded_json['cards'][0]['code']:
                        self._backup_deck.remove(card)
                        self.remaining = len(self._backup_deck)
                        new = Card(loaded_json['cards'][0]['value'], loaded_json['cards'][0]['suit'],
                                   loaded_json['cards'][0]['code'])
                        new.top_down = top_down
                        return new

                # If API gives wrong Card
                new = self._backup_deck.pop(0)
                self.remaining = len(self._backup_deck)
                new.top_down = top_down
                return new
        else:
            return None

    def _request(self, url: str) -> dict or None:
        """Update deck."""
        self.deck_id = 'offline'
        try:
            response = requests.get(url)
        except requests.HTTPError:
            return None
        except Exception:
            return None
        try:
            loaded_json = response.json()
            if loaded_json['success']:
                self.deck_id = loaded_json['deck_id']
                return loaded_json
            else:
                return None
        except KeyError:
            return None
        except json.JSONDecodeError:
            return None

    @staticmethod
    def _generate_backup_pile(deck_count: int = 1, shuffle: bool = False) -> List[Card]:
        """Generate backup pile."""
        values = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
        suits = ['SPADES', 'DIAMONDS', 'CLUBS', 'HEARTS']
        out = []
        for i in range(deck_count):
            for suit in suits:
                for value in values:
                    code = (value[-1] if value.isnumeric() else value[0]) + suit[0]
                    out.append(Card(value, suit, code))
        if shuffle:
            random.shuffle(out)
        return out


if __name__ == '__main__':
    d = Deck(shuffle=True)
    d._generate_backup_pile()
    print(d.remaining)  # 52
    card1 = d.draw_card()  # Random card
    print(card1)
    print(card1 in d._backup_deck)  # False
    print(d.remaining)  # 51
    d2 = Deck(deck_count=2)
    print(d2._backup_deck)  # 104 ordered cards (deck after deck)
