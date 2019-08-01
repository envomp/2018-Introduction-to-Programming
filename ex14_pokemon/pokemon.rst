Pokemon
========

Fail Gitis: ``ex14_pokemon/pokemon.py`` .
Kirjuta programm, mis teeb api päringu pokeapi.co pihta ja korrastab andmed json kujule, mis tuleb seejärel faili kirjutada.


World
----

url, kust kõik pokemonid kätte saab: https://pokeapi.co/api/v2/pokemon?offset=0&limit=100000

import json'it kasutades saab viia dictionary json kujule

.. code-block:: python

        self.data = {"name": str,
                     "speed": int,
                     "attack": int,
                     "defence": int,
                     "special-attack": int,
                     "special-defence": int,
                     "hp": int,
                     "types": List<str>,
                     "abilities": List<str>,
                     "forms": List<str>,
                     "moves": List<str>,
                     "height": int,
                     "base_experience": int}

näide ühest pokemonist

.. code-block:: python

    {"name": "bulbasaur", "speed": 45, "attack": 49, "defense": 49, "special-attack": 65, "special-defense": 65, "hp": 45, "types": ["poison", "grass"], "abilities": ["chlorophyll", "overgrow"], "forms": ["bulbasaur"], "moves": ["razor-wind", "swords-dance", "cut", "bind", "vine-whip", "headbutt", "tackle", "body-slam", "take-down", "double-edge", "growl", "strength", "mega-drain", "leech-seed", "growth", "razor-leaf", "solar-beam", "poison-powder", "sleep-powder", "petal-dance", "string-shot", "toxic", "rage", "mimic", "double-team", "defense-curl", "light-screen", "reflect", "bide", "sludge", "skull-bash", "amnesia", "flash", "rest", "substitute", "snore", "curse", "protect", "sludge-bomb", "mud-slap", "giga-drain", "endure", "charm", "swagger", "fury-cutter", "attract", "sleep-talk", "return", "frustration", "safeguard", "sweet-scent", "synthesis", "hidden-power", "sunny-day", "rock-smash", "facade", "nature-power", "ingrain", "knock-off", "secret-power", "grass-whistle", "bullet-seed", "magical-leaf", "natural-gift", "worry-seed", "seed-bomb", "energy-ball", "leaf-storm", "power-whip", "captivate", "grass-knot", "venoshock", "round", "echoed-voice", "grass-pledge", "work-up", "grassy-terrain", "confide"], "height": 7, "weight": 69, "base_experience": 64}

kõik pokemonid kirjutada faili worldi konstruktorist sisse saadud <nimi + ".txt"> faili


Fighting multipliers
----

