import pytest
import random
from pokemon import Pokemon, World, SamePokemonFightException
import os
import glob
from functools import reduce

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


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_pokemon_init_from_json():
    pokemon = Pokemon(
        """{"name": "pikachu-original-cap", "speed": 90, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "hp": 35, "types": ["electric"], "abilities": ["lightning-rod", "static"], "forms": ["pikachu-original-cap"], "moves": ["slam", "tail-whip", "growl", "thunder-shock", "thunderbolt", "thunder-wave", "thunder", "toxic", "agility", "quick-attack", "double-team", "light-screen", "rest", "substitute", "protect", "swagger", "spark", "attract", "sleep-talk", "return", "frustration", "hidden-power", "rain-dance", "facade", "brick-break", "feint", "fling", "discharge", "grass-knot", "charge-beam", "electro-ball", "round", "echoed-voice", "volt-switch", "wild-charge", "play-nice", "confide", "nuzzle"], "height": 4, "weight": 60, "base_experience": 112}""")
    assert pokemon.__str__() == """{"name": "pikachu-original-cap", "speed": 90, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "hp": 35, "types": ["electric"], "abilities": ["lightning-rod", "static"], "forms": ["pikachu-original-cap"], "moves": ["slam", "tail-whip", "growl", "thunder-shock", "thunderbolt", "thunder-wave", "thunder", "toxic", "agility", "quick-attack", "double-team", "light-screen", "rest", "substitute", "protect", "swagger", "spark", "attract", "sleep-talk", "return", "frustration", "hidden-power", "rain-dance", "facade", "brick-break", "feint", "fling", "discharge", "grass-knot", "charge-beam", "electro-ball", "round", "echoed-voice", "volt-switch", "wild-charge", "play-nice", "confide", "nuzzle"], "height": 4, "weight": 60, "base_experience": 112}"""


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_world_correct_pokemon_form_repr_and_str():
    world = World("PokeLand", 0, 1)
    assert world.pokemons[
               0].__str__() == """{"name": "bulbasaur", "speed": 45, "attack": 49, "defense": 49, "special-attack": 65, "special-defense": 65, "hp": 45, "types": ["poison", "grass"], "abilities": ["chlorophyll", "overgrow"], "forms": ["bulbasaur"], "moves": ["razor-wind", "swords-dance", "cut", "bind", "vine-whip", "headbutt", "tackle", "body-slam", "take-down", "double-edge", "growl", "strength", "mega-drain", "leech-seed", "growth", "razor-leaf", "solar-beam", "poison-powder", "sleep-powder", "petal-dance", "string-shot", "toxic", "rage", "mimic", "double-team", "defense-curl", "light-screen", "reflect", "bide", "sludge", "skull-bash", "amnesia", "flash", "rest", "substitute", "snore", "curse", "protect", "sludge-bomb", "mud-slap", "giga-drain", "endure", "charm", "swagger", "fury-cutter", "attract", "sleep-talk", "return", "frustration", "safeguard", "sweet-scent", "synthesis", "hidden-power", "sunny-day", "rock-smash", "facade", "nature-power", "ingrain", "knock-off", "secret-power", "grass-whistle", "bullet-seed", "magical-leaf", "natural-gift", "worry-seed", "seed-bomb", "energy-ball", "leaf-storm", "power-whip", "captivate", "grass-knot", "venoshock", "round", "echoed-voice", "grass-pledge", "work-up", "grassy-terrain", "confide"], "height": 7, "weight": 69, "base_experience": 64}"""
    assert world.pokemons[0].__repr__() == 'bulbasaur 0'


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_get_correct_attack_multiplier_one_type():
    pokemon1 = Pokemon(
        """{"name": "pikachu-1", "speed": 90, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "hp": 35, "types": ["electric"], "abilities": ["lightning-rod", "static"], "forms": ["pikachu-original-cap"], "moves": ["slam", "tail-whip", "growl", "thunder-shock", "thunderbolt", "thunder-wave", "thunder", "toxic", "agility", "quick-attack", "double-team", "light-screen", "rest", "substitute", "protect", "swagger", "spark", "attract", "sleep-talk", "return", "frustration", "hidden-power", "rain-dance", "facade", "brick-break", "feint", "fling", "discharge", "grass-knot", "charge-beam", "electro-ball", "round", "echoed-voice", "volt-switch", "wild-charge", "play-nice", "confide", "nuzzle"], "height": 4, "weight": 60, "base_experience": 112}""")

    for type1 in all_types:
        pokemon1.data['types'] = [type1]
        for enemy_type in all_types:
            assert pokemon1.get_attack_multiplier([enemy_type]) == pokemon_attack_multipliers[all_types.index(type1)][
                all_types.index(enemy_type)]


