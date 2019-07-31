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

    {"name": "bulbasaur", "speed": 45, "attack": 49, "defence": 49, "special-attack": 65, "special-defence": 65, "hp": 45, "types": ["poison", "grass"], "abilities": ["chlorophyll", "overgrow"], "forms": ["bulbasaur"], "moves": ["razor-wind", "swords-dance", "cut", "bind", "vine-whip", "headbutt", "tackle", "body-slam", "take-down", "double-edge", "growl", "strength", "mega-drain", "leech-seed", "growth", "razor-leaf", "solar-beam", "poison-powder", "sleep-powder", "petal-dance", "string-shot", "toxic", "rage", "mimic", "double-team", "defense-curl", "light-screen", "reflect", "bide", "sludge", "skull-bash", "amnesia", "flash", "rest", "substitute", "snore", "curse", "protect", "sludge-bomb", "mud-slap", "giga-drain", "endure", "charm", "swagger", "fury-cutter", "attract", "sleep-talk", "return", "frustration", "safeguard", "sweet-scent", "synthesis", "hidden-power", "sunny-day", "rock-smash", "facade", "nature-power", "ingrain", "knock-off", "secret-power", "grass-whistle", "bullet-seed", "magical-leaf", "natural-gift", "worry-seed", "seed-bomb", "energy-ball", "leaf-storm", "power-whip", "captivate", "grass-knot", "venoshock", "round", "echoed-voice", "grass-pledge", "work-up", "grassy-terrain", "confide"], "height": 7, "weight": 69, "base_experience": 64}

kõik pokemonid kirjutada faili worldi konstruktorist sisse saadud <nimi + ".txt"> faili


.. code-block:: python

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


Pokemon
----

.. code-block:: python

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
    bug          1.0		0.5		0.5		0.5		1.0		1.0		1.0		0.5		0.5		0.5		1.0		2.0		1.0		2.0		1.0		1.0		2.0		0.5
    ghost		0.0		1.0		1.0		1.0		1.0		1.0		1.0		2.0		1.0		1.0		1.0		1.0		1.0		2.0		1.0		1.0		0.5		1.0
    steel		1.0		1.0		1.0		1.0		1.0		2.0		1.0		1.0		0.5		0.5		0.5		1.0		0.5		1.0		2.0		1.0		1.0		2.0
    fire		1.0		1.0		1.0		1.0		1.0		0.5		2.0		1.0		2.0		0.5		0.5		2.0		1.0		1.0		2.0		0.5		1.0		1.0
    water		1.0		1.0		1.0		1.0		2.0		2.0		1.0		1.0		1.0		2.0		0.5		0.5		1.0		1.0		1.0		0.5		1.0		1.0
    grass		1.0		1.0		0.5		0.5		2.0		2.0		0.5		1.0		0.5		0.5		2.0		0.5		1.0		1.0		1.0		0.5		1.0		1.0
    electric            1.0		1.0		2.0		1.0		0.0		1.0		1.0		1.0		1.0		1.0		2.0		0.5		0.5		1.0		1.0		0.5		1.0		1.0
    psychic		1.0		2.0		1.0		2.0		1.0		1.0		1.0		1.0		0.5		1.0		1.0		1.0		1.0		0.5		1.0		1.0		0.0		1.0
    ice          1.0		1.0		2.0		1.0		2.0		1.0		1.0		1.0		0.5		0.5		0.5		2.0		1.0		1.0		0.5		2.0		1.0		1.0
    dragon		1.0		1.0		1.0		1.0		1.0		1.0		1.0		1.0		0.5		1.0		1.0		1.0		1.0		1.0		1.0		2.0		1.0		0.0
    dark		1.0		0.5		1.0		1.0		1.0		1.0		1.0		2.0		1.0		1.0		1.0		1.0		1.0		2.0		1.0		1.0		0.5		0.5
    fairy		1.0		2.0		1.0		0.5		1.0		1.0		1.0		1.0		0.5		0.5		1.0		1.0		1.0		1.0		1.0		2.0		2.0		1.0

PS: Write a quick script to parse it into a matrix :)

Exceptions
----

.. code-block:: python

    class SamePokemonFightException(Exception):
        """Custom exception."""
        pass


    class NotAPokemonException(Exception):
        """Custom exception."""
        pass
