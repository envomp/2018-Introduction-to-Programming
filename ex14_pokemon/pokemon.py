"""Pokemon fighting nonsense."""
import os
import requests
import json
from pathlib import Path

fighting_multipliers = {'normal': {'normal': 1.0, 'fighting': 1.0, 'flying': 1.0, 'poison': 1.0, 'ground': 1.0, 'rock': 0.5, 'bug': 1.0, 'ghost': 0.0, 'steel': 0.5, 'fire': 1.0, 'water': 1.0, 'grass': 1.0, 'electric': 1.0, 'psychic': 1.0, 'ice': 1.0, 'dragon': 1.0, 'dark': 1.0, 'fairy': 1.0}, 'fighting': {'normal': 2.0, 'fighting': 1.0, 'flying': 0.5, 'poison': 0.5, 'ground': 1.0, 'rock': 2.0, 'bug': 0.5, 'ghost': 0.0, 'steel': 2.0, 'fire': 1.0, 'water': 1.0, 'grass': 1.0, 'electric': 1.0, 'psychic': 0.5, 'ice': 2.0, 'dragon': 1.0, 'dark': 2.0, 'fairy': 0.5}, 'flying': {'normal': 1.0, 'fighting': 2.0, 'flying': 1.0, 'poison': 1.0, 'ground': 1.0, 'rock': 0.5, 'bug': 2.0, 'ghost': 1.0, 'steel': 0.5, 'fire': 1.0, 'water': 1.0, 'grass': 2.0, 'electric': 0.5, 'psychic': 1.0, 'ice': 1.0, 'dragon': 1.0, 'dark': 1.0, 'fairy': 1.0}, 'poison': {'normal': 1.0, 'fighting': 1.0, 'flying': 1.0, 'poison': 0.5, 'ground': 0.5, 'rock': 0.5, 'bug': 1.0, 'ghost': 0.5, 'steel': 0.0, 'fire': 1.0, 'water': 1.0, 'grass': 2.0, 'electric': 1.0, 'psychic': 1.0, 'ice': 1.0, 'dragon': 1.0, 'dark': 1.0, 'fairy': 2.0}, 'ground': {'normal': 1.0, 'fighting': 1.0, 'flying': 0.0, 'poison': 2.0, 'ground': 1.0, 'rock': 2.0, 'bug': 0.5, 'ghost': 1.0, 'steel': 2.0, 'fire': 2.0, 'water': 1.0, 'grass': 0.5, 'electric': 2.0, 'psychic': 1.0, 'ice': 1.0, 'dragon': 1.0, 'dark': 1.0, 'fairy': 1.0}, 'rock': {'normal': 1.0, 'fighting': 0.5, 'flying': 2.0, 'poison': 1.0, 'ground': 0.5, 'rock': 1.0, 'bug': 2.0, 'ghost': 1.0, 'steel': 0.5, 'fire': 2.0, 'water': 1.0, 'grass': 1.0, 'electric': 1.0, 'psychic': 1.0, 'ice': 2.0, 'dragon': 1.0, 'dark': 1.0, 'fairy': 1.0}, 'bug': {'normal': 1.0, 'fighting': 0.5, 'flying': 0.5, 'poison': 0.5, 'ground': 1.0, 'rock': 1.0, 'bug': 1.0, 'ghost': 0.5, 'steel': 0.5, 'fire': 0.5, 'water': 1.0, 'grass': 2.0, 'electric': 1.0, 'psychic': 2.0, 'ice': 1.0, 'dragon': 1.0, 'dark': 2.0, 'fairy': 0.5}, 'ghost': {'normal': 0.0, 'fighting': 1.0, 'flying': 1.0, 'poison': 1.0, 'ground': 1.0, 'rock': 1.0, 'bug': 1.0, 'ghost': 2.0, 'steel': 1.0, 'fire': 1.0, 'water': 1.0, 'grass': 1.0, 'electric': 1.0, 'psychic': 2.0, 'ice': 1.0, 'dragon': 1.0, 'dark': 0.5, 'fairy': 1.0}, 'steel': {'normal': 1.0, 'fighting': 1.0, 'flying': 1.0, 'poison': 1.0, 'ground': 1.0, 'rock': 2.0, 'bug': 1.0, 'ghost': 1.0, 'steel': 0.5, 'fire': 0.5, 'water': 0.5, 'grass': 1.0, 'electric': 0.5, 'psychic': 1.0, 'ice': 2.0, 'dragon': 1.0, 'dark': 1.0, 'fairy': 2.0}, 'fire': {'normal': 1.0, 'fighting': 1.0, 'flying': 1.0, 'poison': 1.0, 'ground': 1.0, 'rock': 0.5, 'bug': 2.0, 'ghost': 1.0, 'steel': 2.0, 'fire': 0.5, 'water': 0.5, 'grass': 2.0, 'electric': 1.0, 'psychic': 1.0, 'ice': 2.0, 'dragon': 0.5, 'dark': 1.0, 'fairy': 1.0}, 'water': {'normal': 1.0, 'fighting': 1.0, 'flying': 1.0, 'poison': 1.0, 'ground': 2.0, 'rock': 2.0, 'bug': 1.0, 'ghost': 1.0, 'steel': 1.0, 'fire': 2.0, 'water': 0.5, 'grass': 0.5, 'electric': 1.0, 'psychic': 1.0, 'ice': 1.0, 'dragon': 0.5, 'dark': 1.0, 'fairy': 1.0}, 'grass': {'normal': 1.0, 'fighting': 1.0, 'flying': 0.5, 'poison': 0.5, 'ground': 2.0, 'rock': 2.0, 'bug': 0.5, 'ghost': 1.0, 'steel': 0.5, 'fire': 0.5, 'water': 2.0, 'grass': 0.5, 'electric': 1.0, 'psychic': 1.0, 'ice': 1.0, 'dragon': 0.5, 'dark': 1.0, 'fairy': 1.0}, 'electric': {'normal': 1.0, 'fighting': 1.0, 'flying': 2.0, 'poison': 1.0, 'ground': 0.0, 'rock': 1.0, 'bug': 1.0, 'ghost': 1.0, 'steel': 1.0, 'fire': 1.0, 'water': 2.0, 'grass': 0.5, 'electric': 0.5, 'psychic': 1.0, 'ice': 1.0, 'dragon': 0.5, 'dark': 1.0, 'fairy': 1.0}, 'psychic': {'normal': 1.0, 'fighting': 2.0, 'flying': 1.0, 'poison': 2.0, 'ground': 1.0, 'rock': 1.0, 'bug': 1.0, 'ghost': 1.0, 'steel': 0.5, 'fire': 1.0, 'water': 1.0, 'grass': 1.0, 'electric': 1.0, 'psychic': 0.5, 'ice': 1.0, 'dragon': 1.0, 'dark': 0.0, 'fairy': 1.0}, 'ice': {'normal': 1.0, 'fighting': 1.0, 'flying': 2.0, 'poison': 1.0, 'ground': 2.0, 'rock': 1.0, 'bug': 1.0, 'ghost': 1.0, 'steel': 0.5, 'fire': 0.5, 'water': 0.5, 'grass': 2.0, 'electric': 1.0, 'psychic': 1.0, 'ice': 0.5, 'dragon': 2.0, 'dark': 1.0, 'fairy': 1.0}, 'dragon': {'normal': 1.0, 'fighting': 1.0, 'flying': 1.0, 'poison': 1.0, 'ground': 1.0, 'rock': 1.0, 'bug': 1.0, 'ghost': 1.0, 'steel': 0.5, 'fire': 1.0, 'water': 1.0, 'grass': 1.0, 'electric': 1.0, 'psychic': 1.0, 'ice': 1.0, 'dragon': 2.0, 'dark': 1.0, 'fairy': 0.0}, 'dark': {'normal': 1.0, 'fighting': 0.5, 'flying': 1.0, 'poison': 1.0, 'ground': 1.0, 'rock': 1.0, 'bug': 1.0, 'ghost': 2.0, 'steel': 1.0, 'fire': 1.0, 'water': 1.0, 'grass': 1.0, 'electric': 1.0, 'psychic': 2.0, 'ice': 1.0, 'dragon': 1.0, 'dark': 0.5, 'fairy': 0.5}, 'fairy': {'normal': 1.0, 'fighting': 2.0, 'flying': 1.0, 'poison': 0.5, 'ground': 1.0, 'rock': 1.0, 'bug': 1.0, 'ghost': 1.0, 'steel': 0.5, 'fire': 0.5, 'water': 1.0, 'grass': 1.0, 'electric': 1.0, 'psychic': 1.0, 'ice': 1.0, 'dragon': 2.0, 'dark': 2.0, 'fairy': 1.0}}