@pytest.mark.timeout(2.0)
@pytest.mark.incgroupdepend("correct")
def test_get_correct_attack_multiplier_two_types():
    pokemon1 = Pokemon(
        """{"name": "pikachu-1", "speed": 90, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "hp": 35, "types": ["electric"], "abilities": ["lightning-rod", "static"], "forms": ["pikachu-original-cap"], "moves": ["slam", "tail-whip", "growl", "thunder-shock", "thunderbolt", "thunder-wave", "thunder", "toxic", "agility", "quick-attack", "double-team", "light-screen", "rest", "substitute", "protect", "swagger", "spark", "attract", "sleep-talk", "return", "frustration", "hidden-power", "rain-dance", "facade", "brick-break", "feint", "fling", "discharge", "grass-knot", "charge-beam", "electro-ball", "round", "echoed-voice", "volt-switch", "wild-charge", "play-nice", "confide", "nuzzle"], "height": 4, "weight": 60, "base_experience": 112}""")

    for type1 in all_types:
        for type2 in all_types:
            if type1 != type2:
                pokemon1.data['types'] = [type1, type2]
                for enemy_type1 in all_types:
                    for enemy_type2 in all_types:
                        if enemy_type1 != enemy_type2:
                            assert pokemon1.get_attack_multiplier([enemy_type1, enemy_type2]) == max(
                                reduce(lambda x, y: x * y, [
                                    pokemon_attack_multipliers[all_types.index(self_type)][all_types.index(enemy_type)]
                                    for enemy_type in [enemy_type1, enemy_type2]]) for self_type in
                                pokemon1.data['types'])


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_get_pokemon_attack():
    pokemon1 = Pokemon(
        """{"name": "pikachu-1", "speed": 90, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "hp": 35, "types": ["electric"], "abilities": ["lightning-rod", "static"], "forms": ["pikachu-original-cap"], "moves": ["slam", "tail-whip", "growl", "thunder-shock", "thunderbolt", "thunder-wave", "thunder", "toxic", "agility", "quick-attack", "double-team", "light-screen", "rest", "substitute", "protect", "swagger", "spark", "attract", "sleep-talk", "return", "frustration", "hidden-power", "rain-dance", "facade", "brick-break", "feint", "fling", "discharge", "grass-knot", "charge-beam", "electro-ball", "round", "echoed-voice", "volt-switch", "wild-charge", "play-nice", "confide", "nuzzle"], "height": 4, "weight": 60, "base_experience": 112}""")
    assert pokemon1.get_pokemon_attack(1) == 55
    assert pokemon1.get_pokemon_attack(3) == 50
    assert pokemon1.get_pokemon_attack(11) == 55
    assert pokemon1.get_pokemon_attack(12) == 50


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_get_pokemon_defense():
    pokemon1 = Pokemon(
        """{"name": "pikachu-1", "speed": 90, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "hp": 35, "types": ["electric"], "abilities": ["lightning-rod", "static"], "forms": ["pikachu-original-cap"], "moves": ["slam", "tail-whip", "growl", "thunder-shock", "thunderbolt", "thunder-wave", "thunder", "toxic", "agility", "quick-attack", "double-team", "light-screen", "rest", "substitute", "protect", "swagger", "spark", "attract", "sleep-talk", "return", "frustration", "hidden-power", "rain-dance", "facade", "brick-break", "feint", "fling", "discharge", "grass-knot", "charge-beam", "electro-ball", "round", "echoed-voice", "volt-switch", "wild-charge", "play-nice", "confide", "nuzzle"], "height": 4, "weight": 60, "base_experience": 112}""")
    assert pokemon1.get_pokemon_defense(1) == 20
    assert pokemon1.get_pokemon_defense(2) == 25
    assert pokemon1.get_pokemon_defense(3) == 20
    assert pokemon1.get_pokemon_defense(4) == 25


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_choose_which_pokemon_hits_first_speed_only():
    pokemon1 = Pokemon(
        """{"name": "pikachu-1", "speed": 90, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "hp": 35, "types": ["electric"], "abilities": ["lightning-rod", "static"], "forms": ["pikachu-original-cap"], "moves": ["slam", "tail-whip", "growl", "thunder-shock", "thunderbolt", "thunder-wave", "thunder", "toxic", "agility", "quick-attack", "double-team", "light-screen", "rest", "substitute", "protect", "swagger", "spark", "attract", "sleep-talk", "return", "frustration", "hidden-power", "rain-dance", "facade", "brick-break", "feint", "fling", "discharge", "grass-knot", "charge-beam", "electro-ball", "round", "echoed-voice", "volt-switch", "wild-charge", "play-nice", "confide", "nuzzle"], "height": 4, "weight": 60, "base_experience": 112}""")
    pokemon2 = Pokemon(
        """{"name": "pikachu-2", "speed": 91, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "hp": 35, "types": ["electric"], "abilities": ["lightning-rod", "static"], "forms": ["pikachu-original-cap"], "moves": ["slam", "tail-whip", "growl", "thunder-shock", "thunderbolt", "thunder-wave", "thunder", "toxic", "agility", "quick-attack", "double-team", "light-screen", "rest", "substitute", "protect", "swagger", "spark", "attract", "sleep-talk", "return", "frustration", "hidden-power", "rain-dance", "facade", "brick-break", "feint", "fling", "discharge", "grass-knot", "charge-beam", "electro-ball", "round", "echoed-voice", "volt-switch", "wild-charge", "play-nice", "confide", "nuzzle"], "height": 4, "weight": 60, "base_experience": 112}""")
    assert pokemon1, pokemon2 == World.choose_which_pokemon_hits_first(pokemon2, pokemon1)
    assert pokemon1, pokemon2 == World.choose_which_pokemon_hits_first(pokemon1, pokemon2)


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_choose_which_pokemon_hits_first_speed_weight():
    pokemon1 = Pokemon(
        """{"name": "pikachu-1", "speed": 90, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "hp": 35, "types": ["electric"], "abilities": ["lightning-rod", "static"], "forms": ["pikachu-original-cap"], "moves": ["slam", "tail-whip", "growl", "thunder-shock", "thunderbolt", "thunder-wave", "thunder", "toxic", "agility", "quick-attack", "double-team", "light-screen", "rest", "substitute", "protect", "swagger", "spark", "attract", "sleep-talk", "return", "frustration", "hidden-power", "rain-dance", "facade", "brick-break", "feint", "fling", "discharge", "grass-knot", "charge-beam", "electro-ball", "round", "echoed-voice", "volt-switch", "wild-charge", "play-nice", "confide", "nuzzle"], "height": 4, "weight": 59, "base_experience": 112}""")
    pokemon2 = Pokemon(
        """{"name": "pikachu-2", "speed": 90, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "hp": 35, "types": ["electric"], "abilities": ["lightning-rod", "static"], "forms": ["pikachu-original-cap"], "moves": ["slam", "tail-whip", "growl", "thunder-shock", "thunderbolt", "thunder-wave", "thunder", "toxic", "agility", "quick-attack", "double-team", "light-screen", "rest", "substitute", "protect", "swagger", "spark", "attract", "sleep-talk", "return", "frustration", "hidden-power", "rain-dance", "facade", "brick-break", "feint", "fling", "discharge", "grass-knot", "charge-beam", "electro-ball", "round", "echoed-voice", "volt-switch", "wild-charge", "play-nice", "confide", "nuzzle"], "height": 4, "weight": 60, "base_experience": 112}""")
    assert pokemon1, pokemon2 == World.choose_which_pokemon_hits_first(pokemon2, pokemon1)
    assert pokemon1, pokemon2 == World.choose_which_pokemon_hits_first(pokemon1, pokemon2)


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_choose_which_pokemon_hits_first_speed_weight_height():
    pokemon1 = Pokemon(
        """{"name": "pikachu-1", "speed": 90, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "hp": 35, "types": ["electric"], "abilities": ["lightning-rod", "static"], "forms": ["pikachu-original-cap"], "moves": ["slam", "tail-whip", "growl", "thunder-shock", "thunderbolt", "thunder-wave", "thunder", "toxic", "agility", "quick-attack", "double-team", "light-screen", "rest", "substitute", "protect", "swagger", "spark", "attract", "sleep-talk", "return", "frustration", "hidden-power", "rain-dance", "facade", "brick-break", "feint", "fling", "discharge", "grass-knot", "charge-beam", "electro-ball", "round", "echoed-voice", "volt-switch", "wild-charge", "play-nice", "confide", "nuzzle"], "height": 3, "weight": 60, "base_experience": 112}""")
    pokemon2 = Pokemon(
        """{"name": "pikachu-2", "speed": 90, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "hp": 35, "types": ["electric"], "abilities": ["lightning-rod", "static"], "forms": ["pikachu-original-cap"], "moves": ["slam", "tail-whip", "growl", "thunder-shock", "thunderbolt", "thunder-wave", "thunder", "toxic", "agility", "quick-attack", "double-team", "light-screen", "rest", "substitute", "protect", "swagger", "spark", "attract", "sleep-talk", "return", "frustration", "hidden-power", "rain-dance", "facade", "brick-break", "feint", "fling", "discharge", "grass-knot", "charge-beam", "electro-ball", "round", "echoed-voice", "volt-switch", "wild-charge", "play-nice", "confide", "nuzzle"], "height": 4, "weight": 60, "base_experience": 112}""")
    assert pokemon1, pokemon2 == World.choose_which_pokemon_hits_first(pokemon2, pokemon1)
    assert pokemon1, pokemon2 == World.choose_which_pokemon_hits_first(pokemon1, pokemon2)


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_choose_which_pokemon_hits_first_all_6():
    pokemon1 = Pokemon(
        """{"name": "pikachu-1", "speed": 90, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "hp": 35, "types": ["electric"], "abilities": ["lightning-rod", "static"], "forms": ["pikachu-original-cap"], "moves": ["slam", "tail-whip", "growl", "thunder-shock", "thunderbolt", "thunder-wave", "thunder", "toxic", "agility", "quick-attack", "double-team", "light-screen", "rest", "substitute", "protect", "swagger", "spark", "attract", "sleep-talk", "return", "frustration", "hidden-power", "rain-dance", "facade", "brick-break", "feint", "fling", "discharge", "grass-knot", "charge-beam", "electro-ball", "round", "echoed-voice", "volt-switch", "wild-charge", "play-nice", "confide", "nuzzle"], "height": 4, "weight": 60, "base_experience": 113}""")
    pokemon2 = Pokemon(
        """{"name": "pikachu-2", "speed": 90, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "hp": 35, "types": ["electric"], "abilities": ["lightning-rod", "static"], "forms": ["pikachu-original-cap"], "moves": ["slam", "tail-whip", "growl", "thunder-shock", "thunderbolt", "thunder-wave", "thunder", "toxic", "agility", "quick-attack", "double-team", "light-screen", "rest", "substitute", "protect", "swagger", "spark", "attract", "sleep-talk", "return", "frustration", "hidden-power", "rain-dance", "facade", "brick-break", "feint", "fling", "discharge", "grass-knot", "charge-beam", "electro-ball", "round", "echoed-voice", "volt-switch", "wild-charge", "play-nice", "confide", "nuzzle"], "height": 4, "weight": 60, "base_experience": 112}""")
    assert pokemon1, pokemon2 == World.choose_which_pokemon_hits_first(pokemon2, pokemon1)
    assert pokemon1, pokemon2 == World.choose_which_pokemon_hits_first(pokemon1, pokemon2)


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_choose_which_pokemon_hits_exception_thrown():
    pokemon1 = Pokemon(
        """{"name": "pikachu-1", "speed": 90, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "hp": 35, "types": ["electric"], "abilities": ["lightning-rod", "static"], "forms": ["pikachu-original-cap"], "moves": ["slam", "tail-whip", "growl", "thunder-shock", "thunderbolt", "thunder-wave", "thunder", "toxic", "agility", "quick-attack", "double-team", "light-screen", "rest", "substitute", "protect", "swagger", "spark", "attract", "sleep-talk", "return", "frustration", "hidden-power", "rain-dance", "facade", "brick-break", "feint", "fling", "discharge", "grass-knot", "charge-beam", "electro-ball", "round", "echoed-voice", "volt-switch", "wild-charge", "play-nice", "confide", "nuzzle"], "height": 4, "weight": 60, "base_experience": 112}""")
    pokemon2 = Pokemon(
        """{"name": "pikachu-2", "speed": 90, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "hp": 35, "types": ["electric"], "abilities": ["lightning-rod", "static"], "forms": ["pikachu-original-cap"], "moves": ["slam", "tail-whip", "growl", "thunder-shock", "thunderbolt", "thunder-wave", "thunder", "toxic", "agility", "quick-attack", "double-team", "light-screen", "rest", "substitute", "protect", "swagger", "spark", "attract", "sleep-talk", "return", "frustration", "hidden-power", "rain-dance", "facade", "brick-break", "feint", "fling", "discharge", "grass-knot", "charge-beam", "electro-ball", "round", "echoed-voice", "volt-switch", "wild-charge", "play-nice", "confide", "nuzzle"], "height": 4, "weight": 60, "base_experience": 112}""")

    try:
        World.choose_which_pokemon_hits_first(pokemon2, pokemon1)
    except SamePokemonFightException:
        return
    assert False


