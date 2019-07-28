"""Blackjack."""
import importlib
import os
import pkgutil
import random

from deck_solved import Deck, Card
from game_view import GameView, SimpleView, FancyView, Move
from strategy import Strategy, HumanStrategy


class Hand:
    """Hand."""

    def __init__(self, cards: list = None):
        """Init."""
        self.cards = cards if cards else []
        self.is_double_down = False
        self.is_surrendered = False

    def add_card(self, card: Card) -> None:
        """Add card to hand."""
        self.cards.append(card)

    def double_down(self, card: Card) -> None:
        """Double down."""
        self.add_card(card)
        self.is_double_down = True

    def split(self):
        """Split hand."""
        if not self.can_split():
            raise ValueError("Invalid hand to split!")
        return Hand([self.cards.pop()])

    def can_split(self) -> bool:
        """Check if hand can be split."""
        return len(self.cards) == 2 and self.cards[0].value == self.cards[1].value

    @property
    def is_blackjack(self) -> bool:
        """Check if is blackjack"""
        return len(self.cards) == 2 and self.score == 21

    @property
    def is_soft_hand(self):
        """Check if is soft hand."""
        return max(self.cards, key=lambda x: x.value == "ACE").value == 11  # TODO: Check for multiple aces?

    @property
    def score(self):
        """Get score of hand."""
        score = 0
        aces_count = 0
        for card in self.cards:
            if card.value == "JACK" or card.value == "QUEEN" or card.value == "KING":
                score += 10
            elif card.value == "ACE":
                score += 11
                aces_count += 1
            else:
                score += int(card.value)
        for _ in range(aces_count):
            score -= 10 if score > 21 else 0
        return score


class Player:
    """Player."""

    def __init__(self, name: str, strategy: Strategy, coins: int = 100):
        """Init."""
        self.name = name
        self.hands = []
        self.coins = coins
        self.strategy = strategy
        strategy.player = self

    def join_table(self):
        """Join table."""
        self.hands = [Hand()]

    def play_move(self, hand: Hand) -> Move:
        """Play move."""
        return self.strategy.play_move(hand)

    def split_hand(self, hand: Hand):
        """Split hand."""
        if hand in self.hands:
            self.hands.append(hand.split())


class GameController:
    """Game controller."""

    PLAYER_START_COINS = 200
    BUY_IN_COST = 10

    def __init__(self, view: GameView):
        """Init."""
        self.view = view
        self.house = Hand()
        self.players = []
        self.bets = dict()
        self.deck = None

    def start_game(self) -> None:
        """Start game"""
        decks_count = self.view.ask_decks_count()
        players_count = self.view.ask_players_count()
        bots_count = self.view.ask_bots_count()

        strategies = self.load_strategies()

        self.deck = Deck(decks_count, True)
        self.house = Hand()

        for i in range(players_count):
            player = Player(self.view.ask_name(i + 1),
                            HumanStrategy(self.players, self.house, self.view),
                            self.PLAYER_START_COINS)
            self.players.append(player)

        for i in range(bots_count):
            bot = Player(f"Bot #{i + 1}", random.choice(strategies)(self.players, self.house), self.PLAYER_START_COINS)
            self.players.append(bot)

    def play_round(self) -> bool:
        if all([player.coins < self.BUY_IN_COST for player in self.players]):
            return False

        for player in self.players:
            if player.coins >= self.BUY_IN_COST:
                player.coins -= self.BUY_IN_COST
                player.join_table()

                for hand in player.hands:
                    hand.add_card(self.deck.draw_card())
                    hand.add_card(self.deck.draw_card())  # Add 2 cards

        self.house.add_card(self.deck.draw_card())

        for p in self.players:
            p.strategy.house = self.house

        self.house = Hand(self.house.cards)
        self.house.add_card(self.deck.draw_card(top_down=True))

        for player in self.players:

            for hand in player.hands:
                playing = True
                while playing:
                    self.view.show_table(self.players, self.house, hand)
                    move = player.play_move(player.hands[0])

                    if move == Move.HIT:
                        hand.add_card(self.deck.draw_card())
                    elif move == Move.SPLIT:
                        if hand.can_split:
                            player.split_hand(hand)
                            player.coins -= self.BUY_IN_COST
                            for h in player.hands:
                                while len(h.cards) < 2:
                                    h.add_card(self.deck.draw_card())
                        else:
                            print("CANNOT SPLIT NOW")
                    elif move == Move.DOUBLE_DOWN:
                        player.coins -= self.BUY_IN_COST
                        hand.double_down(self.deck.draw_card())
                        playing = False
                    elif move == Move.STAND:
                        playing = False
                    elif move == Move.SURRENDER:
                        playing = False
                        hand.is_surrendered = True
                    else:
                        raise ValueError("Illegal move!")

                    if hand.score > 21:
                        playing = False

        # Basic house logic
        for p in self.players:
            p.strategy.house = self.house

        for c in self.house.cards:
            c.top_down = False
        while self.house.score <= 16 or (self.house.score <= 17 and self.house.is_soft_hand):
            self.house.add_card(self.deck.draw_card())
            self.view.show_table(self.players, self.house, None)

        # Pay players at 1:1 ratio on bets, 3:2 for blackjack
        for player in self.players:
            for hand in player.hands:
                if hand.is_surrendered:
                    player.coins += 0.5 * self.BUY_IN_COST
                elif hand.score == 21 and hand.is_blackjack:
                    player.coins += 3 * self.BUY_IN_COST
                elif self.house.score < hand.score <= 21 or self.house.score > 21:
                    player.coins += self.BUY_IN_COST * 4 if hand.is_double_down else self.BUY_IN_COST * 2
                elif self.house.score == hand.score:
                    player.coins += self.BUY_IN_COST

            player.strategy.on_game_end()
            self.house = Hand()

        return True

    @staticmethod
    def load_strategies() -> list:
        """Load strategies"""
        pkg_dir = os.path.dirname(__file__)
        for (module_loader, name, is_pkg) in pkgutil.iter_modules([pkg_dir]):
            importlib.import_module('.' + name, 'ex13_blackjack')
        return list(filter(lambda x: x.__name__ != HumanStrategy.__name__, Strategy.__subclasses__()))


if __name__ == '__main__':
    game_controller = GameController(FancyView())
    game_controller.start_game()
    while game_controller.play_round():
        pass
