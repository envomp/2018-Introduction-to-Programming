# PR 03 

Tee kaust nimega `pr03_rps` ja sinna kausta lisa fail nimega 

## Teooria

Selle nädala teemaks on sõne. Ülesanede eesmärgiks on anda põgus ülevaade, kuidas töödelda ja vorminada sõnesid (*stringe*). 
Proovi ülesannet lahendada samas järjekorras nagu on funktsioonid antud. 

## Ülesanne

* funktsioon `ask_user_name`, mis küsib kasutaja nime ja tagastab nime korrektselt näiteks: 
```
ask_user_name('kristjan') # Kristjan
ask_user_name('KRISTJAN') # Kristjan
```

* funktsioon `reverse_name`, mis küsib kasuaja nime ja pöörab selle tagurpidi. NB! Oluline oleks, et ümberpööratud nimi algaks suure tähega.
Seega on sul võimalik siin kasutada esimest funktsiooni  `ask_user_name`.

```
reverse_user_name('iris') # Siri
```

* funktsioon `ask_user_choice`, mis küsib kasutaja valikut. Valik on järgnev - 'rock', 'paper', 'scissors', kuid tuleb tähele panna, et korrektne on ka 'ROCK'
```
print(ask_user_choice('midagi on viltu'))  # Sorry, you entered unknown command.
```
* funktsioon `determine_winner`, saab sisendiks mängija nime, mängija valiku ja arvuti valiku ning reverse_name. Funktsioon tagastab sõne, mis on järgneva malli järgi koostatud.
Kui reverse_name on True, siis tuleb nimi ümber pööratada ja kasutada seda malli sees. 
`{player_name} had {player_choice} and computer had {computer_choice}, hence {winner} wins.`
Viigi korral tuleks tagastada: `{player_name} had {player_choice} and computer had {computer_choice}, hence it is a draw.`
Kui mingi sisend on ebakorrektne, näiteks kasutaja on oma valikuks sisestanud `water`, siis peaks funktsioon tagastama `There is a problem determining the winner.`

```
print(determine_winner('scissors', 'Marko', 'rock')) # Marko had scissors and computer had rock, hence computer wins.
print(determine_winner('scissors', 'Marko', 'rock')) # Marko had rock and computer had rock, hence it is a draw.
print(determine_winner('scissors', 'Marko', '123')) # There is a problem determining the winner.
````

## Mall

```
"""Simple version of rock paper and scissors."""

def ask_user_name(name: str) -> str:
    """
    Simple function that asks player name and capitalizes the name.

    :param name: name of the player
    :return: A name that is capitalized.
    """
    pass

def reverse_user_name(name: str) -> str:
    """
    Function that takes in name as a parameter and reverses the name. The name should also be capitalized.

    :param name: name of the player
    :return: A name that is reversed.
    """
    pass

def ask_user_choice(choice: str) -> str: 
    """
    Function that asks for user choice.

    The choice can be uppercase or lowercase string, but the choice must be
    either rock, paper or scissors. If it is, then return a choice that is lowercase.
    Otherwise return 'Sorry, you entered unknown command.'
    :param choice: user choice
    :return: choice or an error message
    """
    pass

def determine_winner(name: str, user_choice: str, computer_choice: str, reverse_name: bool = False) -> str:
    """
    Determine the winner returns a string that has information about who won.

    You should use the functions that you wrote before. You should use ask_user_choice function
    to validate the user choice and use ask_user_name for representing a correct name. If the 
    function parameter reverse is true, then you should also reverse the player name.NB! Use the
    previous functions that you have written!
    
    :param name:player name 
    :param user_choice: 
    :param computer_choice: 
    :param reverse_name: 
    :return: 
    """
    pass


def play_game() -> None:
    """
    Enables you to play the game you just created.
    :return:
    """
    user_name = input("What is your name? ")
    play_more = True
    while play_more:
        computer_choice = ['rock', 'paper', 'scissors'][randint(0, 2)]
        user_choice = ask_user_choice(input("What is your choice? "))
        print(determine_winner(user_name, user_choice, computer_choice))
        play_more = True if input("Do you want to play more ? [Y/N] ").lower() == 'y' else False


if __name__ == "__main__":
    print(ask_user_name('ago'))  # Ago
    print(ask_user_name('AGO'))  # Ago
    print(ask_user_name('MaRtInA'))  # Martina

    print(reverse_user_name('MaRtInA'))  # Anitram
    print(reverse_user_name('AGO'))  # Oga

    print(ask_user_choice('rock'))  # rock
    print(ask_user_choice('ROCK'))  # rock
    print(ask_user_choice('midagi on viltu'))  # Sorry, you entered unknown command.

    # 50% on juba tehtud, tubli töö!

    print(determine_winner('ago', 'rock', 'paper'))  # Ago had rock and computer had paper, hence computer wins.
    print(determine_winner('ago', 'rock', 'paper', True))  # Oga had rock and computer had paper, hence computer wins.
    print(
        determine_winner('loORa', 'SCISSORS', 'paper'))  # Loora had scissors and computer had paper, hence Loora wins.
    print(determine_winner('Shakira', 'waka waka', 'fire'))  # There is a problem determining the winner.
    print(determine_winner('Shakira', 'rock',
                           'sciSSOrs'))  # Shakira had rock and computer had scissors, hence Shakira wins.

    # play_game() # Kommenteeri see rida välja kui kõik funktsioonid on valmis
```

## Lisalugemist

### Sõne 

* [Pydoc](https://ained.ttu.ee/pydoc/string.html)
* [Real Python põhjalik tutvustus sõnedest](https://realpython.com/python-strings/)
* [Ametlik Pythoni dokumentatsioon edasijõudnumatele](https://docs.python.org/3/library/string.html) 


### Funktsioon
* [Pydoc](https://ained.ttu.ee/pydoc/func_overview.html) 

