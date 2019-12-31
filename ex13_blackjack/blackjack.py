"""Blackjack."""
import importlib
import os
import pkgutil

# import random
from deck import Deck, Card
from game_view import GameView, FancyView, Move
from strategy import Strategy, HumanStrategy, MirrorDealerStrategy


class Hand:
    """Hand."""

    def __init__(self, cards: list = None):
        """Init."""
        self.cards = [] if cards is None else cards
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
        if self.can_split:
            card = self.cards.pop()
            new_hand = Hand()
            new_hand.add_card(card)
            return new_hand
        else:
            raise ValueError("Invalid hand to split!")

    @property
    def can_split(self) -> bool:
        """Check if hand can be split."""
        return True if len(self.cards) == 2 and self.cards[0].value == self.cards[1].value else False

    @property
    def is_blackjack(self) -> bool:
        """Check if is blackjack."""
        return True if len(self.cards) == 2 and self.score == 21 \
                       and (self.cards[0].value in ('JACK', 'QUEEN', 'KING')
                            or self.cards[1].value in ('JACK', 'QUEEN', 'KING')) else False

    @property
    def is_soft_hand(self) -> bool:
        """Check if is soft hand."""
        return True if len([i for i in self.cards if i.code == 'AS' or i.code == 'AD'
                            or i.code == 'AC' or i.code == 'AH']) else False

    @property
    def score(self) -> int:
        """Get score of hand."""
        total = 0
        aces = 0

        for card in self.cards:
            if card.value != 'ACE':
                if card.value.isnumeric():
                    total += int(card.value)
                elif card.value in ('JACK', 'QUEEN', 'KING'):
                    total += 10
            else:
                aces += 1

        if aces:
            total += aces - 1
            if total <= 10:
                total += 11
            else:
                total += 1

        return total


class Player:
    """Player."""

    def __init__(self, name: str, strategy: Strategy, coins: int = 100):
        """Init."""
        self.name = name
        self.strategy = strategy
        self.coins = coins
        self.hands = []
        self.strategy.player = self

    def join_table(self):
        """Join table."""
        if not len(self.hands):
            # self.hands.append(Hand())
            self.hands = [Hand()]

    def play_move(self, hand: Hand) -> Move:
        """Play move."""
        return self.strategy.play_move(hand)

    def split_hand(self, hand: Hand) -> bool:
        """Split hand."""
        try:
            new_hand = hand.split()
            pos = self.hands.index(hand)
            self.hands.insert(pos + 1, new_hand)
            return True
        except ValueError as e:
            print(e)
            return False


