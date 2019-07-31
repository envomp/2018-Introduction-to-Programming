import requests
import os
from functools import reduce
import json


class SamePokemonFightException(Exception):
    """Custom exception."""
    pass


class NotAPokemonException(Exception):
    """Custom exception."""
    pass


class Pokemon:
    """Class for Pokemon."""

    def __init__(self, url_or_path_name: str):
        """
        Class constructor.

        :param url_or_path_name: url for pokemon or name for file.
        """
        pass

    def parse_json_to_pokemon_information(self, url):
        """
        :param url: url where the information is requested
        """
        pass

    def get_attack_multiplier(self, other: list):
        """
        Calculate Pokemons attack multiplier against others types and take the best result.
        :return: Multiplier.
        """
        pass

    def get_pokemon_attack(self, turn_counter):
        """
        :param turn_counter: every third round the attack is empowered.
        """
        pass

    def __str__(self):
        """
        String representation of object.

        :return: Pokemon's name, experience: Pokemon's experience, att: Pokemon's attack level, def: Pokemon's defence level, types: Pokemon's types.
        """
        pass

    def __repr__(self):
        """
        Object representation.

        :return: Pokemon's name
        """
        pass


class World:
    """World class."""

    def __init__(self, name):
        """
        Class constructor.
        :param name: name of the pokemon world
        """
        pass

    def dump_pokemons_to_file_as_json(self, name):
        """
        :param name: name of the .txt file
        """
        pass

    def fight(self):
        """
        A wild brawl between all pokemons where points are assigned to pokemons
        """
        pass

    @staticmethod
    def choose_which_pokemon_hits_first(pokemon1, pokemon2):
        """
        :param pokemon1:
        :param pokemon2:

        :return pokemon1 who goes first and pokemon2 who goes second
        """
        pass

    def get_leader_board(self):
        """
        Get Pokemons by given format in a list.

        :return: List of leader board.
        """
        pass


class Main:
    if __name__ == '__main__':
        world = World("PokeLand")
