"""Strategy."""
from strategy import Strategy
from game_view import Move


class StudentStrategy(Strategy):
    """Student strategy class."""

    def __init__(self, other_players: list, house, decks_count):
        """Init."""
        super().__init__(other_players, house, decks_count)

    def play_move(self, hand) -> Move:
        """Get next move."""
        if hand.can_split:
            split = self.split_hand(hand)
            if split is not None:
                return split
        if not hand.is_soft_hand:
            return self.hard_hand(hand)
        else:  # hand is_soft_hand
            return self.soft_hand(hand)

    def on_card_drawn(self, card) -> None:
        """Called every time card is drawn."""

    def on_game_end(self) -> None:
        """Called on game end."""

    def house_score(self):
        """House open card score."""
        # card = self.house.cards[1] if self.house.cards[0].top_down else self.house.cards[0]
        card = self.house.cards[0]
        if card.value != 'ACE':
            if card.value.isnumeric():
                return int(card.value)
            elif card.value in ('JACK', 'QUEEN', 'KING'):
                return 10
        else:
            return 11

    def split_hand(self, hand):
        """Deal with hand which can split."""
        if 4 <= hand.score <= 6 and 2 <= self.house_score() <= 7:
            return Move.SPLIT
        if hand.score == 8 and 5 <= self.house_score() <= 6:
            return Move.SPLIT
        if hand.score == 12:
            if hand.is_soft_hand:  # Two Aces
                return Move.SPLIT
            elif 2 <= self.house_score() <= 6:  # Two 6-s
                return Move.SPLIT
        if hand.score == 14 and 2 <= self.house_score() <= 7:
            return Move.SPLIT
        if hand.score == 16:
            return Move.SURRENDER if self.house_score() == 11 else Move.SPLIT
        if hand.score == 18 and (2 <= self.house_score() <= 6 or 8 <= self.house_score() <= 9):
            return Move.SPLIT
        return None

    def hard_hand(self, hand):
        """Deal with hard hand."""
        if hand.score <= 8:
            return Move.HIT
        if hand.score == 9:
            return Move.DOUBLE_DOWN if 3 <= self.house_score() <= 6 else Move.HIT
        if hand.score == 10:
            return Move.DOUBLE_DOWN if 2 <= self.house_score() <= 9 else Move.HIT
        if hand.score == 11:
            return Move.DOUBLE_DOWN
        if hand.score == 12:
            return Move.STAND if 4 <= self.house_score() <= 6 else Move.HIT
        if 13 <= hand.score <= 16:
            return Move.STAND if 2 <= self.house_score() <= 6 else Move.HIT
        if 17 <= hand.score:
            return Move.STAND

    def soft_hand(self, hand):
        """Deal with soft hand."""
        if 13 <= hand.score <= 14:
            return Move.DOUBLE_DOWN if 5 <= self.house_score() <= 6 else Move.HIT
        if 15 <= hand.score <= 16:
            return Move.DOUBLE_DOWN if 4 <= self.house_score() <= 6 else Move.HIT
        if hand.score == 17:
            return Move.DOUBLE_DOWN if 3 <= self.house_score() <= 6 else Move.HIT
        if hand.score == 18:
            return Move.DOUBLE_DOWN if 2 <= self.house_score() <= 6 else Move.STAND if 7 <= self.house_score() <= 8 else Move.HIT
        if hand.score == 19:
            return Move.DOUBLE_DOWN if self.house_score() == 6 else Move.STAND
        if 20 <= hand.score:
            return Move.STAND
