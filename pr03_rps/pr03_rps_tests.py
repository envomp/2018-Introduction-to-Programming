import pytest
from random import choice
import string
from pr03_rps import reverse_name, ask_user_choice, determine_winner
from random import randint


options = {'rock': 0, 'paper': 1, 'scissors': 2}
computer_choice = ['rock', 'paper', 'scissors'][randint(0, 2)]

def get_random_name():
    return ''.join(choice(string.ascii_lowercase) for i in range(10))

def evaluate_winner(choice: str, name: str, computer: str) -> str: 
    if choice not in options.keys() or computer not in options.keys():
        return 'There is a problem determining the winner.'
    base_str = f'{name} had {choice} and computer had {computer}, hence '
    options.get(choice)
    winner = (3 + options.get(choice) - options.get(computer)) % 3
    if winner == 1: 
        return base_str + f'{name} wins.'
    elif winner == 2: 
        return base_str + 'computer wins.'
    elif winner == 0: 
        return base_str + 'it is a draw.'

def reverse_name_solution(name: str) -> str:
    return name[::-1].lower().capitalize()   

@pytest.mark.timeout(1.0)
def test_reverse_name():
    assert reverse_name('Anna') == 'Anna'
    assert reverse_name('Iris') == 'Siri'

@pytest.mark.timeout(1.0)
def test_reverse_name_empty():
    assert reverse_name('') == ''

@pytest.mark.timeout(1.0)
def test_reverse_name_random():
    name = get_random_name()
    assert reverse_name(name) == reverse_name_solution(name)


@pytest.mark.timeout(1.0)
def test_ask_user_choice():
    assert ask_user_choice('ROCK') == 'rock'
    assert ask_user_choice('PaPeR') == 'paper'
    assert ask_user_choice('Scissors') == 'scissors'

@pytest.mark.timeout(1.0)
def test_determine_winner(): 
    assert determine_winner('rock', 'tristan', 'rock') == evaluate_winner('rock', 'tristan', 'rock')
    assert determine_winner('paper', 'tristan', 'rock') == evaluate_winner('paper', 'tristan', 'rock')
    assert determine_winner('scissors', 'tristan', 'rock') == evaluate_winner('scissors', 'tristan', 'rock')
    assert determine_winner('rock', 'tristan', 'scissors') == evaluate_winner('rock', 'tristan', 'scissors')
    assert determine_winner('sfafsa', 'tristan', 'rock') == evaluate_winner('rock', 'tristan', 'qweqe')