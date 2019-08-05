import requests
import os
from functools import reduce
import json

all_types = ['normal', 'fighting', 'flying', 'poison', 'ground', 'rock', 'bug', 'ghost', 'steel', 'fire', 'water',
             'grass', 'electric', 'psychic', 'ice', 'dragon', 'dark', 'fairy']

pokemon_attack_multipliers = [
    [1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 0.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [2.0, 1.0, 0.5, 0.5, 1.0, 2.0, 0.5, 0.0, 2.0, 1.0, 1.0, 1.0, 1.0, 0.5, 2.0, 1.0, 2.0, 0.5],
    [1.0, 2.0, 1.0, 1.0, 1.0, 0.5, 2.0, 1.0, 0.5, 1.0, 1.0, 2.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 1.0, 0.5, 0.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0],
    [1.0, 1.0, 0.0, 2.0, 1.0, 2.0, 0.5, 1.0, 2.0, 2.0, 1.0, 0.5, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 0.5, 2.0, 1.0, 0.5, 1.0, 2.0, 1.0, 0.5, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0],
    [1.0, 0.5, 0.5, 0.5, 1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 1.0, 2.0, 1.0, 2.0, 1.0, 1.0, 2.0, 0.5],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 0.5, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 0.5, 0.5, 0.5, 1.0, 0.5, 1.0, 2.0, 1.0, 1.0, 2.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 2.0, 1.0, 2.0, 0.5, 0.5, 2.0, 1.0, 1.0, 2.0, 0.5, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 2.0, 0.5, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0],
    [1.0, 1.0, 0.5, 0.5, 2.0, 2.0, 0.5, 1.0, 0.5, 0.5, 2.0, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0],
    [1.0, 1.0, 2.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 0.5, 0.5, 1.0, 1.0, 0.5, 1.0, 1.0],
    [1.0, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 0.0, 1.0],
    [1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 2.0, 1.0, 1.0, 0.5, 2.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 0.0],
    [1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 0.5, 0.5],
    [1.0, 2.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 1.0]]


class SamePokemonFightException(Exception):
    """Custom exception."""
    pass


class PokemonFightResultsInATieException(Exception):
    """Custom exception."""
    pass


class NotAPokemonException(Exception):
    """Custom exception."""
    pass


class Pokemon:
    """Class for Pokemon."""

    def __init__(self, url: str):
        """
        Class constructor.

        :param url: url for pokemon
        """
        self.score = 0
        self.data = {}
        if url.split('/').__contains__("pokeapi.co"):
            self.parse_json_to_pokemon_information(url)
        else:
            self.data = json.loads(url)

    def parse_json_to_pokemon_information(self, url):
        all_information = requests.get(url).json()
        speed = attack = defense = special_attack = special_defense = hp = None
        for stat in all_information['stats']:
            name = stat['stat']['name']
            if name == 'speed':
                speed = stat['base_stat']
            if name == 'attack':
                attack = stat['base_stat']
            if name == 'defense':
                defense = stat['base_stat']
            if name == 'special-attack':
                special_attack = stat['base_stat']
            if name == 'special-defense':
                special_defense = stat['base_stat']
            if name == 'hp':
                hp = stat['base_stat']

        self.data = {"name": all_information['name'],
                     "speed": speed,
                     "attack": attack,
                     "defense": defense,
                     "special-attack": special_attack,
                     "special-defense": special_defense,
                     "hp": hp,
                     "types": [x['type']['name'] for x in all_information['types']],
                     "abilities": [x['ability']['name'] for x in all_information['abilities']],
                     "forms": [x['name'] for x in all_information['forms']],
                     "moves": [x['move']['name'] for x in all_information['moves']],
                     "height": all_information['height'], "weight": all_information['weight'],
                     "base_experience": all_information['base_experience']}

    def get_attack_multiplier(self, other: list):
        """
        Calculate Pokemons attack multiplier against others types and take the best result.

        :return: Multiplier.
        """
        return max(reduce(lambda x, y: x * y,
                          [pokemon_attack_multipliers[all_types.index(self_type)][all_types.index(enemy_type)] for
                           enemy_type in other]) for self_type in
                   self.data['types'])

    def get_pokemon_attack(self, turn_counter):
        return self.data['special-attack'] if turn_counter % 3 == 0 else self.data['attack']

    def get_pokemon_defense(self, turn_counter):
        return self.data['special-defense'] if turn_counter % 2 == 0 else self.data['defense'] / 2

    def __str__(self):
        """
        String representation of object.

        :return: Pokemon's name, experience: Pokemon's experience, att: Pokemon's attack level, def: Pokemon's defense level, types: Pokemon's types.
        """
        return json.dumps(self.data)

    def __repr__(self):
        """
        Object representation.

        :return: Pokemon's name
        """
        return f"{self.data['name']} {self.score}"