class GameController:
    """Game controller."""

    PLAYER_START_COINS = 200
    BUY_IN_COST = 10

    def __init__(self, view: GameView):
        """Init."""
        self.view = view
        self.house = Hand()
        self.players = []
        self.deck = None

    def start_game(self) -> None:
        """Start game."""
        self.decks_count = self.view.ask_decks_count()
        self.players_count = self.view.ask_players_count()
        self.bots_count = self.view.ask_bots_count()

        for i in range(self.players_count):
            name = self.view.ask_name(i + 1)
            player = Player(name, HumanStrategy(self.players, self.house, self.decks_count, self.view),
                            GameController.PLAYER_START_COINS)
            # player = Player(name, TestStrategy(self.players, self.house, self.decks_count),
            #                 GameController.PLAYER_START_COINS)
            self.players.append(player)

        for i in range(self.bots_count):
            name = 'Bot' + str(i + 1)
            # bot = Player(name, random.choice(self.load_strategies())(self.players, self.house, self.decks_count),
            #              GameController.PLAYER_START_COINS)
            bot = Player(name, MirrorDealerStrategy(self.players, self.house, self.decks_count),
                         GameController.PLAYER_START_COINS)
            self.players.append(bot)

        self.deck = Deck(self.decks_count, shuffle=True)

    def _draw_card(self, top_down: bool = False) -> Card:
        """Draw card."""
        return self.deck.draw_card(top_down)

    def play_round(self) -> bool:
        """Play round."""
        self.clear_table()
        self.initiate_table()
        self.deal_players()
        self.deal_house_hand()
        self.pay_out()
        self.remove_broked()

        if self.players_count + self.bots_count > 1:
            return True if len(self.players) > 1 else False
        else:
            return True if len(self.players) == 1 else False

    def initiate_table(self):
        """Initiate table."""
        # if self.deck.remaining < 15:
        #    self.deck = Deck(self.decks_count, shuffle=True)

        for player in self.players:
            if player.coins >= GameController.BUY_IN_COST:
                player.join_table()
                player.coins -= GameController.BUY_IN_COST

        for i in range(2):
            for player in self.players:
                if len(player.hands):
                    player.hands[0].add_card(self._draw_card())
            self.house.add_card(self._draw_card(True if i % 2 else False))

    def deal_players(self):
        """Deal with players."""
        for player in self.players:
            for hand in player.hands:
                self.deal_player_hand(player, hand)

    def deal_player_hand(self, player: Player, hand: Hand):
        """Deal player hand."""
        while hand.score < 21:
            self.view.show_table(self.players, self.house, hand)
            decision = player.strategy.play_move(hand)
            if decision == Move.HIT:
                hand.add_card(self._draw_card())
            elif decision == Move.SPLIT:
                if player.coins >= GameController.BUY_IN_COST:
                    if player.split_hand(hand):
                        player.coins -= GameController.BUY_IN_COST
                        self.deal_splitted_hands(player, hand)
            elif decision == Move.DOUBLE_DOWN:
                if player.coins >= GameController.BUY_IN_COST:
                    player.coins -= GameController.BUY_IN_COST
                    hand.double_down(self._draw_card())
                break
            elif decision == Move.SURRENDER:
                hand.is_surrendered = True
                break
            else:  # 'STAND'
                break

    def deal_splitted_hands(self, player: Player, hand: Hand):
        """Deal cards to splitted hands."""
        pos = player.hands.index(hand)
        for i in player.hands[pos:pos + 2]:
            i.add_card(self._draw_card())

    def deal_house_hand(self):
        """Deal house hand."""
        for card in self.house.cards:
            card.top_down = False
        """
        continue_play = False
        for player in self.players:
            for hand in player.hands:
                if hand.score <= 21 and not hand.is_surrendered:
                    continue_play = True
        if continue_play:
        """
        while self.house.score < (18 if self.house.is_soft_hand else 17):
            self.house.add_card(self._draw_card())

    def pay_out(self):
        """Pay out."""
        for player in self.players:
            for hand in player.hands:
                if hand.is_surrendered:
                    player.coins += GameController.BUY_IN_COST // 2
                    continue
                if hand.is_blackjack:
                    player.coins += GameController.BUY_IN_COST + int(GameController.BUY_IN_COST * 1.5) \
                        if not self.house.is_blackjack else 0
                    continue
                bet = GameController.BUY_IN_COST * 2 if hand.is_double_down else GameController.BUY_IN_COST
                if self.house.score <= 21:
                    if hand.score <= 21:
                        if hand.score > self.house.score:
                            player.coins += 2 * bet
                        elif hand.score == self.house.score:
                            player.coins += bet
                else:
                    if hand.score <= 21:
                        player.coins += 2 * bet
        self.view.show_table(self.players, self.house, self.house)

    def remove_broked(self):
        """Remove broke players."""
        broke = [player for player in self.players if player.coins < GameController.BUY_IN_COST]
        for player in broke:
            player.hands = []
            self.players.remove(player)

    def clear_table(self):
        """Clear table."""
        for player in self.players:
            player.hands = []
        self.house.cards = []

    @staticmethod
    def load_strategies() -> list:
        """
        Load strategies.

        @:return list of strategies that are in same package.
        DO NOT EDIT!
        """
        pkg_dir = os.path.dirname(__file__)
        for (module_loader, name, is_pkg) in pkgutil.iter_modules([pkg_dir]):
            importlib.import_module(name)
        return list(filter(lambda x: x.__name__ != HumanStrategy.__name__, Strategy.__subclasses__()))


if __name__ == '__main__':
    game_controller = GameController(FancyView())
    # game_controller = GameController(SimpleView())
    game_controller.start_game()
    game_controller.play_round()
    rounds = 1
    while game_controller.play_round() and rounds < 1000:
        rounds += 1
    print(f"Rounds: {rounds}")