.. code-block:: python

                        normal		fighting	flying		poison		ground		rock		bug		ghost		steel		fire		water		grass	        electric	psychic		ice		dragon		dark		fairy
    normal		1.0		1.0		1.0		1.0		1.0		0.5		1.0		0.0		0.5		1.0		1.0		1.0		1.0		1.0		1.0		1.0		1.0		1.0
    fighting    	2.0		1.0		0.5		0.5		1.0		2.0		0.5		0.0		2.0		1.0		1.0		1.0		1.0		0.5		2.0		1.0		2.0		0.5
    flying		1.0		2.0		1.0		1.0		1.0		0.5		2.0		1.0		0.5		1.0		1.0		2.0		0.5		1.0		1.0		1.0		1.0		1.0
    poison		1.0		1.0		1.0		0.5		0.5		0.5		1.0		0.5		0.0		1.0		1.0		2.0		1.0		1.0		1.0		1.0		1.0		2.0
    ground		1.0		1.0		0.0		2.0		1.0		2.0		0.5		1.0		2.0		2.0		1.0		0.5		2.0		1.0		1.0		1.0		1.0		1.0
    rock		1.0		0.5		2.0		1.0		0.5		1.0		2.0		1.0		0.5		2.0		1.0		1.0		1.0		1.0		2.0		1.0		1.0		1.0
    bug                 1.0		0.5		0.5		0.5		1.0		1.0		1.0		0.5		0.5		0.5		1.0		2.0		1.0		2.0		1.0		1.0		2.0		0.5
    ghost		0.0		1.0		1.0		1.0		1.0		1.0		1.0		2.0		1.0		1.0		1.0		1.0		1.0		2.0		1.0		1.0		0.5		1.0
    steel		1.0		1.0		1.0		1.0		1.0		2.0		1.0		1.0		0.5		0.5		0.5		1.0		0.5		1.0		2.0		1.0		1.0		2.0
    fire		1.0		1.0		1.0		1.0		1.0		0.5		2.0		1.0		2.0		0.5		0.5		2.0		1.0		1.0		2.0		0.5		1.0		1.0
    water		1.0		1.0		1.0		1.0		2.0		2.0		1.0		1.0		1.0		2.0		0.5		0.5		1.0		1.0		1.0		0.5		1.0		1.0
    grass		1.0		1.0		0.5		0.5		2.0		2.0		0.5		1.0		0.5		0.5		2.0		0.5		1.0		1.0		1.0		0.5		1.0		1.0
    electric            1.0		1.0		2.0		1.0		0.0		1.0		1.0		1.0		1.0		1.0		2.0		0.5		0.5		1.0		1.0		0.5		1.0		1.0
    psychic		1.0		2.0		1.0		2.0		1.0		1.0		1.0		1.0		0.5		1.0		1.0		1.0		1.0		0.5		1.0		1.0		0.0		1.0
    ice                 1.0		1.0		2.0		1.0		2.0		1.0		1.0		1.0		0.5		0.5		0.5		2.0		1.0		1.0		0.5		2.0		1.0		1.0
    dragon		1.0		1.0		1.0		1.0		1.0		1.0		1.0		1.0		0.5		1.0		1.0		1.0		1.0		1.0		1.0		2.0		1.0		0.0
    dark		1.0		0.5		1.0		1.0		1.0		1.0		1.0		2.0		1.0		1.0		1.0		1.0		1.0		2.0		1.0		1.0		0.5		0.5
    fairy		1.0		2.0		1.0		0.5		1.0		1.0		1.0		1.0		0.5		0.5		1.0		1.0		1.0		1.0		1.0		2.0		2.0		1.0

PS: Write a quick script to parse it into a matrix :)

.. code-block:: python

    class World:
        """World class."""

        def __init__(self, name):
            """
            Class constructor.
            :param name: name of the pokemon world
            check if f"{name}.txt" file exists, if it does, read pokemons in from that file, if not, then make a api
            request to "https://pokeapi.co/api/v2/pokemon?offset=0&limit=100000" to get all pokemons and dump them to
            f"{name}.txt" file
            """
            self.pokemons = []

        def dump_pokemons_to_file_as_json(self, name):
            """
            :param name: name of the .txt file
            write all self.pokemons separated by a newline to the given filename(if it doesnt exist, then create one)
            PS: write the pokemon.__str__() version, not __repr__() as only name is useless :)
            """
            pass

        def fight(self):
            """
            A wild brawl between all pokemons where points are assigned to winners
            Note, every pokemon fights another pokemon only once
            Fight lasts until one pokemon is dead
            every pokemon hits only 1 time per turn and they take turns when they attack
            call choose_which_pokemon_hits_first(pokemon1, pokemon2): to determine which pokemon hits first
            to get the attack and defense of the pokemon, call pokemon1.get_pokemon_attack()
            and pokemon1.get_pokemon_defense() respectively
            attack is multiplied by the pokemon1.get_attack_multiplier(list(second.data['types'])) multiplier
            total attack is
            pokemon1.get_pokemon_attack(turn_counter) * multiplier1 - second.get_pokemon_defense(turn_counter)
            total attack is subtracted from other pokemons hp
            pokemons can not heal (when total attack is negative, no damage is dealt)
            if the fight lasts more than 100 turns, then PokemonFightResultsInATieException() is thrown
            if one pokemon dies, fight ends and the winner gets 1 point, (self.score += 1)
            every exception thrown by called sub methods must be catched and dealt with.
            """
            pass

        @staticmethod
        def choose_which_pokemon_hits_first(pokemon1, pokemon2):
            """
            :param pokemon1:
            :param pokemon2:
            pokemon who's speed is higher, goes first. if both pokemons have the same speed, then pokemon who's weight
            is lower goes first, if both pokemons have same weight, then pokemon who's height is lower goes first,
            if both pokemons have the same height, then the pokemon with more abilities goes first, if they have the same
            amount of abilities, then the pokemon with more moves goes first, if the pokemons have the same amount of
            moves, then the pokemon with higher base_experience goes first, if the pokemons have the same
            base_experience then SamePokemonFightException() is thrown
            :return pokemon1 who goes first and pokemon2 who goes second (return pokemon1, pokemon2)
            """
            pass

        def get_leader_board(self):
            """
            Get Pokemons by given format in a list sorted by the pokemon.score

            :return: List of leader board. where winners are first
            """
            pass

        def get_pokemons_sorted_by_attribute(self, attribute: str):
            """
            Get Pokemons by given format in a list sorted by the pokemon.data[attribute]
            :param attribute:  pokemon data attribute to sort by
            :return: sorted List of pokemons
            """
            pass


