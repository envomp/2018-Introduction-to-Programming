"""Deck."""
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
        return False


class Deck:
    """Deck."""

    DECK_BASE_API = "https://deckofcardsapi.com/api/deck/"

    def __init__(self, deck_count: int = 1, shuffle: bool = False):
        """Constructor."""
        self._backup_pile = []
        pass

    def shuffle(self) -> None:
        """Shuffle the deck."""
        pass

    def draw_card(self) -> Card:
        """
        Draw card from the deck.

        :return: card instance.
        """
        pass

    def _request(self, url: str):
        """Update deck."""
        pass

    @staticmethod
    def _generate_backup_pile() -> list:
        """Generate backup pile."""
        return []


if __name__ == '__main__':
    d = Deck(shuffle=True)
    print(d.remaining)  # 52
    card1 = d.draw_card()  # Random card
    print(card1 in d._backup_pile)  # False
    print(d._backup_pile)  # 51 shuffled cards
    d2 = Deck(deck_count=2)
    print(d2._backup_pile)  # 104 ordered cards (deck after deck)
