# EX13

## Ülesanne

Fail Gitis: `ex13_blackjack/blackjack.py`

### Taust

See ülesanne on jätkuks pr13-le. Nüüd on aeg valmis kirjutada [Blackjack](https://www.blackjack.org/blackjack-rules/) kaardimäng.
Liikse keerukuse vältimiseks on teile ette antud failid `game_view.py` ja `strategy.py`
Ülesandele järgneb ka kolmas osa (TODO), kus saate kirjutada programmi (Strateegia), mis teie vastu mängib.
Plaan on ka tudengite programmide vahel korraldada võistlus.

### Sisu

#### Klass Hand

`def __init__(self, cards: list = None):` Tuleb deklareerida järgnevad muutujad: `self.cards` -> tühi list või argument cards, kui viimane pole None
`self.is_double_down`-> False ja `self.is_surrendered` -> False

`def add_card(self, card: Card) -> None:` Lisab kaardi `self.cards`-ile.

`def double_down(self, card: Card) -> None:`Lisab kaardi ja seab `self.is_double_down = True`

`def split(self):` Splitib handi ehk tagastab teise `Hand objekti`, kus on 1 kahest kaardist. Kui splittida ei saa 
tuleb visata `ValueError` sõnumiga `"Invalid hand to split!"`

`def can_split(self) -> bool:` Tagastab tõeväärtuse, kas kätt saab splittida.

`def is_blackjack(self) -> bool:` Tagastab tõeväärtuse, kas tegu on Blackjackiga (peab olema esimese 2 kaardiga)

`def is_soft_hand(self):` Tagastab tõeväärtuse, kas käsi on "soft" ehk sisaldab ässa.

`def score(self) -> int:` Tagastab käe väärtuse

#### Klass Player

**`def __init__(self, name: str, strategy: Strategy, coins: int = 100):`** Argumendid tuleb salvestada samanimelistesse
klassimuutujatesse. `self.hands` peab olema tühi list. **Lisaks peab strategil seadama player väärtuse!**

`def join_table(self):` Peale funktsiooni välja kutsumist peab `self.hands` sisaldama ühte kätt.

`def play_move(self) -> Move:` Tagastab strateegia poolt valitud käigu.

`def split_hand(self):` Splitib käe

#### Klass GameController

`def start_game(self) -> None:` Alustab mängu, ehk lisab mängijad lauda ja seab valmis decki.
Mängijalt tuleb `self.view` läbi küsida kaardipakkide arv, inimeste arv ja bottide arv ja vastaval sellele
mäng valmis seada.

`def play_round(self) -> bool:` Mängib kõigi mängijatega, kellel on piisavalt raha ühe raundi. 
Raundi lõpus tuleb ka võidud laiali jagada.

`def load_strategies() -> list:` Seda funktsiooni pole vaja näppida. Soovitatav kasutada bottide laadimisel

### Mall

```python
"""Blackjack."""
import importlib
import os
import pkgutil
import random

from deck_solved import Deck, Card
from game_view import GameView, FancyView, Move
from strategy import Strategy, HumanStrategy


class Hand:
    """Hand."""

    def __init__(self, cards: list = None):
        """Init."""
        pass

    def add_card(self, card: Card) -> None:
        """Add card to hand."""
        pass

    def double_down(self, card: Card) -> None:
        """Double down."""
        pass

    def split(self):
        """Split hand."""
        pass

    def can_split(self) -> bool:
        """Check if hand can be split."""
        pass

    @property
    def is_blackjack(self) -> bool:
        """Check if is blackjack"""
        pass

    @property
    def is_soft_hand(self):
        """Check if is soft hand."""
        pass

    @property
    def score(self) -> int:
        """Get score of hand."""
        pass


class Player:
    """Player."""

    def __init__(self, name: str, strategy: Strategy, coins: int = 100):
        """Init."""
        pass

    def join_table(self):
        """Join table."""
        pass

    def play_move(self) -> Move:
        """Play move."""
        pass

    def split_hand(self):
        """Split hand."""
        pass


class GameController:
    """Game controller."""
    
    PLAYER_START_COINS = 200
    BUY_IN_COST = 10

    def __init__(self, view: GameView):
        """Init."""
        pass

    def start_game(self) -> None:
        """Start game"""
        pass

    def play_round(self) -> bool:
        pass

    @staticmethod
    def load_strategies() -> list:
        """
        Load strategies.
        @:return list of strategies that are in same package.
        DO NOT EDIT!
        """
        pkg_dir = os.path.dirname(__file__)
        for (module_loader, name, is_pkg) in pkgutil.iter_modules([pkg_dir]):
            importlib.import_module('.' + name, 'ex13_blackjack')
        return list(filter(lambda x: x.__name__ != HumanStrategy.__name__, Strategy.__subclasses__()))


if __name__ == '__main__':
    game_controller = GameController(FancyView())
    game_controller.start_game()
    while game_controller.play_round():
        pass

```
