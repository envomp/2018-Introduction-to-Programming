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

    def play_move(self, hand) -> Move:
        """Get next move."""
        if hand.score < 17 or hand.is_soft_hand:
            return Move.HIT
        return Move.STAND

    def on_card_drawn(self) -> None:
        """Called every time card is drawn to player."""

    def on_game_end(self) -> None:
        """Called on game end."""