@pytest.mark.timeout(5.0)
@pytest.mark.incgroupdepend("correct")
def test_world_right_amount_of_pokemons_requested():
    for filename in glob.glob("./PokeLand*"):
        os.remove(filename)  # blow up all previous files

    world = World("PokeLand", 0, 1)
    assert len(world.pokemons) == 1

    world2 = World("PokeLand", 0, 100)
    assert len(world2.pokemons) == 100


@pytest.mark.timeout(2.0)
@pytest.mark.incgroupdepend("correct")
def test_world_reading_from_file():
    world = World("PokeLand", 0, 1)
    assert len(world.pokemons) == 1

    world2 = World("PokeLand", 0, 1)
    assert len(world2.pokemons) == 1


@pytest.mark.timeout(2.0)
@pytest.mark.incgroupdepend("correct")
def test_random_pokemon_correct_form_repr_and_writing_to_file():
    rando = random.randint(0, 900)
    world = World("PokeLand", rando, 1)
    f = open('all_pokemons_0_100000.txt')
    assert f.readlines()[rando] == world.pokemons[0].__str__() + '\n'


@pytest.mark.timeout(5.0)
@pytest.mark.incgroupdepend("correct")
def test_world_100_pokemons_attribute():
    world = World("all_pokemons", 69, 100)
    real = ["chansey 0", "magikarp 0", "ledyba 0", "voltorb 0", "hoothoot 0", "magnemite 0", "gastly 0", "ledian 0",
            "tentacool 0", "exeggcute 0", "horsea 0", "omanyte 0", "seel 0", "onix 0", "staryu 0", "mr-mime 0",
            "sentret 0", "drowzee 0", "ditto 0", "chikorita 0", "haunter 0", "electrode 0", "cubone 0", "jynx 0",
            "noctowl 0", "cyndaquil 0", "lickitung 0", "tangela 0", "eevee 0", "magneton 0", "porygon 0", "omastar 0",
            "spinarak 0", "bayleef 0", "dratini 0", "quilava 0", "slowpoke 0", "shellder 0", "gengar 0", "koffing 0",
            "seadra 0", "vaporeon 0", "jolteon 0", "totodile 0", "goldeen 0", "tentacruel 0", "dewgong 0", "hypno 0",
            "slowbro 0", "starmie 0", "furret 0", "geodude 0", "grimer 0", "marowak 0", "kabuto 0", "croconaw 0",
            "meganium 0", "electabuzz 0", "dragonair 0", "typhlosion 0", "ponyta 0", "doduo 0", "rhyhorn 0", "lapras 0",
            "articuno 0", "weepinbell 0", "farfetchd 0", "weezing 0", "zapdos 0", "ariados 0", "crobat 0", "seaking 0",
            "graveler 0", "cloyster 0", "exeggutor 0", "kangaskhan 0", "magmar 0", "rapidash 0", "tauros 0",
            "moltres 0", "mew 0", "victreebel 0", "muk 0", "krabby 0", "hitmonchan 0", "aerodactyl 0", "feraligatr 0",
            "dodrio 0", "scyther 0", "snorlax 0", "mewtwo 0", "kabutops 0", "golem 0", "hitmonlee 0", "pinsir 0",
            "gyarados 0", "kingler 0", "rhydon 0", "flareon 0", "dragonite 0"]
    for index, pokemon in enumerate(world.get_pokemons_sorted_by_attribute('attack')):
        assert pokemon.__repr__() == real[index]


