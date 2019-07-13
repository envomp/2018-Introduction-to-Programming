"""Strategy."""

from abc import abstractmethod

from game_view import GameView, Move


class Strategy:
    """Strategy."""

    def __init__(self, other_players: list):
        """Init."""
        self.player = None
        self.other_players = other_players

    @abstractmethod
    def play_move(self) -> Move:
        """Play move."""


class HumanStrategy(Strategy):
    """Human strategy."""

    def __init__(self, other_players: list, view: GameView):
        """Init."""
        super().__init__(other_players)
        self.view = view

    def play_move(self) -> Move:
        """Play move."""
        return self.view.ask_move()
