import requests
import os
import json


class SamePokemonFightException(Exception):
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
        if url.startswith('https://'):
            self.parse_json_to_pokemon_information(url)
        else:
            self.data = json.loads(url)

    def parse_json_to_pokemon_information(self, url):
        all_information = requests.get(url).json()
        speed = attack = defence = special_attack = special_defence = hp = None
        for stat in all_information['stats']:
            name = stat['stat']['name']
            if name == 'speed':
                speed = stat['base_stat']
            if name == 'attack':
                attack = stat['base_stat']
            if name == 'defense':
                defence = stat['base_stat']
            if name == 'special-attack':
                special_attack = stat['base_stat']
            if name == 'special-defense':
                special_defence = stat['base_stat']
            if name == 'hp':
                hp = stat['base_stat']

        self.data = {"name": all_information['name'],
                     "speed": speed,
                     "attack": attack,
                     "defence": defence,
                     "special-attack": special_attack,
                     "special-defence": special_defence,
                     "hp": hp,
                     "types": [x['type']['name'] for x in all_information['types']],
                     "abilities": [x['ability']['name'] for x in all_information['abilities']],
                     "forms": [x['name'] for x in all_information['forms']],
                     "moves": [x['move']['name'] for x in all_information['moves']],
                     "height": all_information['height'], "weight": all_information['weight'],
                     "base_experience": all_information['base_experience']}

    def get_power(self):
        """
        Calculate power of Pokemon.

        :return: Power.
        """
        return (self.experience / self.attack + self.defence) * len(self.name)

    def __str__(self):
        """
        String representation of object.

        :return: Pokemon's name, experience: Pokemon's experience, att: Pokemon's attack level, def: Pokemon's defence level, types: Pokemon's types.
        """
        return json.dumps(self.data)

    def __repr__(self):
        """
        Object representation.

        :return: Pokemon's name
        """
        return f"{self.data['name']}"


class World:
    """World class."""

    def __init__(self, name):
        """
        Class constructor.
        :param name:
        """
        if os.path.isfile(name + '.txt'):
            f = open(name + '.txt', "r")
            self.pokemons = [Pokemon(pokemon) for pokemon in f]
        else:
            self.pokemons = [Pokemon(pokemon['url']) for pokemon in
                             requests.get("https://pokeapi.co/api/v2/pokemon?offset=0&limit=100000").json()[
                                 'results']]  # TODO right now every pokemon gets put into the world, maybe give in the number for limit as an input
            self.dump_pokemons_to_file_as_json(name)

        self.leaderBoard = []
        self.fight()

    def dump_pokemons_to_file_as_json(self, name):
        f = open(name + '.txt', "w")
        for pokemon in self.pokemons:
            f.write(pokemon.__str__() + '\n')
        f.close()

    def fight(self):
        """
        Two people fight with their Pokemons.
        :return: Pokemon which wins.
        """
        for pokemon1 in self.pokemons:
            for pokemon2 in self.pokemons:
                try:
                    stack1 = [pokemon1.data['speed'], pokemon1.data['weight'], pokemon1.data['height'],
                              pokemon1.data['base_experience'], len(pokemon1.data['moves'])]
                    stack2 = [pokemon2.data['speed'], pokemon2.data['weight'], pokemon2.data['height'],
                              pokemon2.data['base_experience'], len(pokemon2.data['moves'])]

                    if all(stack1[x] == stack2[x] for x in range(5)):
                        raise SamePokemonFightException(
                            f"Same base Pokemon: {str(pokemon1.data['name']).split('-')[0]}")

                    if not any([all([stack1[i] > stack2[i] if i % 2 == 0 else stack1[i] < stack2[i],
                                     all(stack1[j] == stack2[j] for j in range(i))]) for i in range(5)]):
                        pokemon1, pokemon2 = pokemon2, pokemon1

                    hp1 = pokemon1.data['hp']
                    hp2 = pokemon2.data['hp']
                    while True:
                        #  TODO some fight logic between pokemon 1 and 2, where pokemon 1 goes first
                        break

                except SamePokemonFightException:
                    continue


def group_pokemons(self):
    """
    Group Pokemons by given format.

    :return: Dictionary of grouped Pokemons.
    """
    pass


def sort_by_type_experience(self):
    """
    Sort Pokemons by type adn experience. The first Pokemons should be Fire type and experience level of under 100.

    :return: List of sorted Pokemons.
    """
    pass


def get_most_experienced_pokemon(self):
    """
    Get the Pokemon(s) which has the maximum experience level.
    """
    pass


def get_min_experience_pokemon(self):
    """
    Get the Pokemon(s) which has the minimum experience level.
    """


class Main:
    if __name__ == '__main__':
        world = World("PokeLand")