class World:
    """World class."""

    def __init__(self, name, offset, limit):
        """
        Class constructor.

        :param name: name of the pokemon world
        :param offset: offset for api request
        :param limit: limit for api request
        Check if f"{name}_{offset}_{limit}.txt" file exists, if it does, read pokemons in from that file, if not, then make an api
        request to f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}" to get pokemons and dump them to
        f"{name}_{offset}_{limit}.txt" file
        """
        self.name = name
        self.offset = offset
        self.limit = limit
        self.pokemons = []
        filename = f"{self.name}_{self.offset}_{self.limit}.txt"
        if os.path.isfile(filename):
            file = Path(filename)
            contents = file.read_text()
            for line in contents.splitlines():
                self.pokemons.append(Pokemon(line))
        else:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon?offset={self.offset}&limit={self.limit}")
            rpjson = response.json()
            for p in rpjson['results']:
                self.pokemons.append(Pokemon(p['url']))
            self.dump_pokemons_to_file_as_json(filename)

    def dump_pokemons_to_file_as_json(self, name):
        """
        Dump pokemons to file one by one.

        :param name: name of the .txt file
        Write all self.pokemons separated by a newline to the given filename(if it doesnt exist, then create one)
        PS: Write the pokemon.__str__() version, not __repr__() as only name is useless :)
        """
        writedata = ''
        for p in self.pokemons:
            writedata += "%s\n" % p.__str__()
        f = open(name, "w")
        f.write(writedata)
        f.close()

    def fight(self):
        """
        A wild brawl between all pokemons where points are assigned to winners.

        Note, every pokemon fights another pokemon only once
        Fight lasts until one pokemon runs out of hp.
        every pokemon hits only 1 time per turn and they take turns when they attack.
        Call choose_which_pokemon_hits_first(pokemon1, pokemon2): to determine which pokemon hits first
        Call pokemon_duel function in this method with the aforementioned pokemons.
        every exception thrown by called sub methods must be caught and dealt with.
        """
        already = []
        for p1 in self.pokemons:
            already.append(p1)
            for p2 in self.pokemons:
                if p2 not in already and p2 != p1:
                    try:
                        pp1, pp2 = self.choose_which_pokemon_hits_first(p1, p2)
                        try:
                            self.pokemon_duel(pp1, pp2)
                        except PokemonFightResultsInATieException:
                            pass
                    except SamePokemonFightException:
                        pass

    @staticmethod
    def pokemon_duel(pokemon1, pokemon2):
        """
        Make a duel between two pokemons.

        :param pokemon1: pokemon, who attacks first.
        :param pokemon2: pokemon, who attacks second.
        :return winner: pokemon, who won.

        Here 2 pokemons fight.
        To get the attack and defense of the pokemon, call pokemon1.get_pokemon_attack()
        and pokemon1.get_pokemon_defense() respectively.
        Attack is multiplied by the pokemon1.get_attack_multiplier(list(second.data['types'])) multiplier
        Total attack is
        pokemon1.get_pokemon_attack(turn_counter) * multiplier1 - second.get_pokemon_defense(turn_counter)
        [turn counter starts from 1]
        Total attack is subtracted from other pokemons hp.
        Pokemons can not heal during the fight. (when total attack is negative, no damage is dealt)
        If the fight between 2 pokemons lasts more than 100 turns, then PokemonFightResultsInATieException() is thrown.
        If one pokemon runs out of hp, fight ends and the winner gets 1 point, (self.score += 1)
        then both pokemons are healed to full hp.
        """
        turn_counter = 1
        hp1 = pokemon1.data['hp']
        hp2 = pokemon2.data['hp']
        while turn_counter <= 100:
            total1 = pokemon1.get_pokemon_attack(turn_counter) * pokemon1.get_attack_multiplier(pokemon2.data['types']) - pokemon2.get_pokemon_defense(turn_counter)
            total2 = pokemon2.get_pokemon_attack(turn_counter) * pokemon2.get_attack_multiplier(pokemon1.data['types']) - pokemon1.get_pokemon_defense(turn_counter)
            if total1 < 0:
                total1 = 0
            if total2 < 0:
                total2 = 0
            hp2 = hp2 - total1
            if hp2 <= 0:
                pokemon1.score += 1
                return pokemon1
            hp1 = hp1 - total2
            if hp1 <= 0:
                pokemon2.score += 1
                return pokemon2
            turn_counter += 1
        raise PokemonFightResultsInATieException()

    @staticmethod
    def choose_which_pokemon_hits_first(pokemon1, pokemon2):
        """
        What pokemon should fight first.

        :param pokemon1:
        :param pokemon2:
        Pokemon who's speed is higher, goes first. if both pokemons have the same speed, then pokemon who's weight
        is lower goes first, if both pokemons have same weight, then pokemon who's height is lower goes first,
        if both pokemons have the same height, then the pokemon with more abilities goes first, if they have the same
        amount of abilities, then the pokemon with more moves goes first, if the pokemons have the same amount of
        moves, then the pokemon with higher base_experience goes first, if the pokemons have the same
        base_experience then SamePokemonFightException() is thrown
        :return pokemon1 who goes first and pokemon2 who goes second (return pokemon1, pokemon2)
        """
        compare = [('speed', True), ('weight', False), ('height', False), ('abilities', None), ('moves', None), ('base_experience', True)]
        for c in compare:
            p1, p2 = pokemon1.get_comparison(pokemon2, c)
            if p1 is not None:
                return p1, p2
        raise SamePokemonFightException()

    def get_leader_board(self):
        """
        Get Pokemons by given format in a list sorted by the pokemon.score.

        :return: List of leader board. where winners are first
        """
        maybe = sorted(self.pokemons, key=lambda x: x.data['name'], reverse=False)
        return sorted(maybe, key=lambda x: x.score, reverse=True)

    def get_pokemons_sorted_by_attribute(self, attribute: str):
        """
        Get Pokemons by given format in a list sorted by the pokemon.data[attribute].

        :param attribute:  pokemon data attribute to sort by
        :return: sorted List of pokemons
        """
        return sorted(self.pokemons, key=lambda x: x.data[attribute], reverse=False)


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
        try:
            self.data = json.loads(url_or_path_name)
        except json.decoder.JSONDecodeError:
            self.data = self.parse_json_to_pokemon_information(url_or_path_name)

    def parse_json_to_pokemon_information(self, url):
        """
        Parse json to pokemon.

        :param url: url where the information is requested.
        Called from constructor and this method requests data from url to parse it into proper json object
        and then saved under self.data example done previously
        """
        response = requests.get(url)
        rpjson = response.json()
        data = {}

        data['name'] = rpjson['name']
        for s in rpjson['stats']:
            data[s['stat']['name']] = s['base_stat']
        data['types'] = []
        for x in rpjson['types']:
            data['types'].append(x['type']['name'])
        data['abilities'] = []
        for x in rpjson['abilities']:
            data['abilities'].append(x['ability']['name'])
        data['forms'] = []
        for x in rpjson['forms']:
            data['forms'].append(x['name'])
        data['moves'] = []
        for x in rpjson['moves']:
            data['moves'].append(x['move']['name'])
        data['height'] = rpjson['height']
        data['weight'] = rpjson['weight']
        data['base_experience'] = rpjson['base_experience']
        return data

    def get_comparison(self, other, comp):
        """Universal comparison tool."""
        if comp[1] is True:
            if self.data[comp[0]] > other.data[comp[0]]:
                return self, other
            elif self.data[comp[0]] < other.data[comp[0]]:
                return other, self
            return None, None
        elif comp[1] is False:
            if self.data[comp[0]] < other.data[comp[0]]:
                return self, other
            elif self.data[comp[0]] > other.data[comp[0]]:
                return other, self
        else:
            if len(self.data[comp[0]]) > len(other.data[comp[0]]):
                return self, other
            elif len(self.data[comp[0]]) < len(other.data[comp[0]]):
                return other, self
        return None, None

    def get_attack_multiplier(self, other: list):
        """
        self.pokemon is attacking, other is defending.

        :param other: list of other pokemon2.data['types']
        Calculate Pokemons attack multiplier against others types and take the best result.
        get the initial multiplier from Fighting Multiplier matrix.
        For example if self.type == ['fire'] and other == ['ground']: return fighting_multipliers['fire']['ground']
        if the defendant has dual types, then multiply the multipliers together.
        if the attacker has dual-types, then the best option is
        chosen(attack can only be of 1 type, choose better[higher multiplier])
        :return: Multiplier.
        """
        resmax = 0
        for at in self.data['types']:
            result = 1
            for dt in other:
                result = result * fighting_multipliers[at][dt]
            if resmax < result:
                resmax = result
        return resmax

    def get_pokemon_attack(self, turn_counter):
        """
        Get attack power.

        :param turn_counter: every third round the attack is empowered. (return self.data['special-attack'])
        otherwise basic attack is returned (self.data['attack'])
        """
        if turn_counter % 3 == 0:
            return self.data['special-attack']
        return self.data['attack']

    def get_pokemon_defense(self, turn_counter):
        """
        Note: whatever the result is returned, return half of it instead (for example return self.data['defense'] / 2).

        :param turn_counter: every second round the defense is empowered. (return self.data['special-defense'])
        otherwise basic defense is returned (self.data['defense'])
        """
        if turn_counter % 2 == 0:
            return self.data['special-defense'] / 2
        return self.data['defense'] / 2

    def __str__(self):
        """
        String representation of json(self.data) object.

        One way to accomplish this is to use json.dumps functionality
        :return: string version of json file with necessary information
        """
        return json.dumps(self.data)

    def __repr__(self):
        """
        Object representation.

        :return: Pokemon's name in string format and his score, for example: "garchomp-mega 892"
        """
        return "%s %s" % (self.data['name'], self.score)


