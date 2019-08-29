"""Strategy."""
from strategy import Strategy
from game_view import Move


class StudentStrategy(Strategy):
    """Student strategy class"""

    CARD_VALUES = {
        '2': 1,
        '3': 1,
        '4': 1,
        '5': 1,
        '6': 1,
        '7': 0,
        '8': 0,
        '9': 0,
        '0': -1,
        'J': -1,
        'Q': -1,
        'K': -1,
        'A': -1,
    }

    def __init__(self, other_players: list, house, decks_count):
        """Init."""
        super().__init__(other_players, house, decks_count)
        self.deck_count = 0
        self.count = 0

    def play_move(self, hand) -> Move:
        """Get next move."""
        score_to_stop = 17 + self._real_count/ 10  # some random number atm
        if hand.score < score_to_stop or hand.is_soft_hand and hand.score < score_to_stop + 1:
            return Move.HIT
        return Move.STAND

    def on_card_drawn(self, card) -> None:
        """Called every time card is drawn."""
        self.count += self.CARD_VALUES[card.value]

    def on_game_end(self) -> None:
        """Called on game end."""

    @property
    def _real_count(self) -> int:
        """Get real count (per deck)."""
        return self.count / self.decks_count
