import pytest
from random import choice
import string
from rps import reverse_user_name, ask_user_choice, determine_winner
from random import randint


def get_random_name():
    return ''.join(choice(string.ascii_lowercase) for i in range(10))


def evaluate_winner(name: str, choice: str, computer_choice: str, reverse: bool = False) -> str:
    options = {'rock': 0, 'paper': 1, 'scissors': 2}
    if choice not in options.keys() or computer_choice.lower() not in options.keys():
        return 'There is a problem determining the winner.'
    name = name[::-1].lower().capitalize() if reverse else name.capitalize()
    base_str = f'{name} had {choice} and computer had {computer_choice}, hence '
    options.get(choice)
    winner = (3 + options.get(choice) - options.get(computer_choice)) % 3
    if winner == 1:
        return base_str + f'{name} wins.'
    elif winner == 2:
        return base_str + 'computer wins.'
    elif winner == 0:
        return base_str + 'it is a draw.'


@pytest.mark.timeout(1.0)
def test_reverse_user_name():
    assert reverse_user_name('Anna') == 'Anna'
    assert reverse_user_name('Iris') == 'Siri'


@pytest.mark.timeout(1.0)
def test_reverse_user_name():
    assert reverse_user_name('') == ''


@pytest.mark.timeout(1.0)
def test_random_reverse_user_name():
    name = get_random_name()
    assert reverse_user_name(name) == name[::-1].capitalize()


@pytest.mark.timeout(1.0)
def test_reverse_user_name():
    name = get_random_name()
    assert reverse_user_name(name) == name[::-1].capitalize()


@pytest.mark.timeout(1.0)
def test_ask_user_choice():
    assert ask_user_choice('ROCK') == 'rock'
    assert ask_user_choice('PaPeR') == 'paper'
    assert ask_user_choice('Scissors') == 'scissors'


@pytest.mark.timeout(1.0)
def test_user_wrong_choice():
    assert ask_user_choice('midagi') == 'Sorry, you entered unknown command.'


@pytest.mark.timeout(1.0)
def test_determine_winner():
    computer_choice = ['rock', 'paper', 'scissors'][randint(0, 2)]
    assert determine_winner('tristan', 'rock', computer_choice) == evaluate_winner('tristan', 'rock', computer_choice)


@pytest.mark.timeout(1.0)
def test_determine_winner_reverse():
    computer_choice = ['rock', 'paper', 'scissors'][randint(0, 2)]
    assert determine_winner('IRIS', 'rock', computer_choice, True) == evaluate_winner('IRIS', 'rock',
                                                                                      computer_choice, True)


def test_determine_winner_reverse_random():
    computer_choice = ['rock', 'paper', 'scissors'][randint(0, 2)]
    user_choice = ['rock', 'paper', 'scissors'][randint(0, 2)]
    assert determine_winner('marTin', user_choice, computer_choice, True) == evaluate_winner('marTin', user_choice,
                                                                                             computer_choice, True)


def test_determine_winner_all_random():
    computer_choice = ['rock', 'paper', 'scissors'][randint(0, 2)]
    user_choice = ['rock', 'paper', 'scissors'][randint(0, 2)]
    name = get_random_name()
    assert determine_winner(name, user_choice, computer_choice, True) == evaluate_winner(name, user_choice,
                                                                                         computer_choice, True)


@pytest.mark.timeout(1.0)
def test_determine_winner_computer_wrong_choice():
    user_choice = ['rock', 'paper', 'scissors'][randint(0, 2)]
    assert determine_winner('Reiko', user_choice, 'waka') == evaluate_winner('Reiko', user_choice, 'waka')
