"""Simple version of rock paper and scissors."""
from random import choice


def normalize_user_name(name: str) -> str:
    """
    Simple function gets player name as input and capitalizes it.

    :param name: name of the player
    :return: A name that is capitalized.
    """
    return name.capitalize()


def reverse_user_name(name: str) -> str:
    """
    Function that takes in name as a parameter and reverses its letters. The name should also be capitalized.

    :param name: name of the player
    :return: A name that is reversed.
    """
    return normalize_user_name(name[::-1])


def check_user_choice(choice: str) -> str:
    """
    Function that checks user's choice.

    The choice can be uppercase or lowercase string, but the choice must be
    either rock, paper or scissors. If it is, then return a choice that is lowercase.
    Otherwise return 'Sorry, you entered unknown command.'
    :param choice: user choice
    :return: choice or an error message
    """
    choices = "rock", "paper", "scissors"

    return choice.lower() if choice.lower() in choices else 'Sorry, you entered unknown command.'


def determine_winner(name: str, user_choice: str, computer_choice: str, reverse_name: bool = False) -> str:
    """
    Determine the winner returns a string that has information about who won.

    You should use the functions that you wrote before. You should use check_user_choice function
    to validate the user choice and use normalize_user_name for representing a correct name. If the
    function parameter reverse is true, then you should also reverse the player name.
    NB! Use the previous functions that you have written!

    :param name:player name
    :param user_choice:
    :param computer_choice:
    :param reverse_name:
    :return:
    """
    name = reverse_user_name(name) if reverse_name else normalize_user_name(name)
    user_choice = check_user_choice(user_choice)
    computer_choice = check_user_choice(computer_choice)
    winner = ""

    if user_choice != 'Sorry, you entered unknown command.' and \
            computer_choice != 'Sorry, you entered unknown command.':
        if user_choice == 'rock':
            if computer_choice == 'paper':
                winner = 'computer'
            elif computer_choice == 'scissors':
                winner = name
        elif user_choice == 'paper':
            if computer_choice == 'scissors':
                winner = 'computer'
            elif computer_choice == 'rock':
                winner = name
        else:  # User choice scissors
            if computer_choice == 'rock':
                winner = 'computer'
            elif computer_choice == 'paper':
                winner = name

        return f"{name} had {user_choice} and computer had {computer_choice}, hence {winner} wins." if winner else \
            f"{name} had {user_choice} and computer had {computer_choice}, hence it is a draw."
    else:
        return 'There is a problem determining the winner.'


def play_game() -> None:
    """
    Enable to play the game.

    :return:
    """
    user_name = input("What is your name? ")
    play_more = True
    while play_more:
        computer_choice = choice(['rock', 'paper', 'scissors'])
        user_choice = check_user_choice(input("What is your choice? "))
        print(determine_winner(user_name, user_choice, computer_choice))
        play_more = True if input("Do you want to play more ? [Y/N] ").lower() == 'y' else False


if __name__ == "__main__":
    play_game()  # Kommenteeri see rida välja kui kõik funktsioonid on valmis