class SamePokemonFightException(Exception):
    """Custom exception thrown when same pokemons are fighting."""

    pass


class PokemonFightResultsInATieException(Exception):
    """Custom exception thrown when the fight lasts longer than 100 rounds."""

    pass


if __name__ == '__main__':
    world = World("PokeLand", 15, 20)
    world.fight()
    print(world.get_leader_board())
    print("[nidoqueen 17, nidoking 16, arbok 15, fearow 15, sandslash 14, pidgeot 13, raichu 13, sandshrew 13, nidorino 11, nidorina 10, pidgeotto 10, raticate 9, ekans 7, nidoran-m 6, clefairy 5, nidoran-f 5, spearow 5, pidgey 3, pikachu 2, rattata 1]")
    world = World("PokeLand", 65, 17)
    world.fight()
    print(world.get_leader_board())
    print("[slowbro 16, slowpoke 14, machamp 12, victreebel 12, graveler 10, geodude 9, golem 9, machoke 8, tentacruel 8, weepinbell 8, magneton 7, rapidash 6, machop 5, bellsprout 4, ponyta 3, tentacool 3, magnemite 2]")
    world = World("PokeLand", 165, 27)
    world.fight()
    print(world.get_leader_board())
    print('[ariados 23, sudowoodo 23, ampharos 22, crobat 21, lanturn 20, flaaffy 19, xatu 19, jumpluff 18, bellossom 16, politoed 15, spinarak 15, sunflora 15, togetic 15, aipom 14, azumarill 13, skiploom 13, mareep 12, natu 12, chinchou 10, ledian 9, hoppip 7, togepi 6, cleffa 4, igglybuff 3, pichu 3, sunkern 3, marill 1]')


    print('hi')
    print(fighting_multipliers['bug']['flying'])
    print(fighting_multipliers['flying']['bug'])