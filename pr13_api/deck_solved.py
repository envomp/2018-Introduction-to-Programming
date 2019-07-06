"""Deck."""
import itertools
import random

import requests


class Card:
    """Simple dataclass for holding card information."""

    def __init__(self, value: str, suit: str, code: str):
        """Constructor."""
        self.value = value
        self.suit = suit
        self.code = code

    def __repr__(self) -> str:
        """Repr."""
        return self.code

    def __eq__(self, o) -> bool:
        """Eq."""
        return isinstance(o, Card) and self.value == o.value and self.suit == o.suit and self.code == o.code


class Deck:
    """Deck."""

    DECK_BASE_API = "https://deckofcardsapi.com/api/deck/"

    def __init__(self, deck_count: int = 1, shuffle: bool = False):
        """Constructor."""
        self.deck_count = deck_count
        self.is_shuffled = shuffle
        self.id = None
        self._backup_pile = list(itertools.chain(*[self._generate_backup_pile() for _ in range(deck_count)]))
        self.remaining = len(self._backup_pile)

        if shuffle:
            random.shuffle(self._backup_pile)

        self._request(self.DECK_BASE_API + f"new/{'shuffle' if shuffle else ''}/?deck_count={deck_count}")

    def shuffle(self) -> None:
        """Shuffle the deck."""
        if self.id:
            self._request(self.DECK_BASE_API + f"{self.id}/shuffle")

        random.shuffle(self._backup_pile)

    def draw_card(self) -> Card:
        """
        Draw card from the deck.

        :return: card instance.
        """
        if id:
            resp = self._request(self.DECK_BASE_API + f"{self.id}/draw/?count=1").json()
            try:
                card = Card(resp["cards"][0]["value"], resp["cards"][0]["suit"], resp["cards"][0]["code"])
            except ValueError:
                card = self._backup_pile.pop()
        else:
            card = self._backup_pile.pop()
        self._backup_pile.remove(card)
        return card

    def _request(self, url: str):
        """Update deck."""
        resp = None
        try:
            resp = requests.get(url).json()
            self.is_shuffled = resp["shuffled"] if "shuffled" in resp else self.is_shuffled
            self.id = resp["deck_id"]
            self.remaining = resp["remaining"]
        except requests.exceptions.RequestException or ValueError:
            self.id = None
        return resp

    @staticmethod
    def _generate_backup_pile() -> list:
        """Generate backup pile."""
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']
        suits = ['SPADES', 'DIAMONDS', 'HEARTS', 'CLUBS']

        return [Card(v, s, (v[-1] if v.isdigit() else v[0]) + s[0]) for v in values for s in suits]


if __name__ == '__main__':
    d = Deck(shuffle=True)
    print(d.remaining)  # 52
    card1 = d.draw_card()  # Random card
    print(card1 in d._backup_pile)  # False
    print(d._backup_pile)  # 51 shuffled cards
    d2 = Deck(deck_count=2)
    print(d2._backup_pile)  # 104 ordered cards (deck after deck)