@pytest.mark.timeout(2.0)
@pytest.mark.incgroupdepend("correct")
def test_world_fight_between_some_pokemons_leaderboard():
    world = World("all_pokemons", 420, 20)
    world.fight()
    real = ["gastrodon 18", "honchkrow 17", "skuntank 17", "bronzong 15", "bonsly 14", "drifblim 14", "drifloon 11",
            "lopunny 10", "stunky 10", "ambipom 9", "cherrim 9", "purugly 9", "shellos 7", "bronzor 5", "buneary 5",
            "mismagius 4", "glameow 3", "mime-jr 2", "chingling 1", "happiny 0"]
    for index, pokemon in enumerate(world.get_leader_board()):
        assert pokemon.__repr__() == real[index]


@pytest.mark.timeout(5.0)
@pytest.mark.incgroupdepend("correct")
def test_world_fight_between_100_pokemons_leaderboard():
    world = World("all_pokemons", 69, 100)
    world.fight()
    real = ["rhydon 92", "snorlax 91", "dragonite 86", "slowbro 86", "golem 84", "gyarados 84", "exeggutor 83",
            "mewtwo 83", "lapras 82", "feraligatr 81", "mew 80", "kabutops 79", "graveler 78", "kingler 76", "muk 76",
            "rhyhorn 75", "zapdos 75", "articuno 73", "geodude 72", "magneton 72", "cloyster 70", "kangaskhan 69",
            "slowpoke 69", "moltres 67", "omastar 67", "tentacruel 67", "victreebel 67", "starmie 66", "ariados 65",
            "vaporeon 65", "aerodactyl 64", "weezing 64", "dewgong 63", "seaking 63", "hypno 62", "flareon 61",
            "scyther 61", "weepinbell 61", "pinsir 59", "kabuto 58", "dragonair 57", "tauros 57", "crobat 56",
            "croconaw 54", "grimer 54", "meganium 54", "electabuzz 52", "hitmonchan 52", "marowak 52", "krabby 51",
            "dodrio 50", "typhlosion 49", "farfetchd 48", "jolteon 46", "exeggcute 45", "hitmonlee 45", "noctowl 45",
            "rapidash 45", "furret 44", "magmar 44", "gengar 43", "seadra 42", "onix 41", "porygon 41", "tangela 41",
            "omanyte 40", "totodile 39", "bayleef 38", "lickitung 37", "magnemite 37", "cubone 35", "dratini 34",
            "koffing 34", "goldeen 32", "haunter 31", "shellder 31", "doduo 30", "electrode 30", "mr-mime 30",
            "ponyta 29", "quilava 29", "chikorita 28", "jynx 28", "seel 27", "drowzee 24", "spinarak 24",
            "tentacool 23", "ledian 22", "gastly 21", "cyndaquil 18", "eevee 16", "staryu 15", "horsea 13", "ditto 11",
            "ledyba 10", "hoothoot 9", "voltorb 7", "sentret 6", "chansey 5", "magikarp 0"]
    for index, pokemon in enumerate(world.get_leader_board()):
        assert pokemon.__repr__() == real[index]


