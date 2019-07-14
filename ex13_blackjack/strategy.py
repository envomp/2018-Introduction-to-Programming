"""Strategy."""

from abc import abstractmethod

from game_view import GameView, Move


class Strategy:
    """Strategy."""

    def __init__(self, other_players: list, house):
        """Init."""
        self.player = None
        self.house = house
        self.other_players = other_players

    @abstractmethod
    def play_move(self, hand) -> Move:
        """Play move."""

    @abstractmethod
    def on_game_end(self) -> None:
        """Called on game end."""


class HumanStrategy(Strategy):
    """Human strategy."""

    def __init__(self, other_players: list, house, view: GameView):
        """Init."""
        super().__init__(other_players, house)
        self.view = view

    def play_move(self, hand) -> Move:
        """Play move."""
        return self.view.ask_move()

    def on_game_end(self) -> None:
        """Called on game end."""


class MirrorDealerStrategy(Strategy):
    """Very simple strategy."""

    def play_move(self, hand) -> Move:
        if hand.score < 17 or hand.is_soft_hand:
            return Move.HIT
        return Move.STAND

    def on_game_end(self) -> None:
        """Called on game end."""