Pokemon
----

.. code-block:: python

    class Pokemon:
        """Class for Pokemon."""

        def __init__(self, url_or_path_name: str):
            """
            Class constructor.
            :param url_or_path_name: url or json object.
            If it is url, then parse information from request to proper
            json file and save it to self.data.
            If it is a string representation of a json object, then parse it into json object and save to self.data
            """
            self.score = 0
            self.data = {}

        def parse_json_to_pokemon_information(self, url):
            """
            :param url: url where the information is requested.
            called from constructor and this method requests data from url to parse it into proper json object
            and then saved under self.data example done previously
            """
            pass

        def get_attack_multiplier(self, other: list):
            """
            self.pokemon is attacking, other is defending
            :param other: list of other pokemon2.data['types']
            Calculate Pokemons attack multiplier against others types and take the best result.
            get the initial multiplier from Fighting Multiplier matrix.
            For example if self.type == ['fire'] and other == ['ground']: return fighting_multipliers['fire']['ground']
            if the defendant has dual types, then multiply the multipliers together.
            if the attacker has dual-types, then the best option is
            chosen(attack can only be of 1 type, choose better[higher multiplier])
            :return: Multiplier.
            """
            pass

        def get_pokemon_attack(self, turn_counter):
            """
            :param turn_counter: every third round the attack is empowered. (return self.data['special-attack'])
            otherwise basic attack is returned (self.data['attack'])
            """
            pass

        def get_pokemon_defense(self, turn_counter):
            """
            Note: whatever the result is returned, return half of it instead (for example return self.data['defense'] / 2)
            :param turn_counter: every second round the defense is empowered. (return self.data['special-defense'])
            otherwise basic defense is returned (self.data['defense'])
            """

        def __str__(self):
            """
            String representation of json(self.data) object.
            One way to accomplish this is to use json.dumps functionality
            :return: string version of json file with necessary information
            """
            pass

        def __repr__(self):
            """
            Object representation.

            :return: Pokemon's name in string format and his score, for example: "garchomp-mega 892"
            """
            pass

Exceptions
----

.. code-block:: python

    class SamePokemonFightException(Exception):
        """Custom exception thrown when same pokemons are fighting."""
        pass


    class PokemonFightResultsInATieException(Exception):
        """Custom exception thrown when the fight lasts longer than 100 rounds."""
        pass


    class NotAPokemonException(Exception):
        """Custom exception thrown when object is not a pokemon."""
        pass