@pytest.mark.timeout(60.0)
@pytest.mark.incgroupdepend("correct")
def test_world_fight_between_all_pokemons_leaderboard():
    world = World("all_pokemons", 0, 100000)
    world.fight()
    real = ["zygarde-complete 920", "steelix-mega 902", "garchomp-mega 892", "golisopod 890", "stakataka 883",
            "rhyperior 878", "giratina-origin 870", "doublade 862", "guzzlord 862", "crabominable 860",
            "giratina-altered 860", "necrozma-dusk 860", "zekrom 860", "yveltal 857", "dialga 856", "camerupt-mega 854",
            "scizor-mega 853", "swampert-mega 853", "dhelmise 851", "escavalier 851", "solgaleo 851", "gyarados 847",
            "muk-alola 844", "rhydon 843", "celesteela 841", "aegislash-blade 836", "pangoro 834", "gyarados-mega 831",
            "carracosta 830", "groudon-primal 830", "kyurem-black 830", "metagross 830", "mewtwo-mega-x 828",
            "tyranitar-mega 827", "palkia 826", "necrozma-dawn 825", "abomasnow-mega 823", "landorus-therian 823",
            "xerneas 822", "kyogre-primal 821", "ampharos-mega 819", "dragonite 816", "aggron-mega 815", "reshiram 813",
            "rayquaza 809", "slaking 809", "lunala 808", "steelix 808", "armaldo 805", "bewear 805", "garchomp 805",
            "bisharp 803", "zygarde-50 803", "heracross-mega 802", "zygarde 802", "ho-oh 800", "regigigas 800",
            "swampert 800", "golem-alola 799", "kyurem 797", "metagross-mega 797", "honchkrow 796", "scizor 795",
            "hoopa-unbound 794", "rayquaza-mega 794", "wishiwashi-school 793", "gigalith 792", "kyurem-white 792",
            "aggron 791", "magearna 791", "magearna-original 791", "slowbro-mega 791", "ferrothorn 789",
            "gourgeist-super 787", "mawile-mega 784", "golem 782", "mamoswine 782", "charizard-mega-x 781",
            "emboar 781", "forretress 781", "granbull 781", "salamence-mega 781", "buzzwole 779", "druddigon 777",
            "exeggutor-alola 777", "piloswine 776", "tyranitar 776", "crustle 775", "golurk 774", "kartana 772",
            "snorlax 772", "trevenant 771", "excadrill 769", "altaria-mega 768", "lapras 768", "landorus-incarnate 767",
            "bronzong 766", "cradily 765", "salamence 765", "tyrantrum 765", "empoleon 764", "avalugg 763",
            "braviary 761", "incineroar 761", "volcanion 759", "mewtwo-mega-y 758", "rampardos 756", "crawdaunt 751",
            "arceus 750", "sableye-mega 749", "gastrodon 747", "magnezone 746", "toucannon 746", "genesect 743",
            "necrozma-ultra 741", "seismitoad 741", "beartic 740", "haxorus 740", "hoopa 740", "kingdra 737",
            "skarmory 733", "turtonator 733", "tapu-bulu 731", "spiritomb 730", "torterra 730", "quagsire 729",
            "ursaring 729", "slowbro 728", "walrein 728", "jirachi 727", "relicanth 727", "kommo-o-totem 726",
            "skuntank 726", "kommo-o 724", "scrafty 724", "kyogre 723", "zapdos 723", "diancie 722", "eelektross 722",
            "mudsdale 722", "conkeldurr 721", "camerupt 720", "gourgeist-large 720", "blastoise-mega 719",
            "gliscor 718", "lairon 716", "slowking 716", "lugia 715", "gallade-mega 714", "kangaskhan-mega 714",
            "cobalion 712", "groudon 711", "venusaur-mega 711", "barbaracle 710", "honedge 710", "regirock 710",
            "bouffalant 705", "goodra 705", "lucario-mega 705", "decidueye 704", "graveler 704", "necrozma 701",
            "articuno 700", "gallade 699", "luxray 699", "thundurus-incarnate 699", "hippowdon 698",
            "sandslash-alola 698", "thundurus-therian 698", "banette-mega 697", "graveler-alola 697", "marshadow 697",
            "moltres 696", "palossand 695", "wailord 695", "audino-mega 694", "drapion 694", "poliwrath 694",
            "charjabug 693", "amoonguss 692", "donphan 691", "muk 691", "fraxure 689", "tapu-fini 689", "whiscash 688",
            "exeggutor 687", "feraligatr 687", "latios-mega 686", "rhyhorn 686", "cloyster 684", "hariyama 684",
            "hydreigon 683", "pinsir-mega 683", "toxapex 682", "drifblim 681", "samurott 681", "stunfisk 681",
            "aurorus 680", "mawile 680", "vikavolt-totem 680", "boldore 678", "dusknoir 678", "primarina 678",
            "togedemaru-totem 678", "vikavolt 678", "klefki 677", "togedemaru 677", "krookodile 676", "latias-mega 676",
            "cacturne 675", "blaziken 674", "kabutops 674", "manaphy 674", "octillery 674", "abomasnow 673",
            "heatran 673", "kingler 673", "aegislash-shield 671", "meloetta-pirouette 671", "tapu-koko 670",
            "gumshoos-totem 668", "lucario 667", "grimer-alola 666", "blaziken-mega 665", "mesprit 665",
            "jellicent 664", "araquanid-totem 663", "durant 663", "gumshoos 663", "nidoqueen 663", "registeel 663",
            "araquanid 662", "unfezant 662", "machamp 661", "staraptor 660", "victini 660", "type-null 659",
            "marowak-totem 658", "mewtwo 658", "qwilfish 658", "dragalge 657", "marowak-alola 656",
            "charizard-mega-y 655", "malamar 655", "chesnaught 654", "gourgeist-average 654", "meloetta-aria 654",
            "sudowoodo 654", "lickilicky 653", "wigglytuff 653", "electivire 652", "shelgon 652", "heracross 651",
            "suicune 650", "pignite 649", "magneton 646", "wormadam-trash 646", "huntail 645", "stoutland 645",
            "tirtouga 645", "aerodactyl-mega 643", "aromatisse 643", "flygon 642", "throh 642",
            "darmanitan-standard 640", "geodude 639", "mew 639", "solrock 639", "vespiquen 639", "absol 638",
            "metang 638", "terrakion 636", "wormadam-sandy 636", "nidoking 635", "probopass 634", "marshtomp 633",
            "zeraora 633", "entei 632", "tyrunt 630", "victreebel 630", "toxicroak 628", "cresselia 627",
            "ampharos 625", "mandibuzz 625", "sharpedo-mega 625", "zweilous 624", "torkoal 620", "archeops 619",
            "passimian 619", "tornadus-incarnate 617", "geodude-alola 614", "bastiodon 613", "cranidos 613",
            "flareon 613", "gurdurr 613", "celebi 610", "mimikyu-totem-disguised 610", "lycanroc-midnight 609",
            "mimikyu-totem-busted 609", "mimikyu-busted 608", "blastoise 607", "mimikyu-disguised 607", "breloom 603",
            "dewgong 601", "klinklang 601", "munchlax 601", "greninja-ash 600", "pawniard 600", "alomomola 599",
            "swanna 599", "diancie-mega 598", "banette 597", "tentacruel 597", "vaporeon 597", "silvally 596",
            "exploud 595", "shaymin-sky 595", "tangrowth 595", "ariados 594", "vileplume 593", "glalie-mega 592",
            "kangaskhan 592", "komala 592", "sandshrew-alola 592", "altaria 591", "tropius 591", "slurpuff 590",
            "xurkitree 590", "gligar 589", "latios 588", "tapu-lele 588", "garbodor 587", "pupitar 587", "aron 586",
            "latias 586", "arcanine 585", "bruxish 585", "clefable 585", "lopunny-mega 585", "reuniclus 585",
            "sylveon 584", "weezing 584", "aerodactyl 583", "gabite 583", "houndoom-mega 583", "archen 582",
            "raikou 580", "uxie 580", "musharna 579", "rotom-fan 579", "shiftry 579", "parasect 578", "charizard 577",
            "heatmor 577", "umbreon 577", "dartrix 576", "gourgeist-small 576", "klang 576", "tsareena 576",
            "drampa 575", "lanturn 575", "absol-mega 574", "deoxys-defense 572", "azelf 571", "keldeo-ordinary 569",
            "keldeo-resolute 569", "politoed 569", "vanilluxe 569", "gardevoir-mega 567", "bibarel 566",
            "tornadus-therian 566", "infernape 565", "regice 565", "venusaur 565", "porygon2 564",
            "oricorio-pom-pom 563", "sharpedo 563", "machoke 562", "omastar 562", "seaking 560", "eelektrik 559",
            "darmanitan-zen 556", "gogoat 556", "gorebyss 554", "sandslash 554", "sawk 554", "beheeyem 553",
            "hawlucha 553", "medicham-mega 553", "oranguru 553", "pinsir 552", "zangoose 552", "golett 551",
            "seviper 551", "slowpoke 551", "blacephalon 547", "lurantis-totem 547", "combusken 546", "lurantis 545",
            "minior-blue-meteor 545", "minior-green-meteor 545", "minior-indigo-meteor 545", "minior-orange-meteor 545",
            "minior-red-meteor 545", "minior-violet-meteor 545", "minior-yellow-meteor 545", "crobat 544", "sealeo 544",
            "hakamo-o 543", "magmortar 543", "scyther 543", "rotom-heat 542", "florges 541", "togekiss 541",
            "magcargo 540", "milotic 540", "virizion 540", "azumarill 539", "dusclops 539", "bonsly 538",
            "houndoom 538", "froslass 537", "swalot 537", "mudbray 534", "pumpkaboo-super 533", "mothim 532",
            "shaymin-land 532", "weavile 532", "chandelure 531", "clawitzer 531", "rotom-wash 530", "sawsbuck 528",
            "scraggy 528", "weepinbell 528", "golduck 527", "mightyena 526", "ferroseed 525", "golbat 525",
            "ludicolo 525", "greninja-battle-bond 524", "noivern 524", "rotom-frost 524", "talonflame 524",
            "floatzel 523", "greninja 523", "lycanroc-dusk 523", "pidgeot-mega 523", "carbink 521", "rufflet 520",
            "yanmega 520", "lycanroc-midday 519", "dodrio 518", "hypno 518", "kecleon 517", "sableye 517", "phione 516",
            "phantump 515", "pidgeot 515", "oricorio-sensu 514", "darkrai 513", "mantine 513", "pumpkaboo-large 513",
            "cofagrigus 512", "zebstrika 511", "carnivine 510", "naganadel 510", "delphox 508", "leafeon 508",
            "pelipper 507", "claydol 505", "roggenrola 504", "tauros 504", "glalie 503", "leavanny 503", "wailmer 503",
            "gardevoir 501", "glaceon 501", "nihilego 501", "sliggoo 501", "trapinch 501", "corsola 498",
            "dragonair 498", "dwebble 498", "kabuto 498", "darumaka 497", "grimer 497", "larvesta 497",
            "pumpkaboo-average 497", "typhlosion 496", "simipour 495", "pyukumuku 494", "galvantula 493", "krabby 492",
            "bellossom 491", "farfetchd 491", "croconaw 490", "arbok 489", "oricorio-baile 489", "miltank 488",
            "rotom-mow 488", "amaura 487", "snubbull 487", "sceptile-mega 486", "zygarde-10 485", "ninetales-alola 482",
            "simisear 482", "anorith 481", "girafarig 480", "grotle 480", "marowak 480", "skrelp 479", "snover 479",
            "tranquill 479", "floette-eternal 478", "magmar 477", "sandygast 476", "hitmontop 474", "ninetales 474",
            "gible 473", "lileep 472", "volcarona 471", "dewott 470", "pumpkaboo-small 470", "rapidash 470",
            "gloom 469", "stantler 469", "starmie 467", "lunatone 465", "meganium 465", "numel 465", "dunsparce 463",
            "pyroar 463", "shedinja 462", "luxio 461", "palpitoad 461", "larvitar 460", "manectric-mega 460",
            "rotom 460", "porygon-z 459", "hitmonchan 458", "fearow 455", "zoroark 455", "gengar-mega 454",
            "minior-blue 454", "minior-green 454", "minior-indigo 454", "minior-orange 454", "minior-red 454",
            "minior-violet 454", "minior-yellow 454", "axew 453", "bergmite 453", "noctowl 452", "wormadam-plant 452",
            "mienshao 451", "scolipede 451", "vullaby 451", "fletchinder 450", "timburr 449", "beldum 447",
            "brionne 447", "castform-snowy 447", "raticate-totem-alola 447", "shiinotic 447", "ambipom 446",
            "dugtrio-alola 446", "emolga 446", "gothitelle 445", "murkrow 445", "oricorio-pau 445",
            "raticate-alola 445", "whimsicott 445", "raichu-alola 444", "stufful 444", "basculin-blue-striped 443",
            "basculin-red-striped 443", "monferno 440", "beedrill-mega 437", "roserade 436", "pancham 435",
            "shieldon 435", "beedrill 433", "lampent 433", "vigoroth 431", "castform-sunny 429", "maractus 429",
            "trumbeak 429", "electabuzz 428", "machop 427", "sunflora 426", "hippopotas 425", "pheromosa 425",
            "bellsprout 424", "xatu 424", "beautifly 423", "castform-rainy 422", "prinplup 422", "swadloon 421",
            "corphish 420", "krokorok 420", "nuzleaf 420", "primeape 420", "raichu 419", "gengar 417", "rowlet 415",
            "audino 413", "cubchoo 413", "hitmonlee 413", "paras 412", "sigilyph 412", "kricketune 411",
            "masquerain 410", "simisage 410", "drifloon 409", "ivysaur 409", "lumineon 409", "poipole 406",
            "torracat 404", "dedenne 403", "deoxys-speed 403", "herdier 403", "sandshrew 403", "deino 402",
            "vanillish 402", "cinccino 401", "salazzle-totem 399", "serperior 399", "watchog 399", "manectric 398",
            "medicham 398", "salazzle 398", "carvanha 397", "foongus 391", "furfrou 390", "sneasel 390", "lopunny 387",
            "quilladin 387", "wartortle 387", "stunky 385", "loudred 383", "teddiursa 383", "furret 382", "togetic 382",
            "frillish 377", "blissey 375", "venomoth 375", "magnemite 374", "ponyta 374", "seadra 373",
            "deoxys-normal 372", "flaaffy 372", "swellow 372", "growlithe 371", "jumpluff 371", "diggersby 370",
            "jolteon 369", "volbeat 369", "clamperl 366", "nosepass 366", "chimecho 365", "sceptile 365", "liepard 364",
            "staravia 363", "bagon 362", "koffing 362", "phanpy 361", "vibrava 360", "klink 359", "pidgeotto 359",
            "castform 358", "chatot 358", "cryogonal 358", "mareanie 357", "tepig 357", "charmeleon 356", "comfey 356",
            "croagunk 356", "mudkip 356", "nidorina 356", "quilava 355", "heliolisk 353", "spritzee 352",
            "nidorino 351", "braixen 348", "porygon 348", "purugly 347", "totodile 346", "houndour 343", "cacnea 342",
            "ninjask 341", "whirlipede 341", "lickitung 339", "onix 339", "pineco 339", "omanyte 338", "roselia 337",
            "drilbur 336", "sandile 334", "litleo 333", "litwick 331", "doduo 330", "grumpig 330", "tangela 330",
            "turtwig 330", "lilligant 329", "sewaddle 329", "yanma 328", "espeon 327", "oddish 327", "poliwhirl 327",
            "ducklett 326", "misdreavus 325", "rockruff-own-tempo 325", "binacle 324", "crabrawler 324", "rockruff 324",
            "mismagius 318", "venonat 318", "cherrim 316", "shellder 313", "bayleef 311", "makuhita 311", "pidove 311",
            "vivillon 311", "linoone 310", "shuppet 310", "swoobat 310", "dustox 305", "mienfoo 303",
            "ribombee-totem 303", "shinx 303", "ribombee 302", "spinarak 302", "goldeen 301", "lombre 300", "unown 300",
            "skiddo 298", "magby 297", "wooper 297", "meowstic-female 296", "torchic 296", "meowstic-male 295",
            "karrablast 294", "servine 294", "haunter 293", "exeggcute 292", "morelull 292", "raticate 292",
            "swinub 292", "chespin 287", "inkay 286", "bulbasaur 285", "jigglypuff 285", "jynx 284", "chinchou 283",
            "cubone 282", "elgyem 282", "butterfree 280", "spheal 280", "accelgor 279", "illumise 279", "delibird 278",
            "persian-alola 278", "skiploom 276", "electrode 275", "pikipek 275", "shellos 275", "joltik 274",
            "mr-mime 274", "deerling 273", "nincada 269", "clauncher 268", "clefairy 268", "slakoth 268", "litten 267",
            "skorupi 267", "delcatty 266", "swirlix 266", "popplio 264", "chimchar 263", "alakazam-mega 262",
            "pansear 261", "gothorita 259", "pachirisu 259", "persian 258", "oshawott 256", "frogadier 255",
            "barboach 253", "floette 253", "salandit 250", "jangmo-o 249", "grubbin 247", "woobat 247", "snorunt 245",
            "dratini 244", "duosion 244", "piplup 243", "grovyle 242", "gulpin 242", "spinda 242", "trubbish 240",
            "aipom 236", "ledian 233", "seel 233", "wobbuffet 233", "deoxys-attack 231", "mantyke 231", "vanillite 231",
            "starly 230", "spearow 229", "mankey 228", "buizel 227", "ekans 225", "fletchling 225", "nidoran-f 225",
            "riolu 225", "cosmoem 224", "swablu 224", "nidoran-m 223", "chikorita 222", "plusle 222", "squirtle 221",
            "drowzee 220", "zubat 220", "natu 217", "charmander 216", "cyndaquil 215", "elekid 214", "dewpider 213",
            "bronzor 212", "psyduck 212", "shelmet 212", "goomy 210", "buneary 208", "blitzle 206", "fomantis 206",
            "minun 205", "alakazam 204", "pansage 203", "eevee 202", "yungoos 202", "tentacool 200", "dugtrio 199",
            "shroomish 198", "zorua 196", "baltoy 195", "slugma 195", "remoraid 193", "fennekin 192", "gastly 191",
            "espurr 190", "panpour 190", "cutiefly 187", "finneon 186", "duskull 184", "pidgey 184", "hoppip 181",
            "poochyena 181", "venipede 180", "taillow 179", "mareep 178", "yamask 178", "budew 177", "petilil 177",
            "snivy 177", "froakie 174", "cottonee 170", "diglett-alola 170", "whismur 169", "vulpix 168", "cherubi 165",
            "lillipup 165", "tynamo 165", "steenee 159", "patrat 154", "wurmple 153", "flabebe 151", "munna 147",
            "treecko 146", "seedot 145", "tympole 144", "noibat 141", "pikachu-alola-cap 136", "pikachu-hoenn-cap 136",
            "pikachu-kalos-cap 136", "pikachu-original-cap 136", "pikachu-partner-cap 136", "pikachu-sinnoh-cap 136",
            "pikachu-unova-cap 136", "vulpix-alola 136", "bidoof 135", "pikachu-cosplay 135", "ditto 134",
            "hoothoot 133", "purrloin 133", "meditite 130", "pikachu-belle 130", "pikachu-libre 130", "pikachu-phd 130",
            "pikachu-pop-star 130", "pikachu-rock-star 130", "pikachu 129", "combee 128", "rattata-alola 127",
            "electrike 126", "kirlia 125", "lotad 122", "staryu 119", "helioptile 117", "ledyba 117", "skitty 111",
            "spoink 109", "minccino 105", "igglybuff 103", "poliwag 101", "weedle 100", "glameow 99", "horsea 99",
            "bounsweet 97", "solosis 95", "cascoon 94", "silcoon 93", "kakuna 90", "mime-jr 90", "surskit 90",
            "marill 89", "wingull 89", "chansey 88", "luvdisc 85", "togepi 82", "gothita 81", "voltorb 79",
            "sentret 77", "cleffa 76", "scatterbug 75", "smoochum 74", "chingling 72", "meowth-alola 72", "shuckle 71",
            "diglett 69", "rattata 69", "tyrogue 65", "sunkern 62", "burmy 60", "caterpie 52", "ralts 48",
            "kricketot 47", "wynaut 47", "spewpa 46", "kadabra 45", "meowth 45", "wimpod 44", "metapod 42", "pichu 41",
            "azurill 38", "bunnelby 34", "cosmog 30", "zigzagoon 24", "wishiwashi-solo 17", "abra 6", "smeargle 6",
            "feebas 3", "magikarp 1", "happiny 0"]
    for index, pokemon in enumerate(world.get_leader_board()):
        assert pokemon.__repr__() == real[index]

    for filename in glob.glob("./PokeLand*"):
        os.remove(filename)  # blow up all previous files
