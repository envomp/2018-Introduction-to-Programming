"""Strategy."""
from abc import abstractmethod

from game_view import GameView, Move


class Strategy:
    """Strategy."""

    def __init__(self, other_players: list, house, decks_count: int):
        """Init."""
        self.player = None
        self.house = house
        self.decks_count = decks_count
        self.other_players = other_players

    @abstractmethod
    def on_card_drawn(self, card) -> None:
        """Called every time when card is drawn."""

    @abstractmethod
    def play_move(self, hand) -> Move:
        """Play move."""

    @abstractmethod
    def on_game_end(self) -> None:
        """Called on game end."""


class HumanStrategy(Strategy):
    """Human strategy."""

    def __init__(self, other_players: list, house, decks_count, view: GameView):
        """Init."""
        super().__init__(other_players, house, decks_count)
        self.view = view

    def play_move(self, hand) -> Move:
        """Play move."""
        return self.view.ask_move()

    def on_card_drawn(self, card) -> None:
        """Called every time card is drawn."""

    def on_game_end(self) -> None:
        """Called on game end."""


class MirrorDealerStrategy(Strategy):
    """Very simple strategy."""

    def play_move(self, hand) -> Move:
        """Get next move."""
        if hand.score < (18 if hand.is_soft_hand else 17):
            return Move.HIT
        return Move.STAND

    def on_card_drawn(self, card) -> None:
        """Called every time card is drawn."""

    def on_game_end(self) -> None:
        """Called on game end."""


class TestStrategy(Strategy):
    """Test strategy."""

    def house_score(self):
        """House open card score."""
        card = self.house.cards[1] if self.house.cards[0].top_down else self.house.cards[0]
        if card.value != 'ACE':
            if card.value.isnumeric():
                return int(card.value)
            elif card.value in ('JACK', 'QUEEN', 'KING'):
                return 10
        else:
            return 11

    def play_move(self, hand) -> Move:
        """Get next move."""
        if hand.score <= 11 and not hand.is_soft_hand:
            return Move.HIT
        if hand.score == 12 and not hand.is_soft_hand:
            return Move.STAND if 4 <= self.house_score() <= 6 else Move.HIT
        if 13 <= hand.score <= 15 and not hand.is_soft_hand:
            return Move.STAND if 2 <= self.house_score() <= 6 else Move.HIT
        if hand.score == 16 and not hand.is_soft_hand:
            return Move.STAND if 2 <= self.house_score() <= 6 else Move.HIT if 7 <= self.house_score() <= 8 else Move.SURRENDER
        if 17 <= hand.score and not hand.is_soft_hand:
            return Move.STAND
        if hand.score <= 17 and hand.is_soft_hand:
            return Move.HIT
        if hand.score == 18 and hand.is_soft_hand:
            return Move.HIT if self.house_score() >= 9 else Move.STAND
        if 19 <= hand.score and hand.is_soft_hand:
            return Move.STAND