class World:
    """World class."""

    def __init__(self, name, offset, limit):
        """
        Class constructor.
        :param name:
        """
        if os.path.isfile(name + '.txt'):
            f = open(f"{name}_{offset}_{limit}.txt", "r")
            self.pokemons = [Pokemon(pokemon) for pokemon in f]
        else:
            self.pokemons = [Pokemon(pokemon['url']) for pokemon in
                             requests.get(f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}").json()[
                                 'results']]
            self.dump_pokemons_to_file_as_json(name, offset, limit)

    def dump_pokemons_to_file_as_json(self, name, offset, limit):
        f = open(f"{name}_{offset}_{limit}.txt", "w")
        for pokemon in self.pokemons:
            f.write(pokemon.__str__() + '\n')
        f.close()

    def fight(self):
        """
        Two people fight with their Pokemons.
        :return: Pokemon which wins.
        """
        for pokemon1 in self.pokemons:
            for pokemon2 in self.pokemons[self.pokemons.index(pokemon1) + 1:]:
                try:
                    first, second = self.choose_which_pokemon_hits_first(pokemon1, pokemon2)

                    hp1 = first.data['hp']
                    hp2 = second.data['hp']
                    multiplier1 = first.get_attack_multiplier(list(second.data['types']))
                    multiplier2 = second.get_attack_multiplier(list(first.data['types']))
                    turn_counter = 1
                    while True:
                        attack1 = max(
                            first.get_pokemon_attack(turn_counter) * multiplier1 - second.get_pokemon_defense(
                                turn_counter), 0)
                        attack2 = max(
                            second.get_pokemon_attack(
                                turn_counter) * multiplier2 - first.get_pokemon_defense(turn_counter), 0)

                        hp2 -= attack1
                        if hp2 <= 0:
                            first.score += 1
                            break
                        hp1 -= attack2
                        if hp1 <= 0:
                            second.score += 1
                            break

                        if turn_counter == 100:
                            raise PokemonFightResultsInATieException()
                        else:
                            turn_counter += 1
                except SamePokemonFightException:
                    continue

                except PokemonFightResultsInATieException:
                    continue

    @staticmethod
    def choose_which_pokemon_hits_first(pokemon1, pokemon2):
        stack1 = [pokemon1.data['speed'], pokemon1.data['weight'], pokemon1.data['height'],
                  len(pokemon1.data['abilities']), len(pokemon1.data['moves']), pokemon1.data['base_experience']]
        stack2 = [pokemon2.data['speed'], pokemon2.data['weight'], pokemon2.data['height'],
                  len(pokemon2.data['abilities']), len(pokemon2.data['moves']), pokemon2.data['base_experience']]
        if all(stack1[x] == stack2[x] for x in range(6)):
            raise SamePokemonFightException(
                f"Same base Pokemon: {str(pokemon1.data['name']).split('-')[0]}")
        if any([all([stack1[i] > stack2[i] if i in [1, 2] else stack1[i] < stack2[i],
                     all(stack1[j] == stack2[j] for j in range(i))]) for i in range(6)]):
            return pokemon1, pokemon2
        return pokemon2, pokemon1

    def get_leader_board(self):
        """
        Get Pokemons by given format.

        :return: List of leader board.
        """
        return list(reversed(sorted(self.pokemons, key=lambda x: x.score)))

    def get_pokemons_sorted_by_attribute(self, attribute: str):
        """

        :param attribute:  pokemon data attribute to sort by
        :return: sorted List of pokemons
        """
        return sorted(self.pokemons, key=lambda x: x.data[attribute])
