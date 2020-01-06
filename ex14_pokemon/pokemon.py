"""Pokemons."""
import json
import requests


class SamePokemonFightException(Exception):
    """Custom exception thrown when same pokemons are fighting."""

    pass



class PokemonFightResultsInATieException(Exception):
    """Custom exception thrown when the fight lasts longer than 100 rounds."""

    pass


class World:
    """World class."""

    fight_matrix = None

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
        self.pokemons = []

        filename = f"{name}_{offset}_{limit}.txt"
        try:
            with open(filename, encoding='utf-8') as file:
                data = file.read()
                for line in data.splitlines():
                    self.pokemons.append(Pokemon(line))
        except FileNotFoundError:
            url = f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}"
            response = requests.get(url)
            loaded_json = response.json()
            for pokemon in loaded_json['results']:
                self.pokemons.append(Pokemon(pokemon['url']))
            self.dump_pokemons_to_file_as_json(filename)

    def dump_pokemons_to_file_as_json(self, name):
        """
        Dump pokemons as json.

        :param name: name of the .txt file
        Write all self.pokemons separated by a newline to the given filename(if it doesnt exist, then create one)
        PS: Write the pokemon.__str__() version, not __repr__() as only name is useless :)
        """
        with open(name, mode='w', encoding='utf-8') as file:
            for pokemon in self.pokemons:
                file.write(pokemon.__str__() + '\n')

    def fight(self):
        """
        Fight.

        A wild brawl between all pokemons where points are assigned to winners
        Note, every pokemon fights another pokemon only once
        Fight lasts until one pokemon runs out of hp.
        every pokemon hits only 1 time per turn and they take turns when they attack.
        Call choose_which_pokemon_hits_first(pokemon1, pokemon2): to determine which pokemon hits first
        Call pokemon_duel function in this method with the aforementioned pokemons.
        every exception thrown by called sub methods must be caught and dealt with.
        """
        for i in range(len(self.pokemons) - 1):
            for j in range(i + 1, len(self.pokemons)):
                try:
                    pok1, pok2 = self.choose_which_pokemon_hits_first(self.pokemons[i], self.pokemons[j])
                    World.pokemon_duel(pok1, pok2)
                except SamePokemonFightException:
                    pass
                except PokemonFightResultsInATieException:
                    pass

    @staticmethod
    def get_fight_matrix():
        """Make fighting matrix."""
        if World.fight_matrix is None:
            World.fight_matrix = {}
            with open('fighting_multipliers.txt') as file:
                table = file.readlines()
                cols = table[0].split()
                for i in range(1, len(table)):
                    row = table[i].split()
                    World.fight_matrix[row[0]] = {}
                    for col in range(1, len(cols)):
                        World.fight_matrix[row[0]][cols[col]] = float(row[col])

        return World.fight_matrix

    @staticmethod
    def pokemon_duel(pokemon1, pokemon2):
        """
        Pokemon duel.

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
        If one pokemon runs out of hp, fight ends abruptly and the winner gets 1 point, (self.score += 1)
        then both pokemons are healed to full hp. (Round rundown: one pokemon hits, second pokemon hits, new round starts)
        """
        hp1 = pokemon1.data['hp']
        hp2 = pokemon2.data['hp']
        multiplier1 = pokemon1.get_attack_multiplier(pokemon2.data['types'])
        multiplier2 = pokemon2.get_attack_multiplier(pokemon1.data['types'])

        for i in range(1, 101):
            total_attack = pokemon1.get_pokemon_attack(i) * multiplier1 - pokemon2.get_pokemon_defense(i)
            if total_attack > 0:
                hp2 -= total_attack
            if hp2 <= 0:
                winner = pokemon1
                break
            total_attack = pokemon2.get_pokemon_attack(i) * multiplier2 - pokemon1.get_pokemon_defense(i)
            if total_attack > 0:
                hp1 -= total_attack
            if hp1 <= 0:
                winner = pokemon2
                break
        else:
            raise PokemonFightResultsInATieException()

        winner.score += 1
        return winner

    @staticmethod
    def choose_which_pokemon_hits_first(pokemon1, pokemon2):
        """
        Which pokemon hits first.

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
        compare = [('speed', True, False), ('weight', False, False), ('height', False, False),
                   ('abilities', True, True), ('moves', True, True), ('base_experience', True, False)]
        for comp in compare:
            pok1, pok2 = World.compare_pokemons(pokemon1, pokemon2, comp[0], comp[1], comp[2])
            if pok1 is not None:
                return pok1, pok2

        raise SamePokemonFightException()

    @staticmethod
    def compare_pokemons(pokemon1, pokemon2, to_compare: str, higher_first: bool, comp_length: bool):
        """Compare pokemons."""
        if comp_length:
            if len(pokemon1.data[to_compare]) > len(pokemon2.data[to_compare]):
                return (pokemon1, pokemon2) if higher_first else (pokemon2, pokemon1)
            elif len(pokemon1.data[to_compare]) < len(pokemon2.data[to_compare]):
                return (pokemon2, pokemon1) if higher_first else (pokemon1, pokemon2)
            else:
                return None, None
        else:
            if pokemon1.data[to_compare] > pokemon2.data[to_compare]:
                return (pokemon1, pokemon2) if higher_first else (pokemon2, pokemon1)
            elif pokemon1.data[to_compare] < pokemon2.data[to_compare]:
                return (pokemon2, pokemon1) if higher_first else (pokemon1, pokemon2)
            else:
                return None, None

    def get_leader_board(self):
        """
        Get Pokemons by given format in a list sorted by the pokemon.score.

        :return: List of leader board. where winners are first
        """
        return sorted(self.pokemons, key=lambda pokemon: (-pokemon.score, pokemon.data['name']), reverse=False)

    def get_pokemons_sorted_by_attribute(self, attribute: str):
        """
        Get Pokemons by given format in a list sorted by the pokemon.data[attribute].

        :param attribute:  pokemon data attribute to sort by
        :return: sorted List of pokemons
        """
        return sorted(self.pokemons, key=lambda pokemon: pokemon.data[attribute])


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

        try:
            self.data = json.loads(url_or_path_name)
        except json.decoder.JSONDecodeError:
            self.parse_json_to_pokemon_information(url_or_path_name)

    def parse_json_to_pokemon_information(self, url):
        """
        Parse js onto pokemon information.

        :param url: url where the information is requested.
        Called from constructor and this method requests data from url to parse it into proper json object
        and then saved under self.data example done previously
        """
        response = requests.get(url)
        loaded_json = response.json()
        self.data["name"] = loaded_json['name']
        self.data["height"] = loaded_json['height']
        self.data["weight"] = loaded_json['weight']
        self.data["base_experience"] = loaded_json['base_experience']

        # speed, attack, defence, special-attack, special-defence, hp
        for stat in loaded_json['stats']:
            self.data[stat['stat']['name']] = stat['base_stat']

        self.data["moves"] = []
        for move in loaded_json['moves']:
            self.data["moves"].append(move['move']['name'])
        self.data["abilities"] = []
        for ability in loaded_json['abilities']:
            self.data["abilities"].append(ability['ability']['name'])
        self.data["types"] = []
        for type in loaded_json['types']:
            self.data["types"].append(type['type']['name'])
        self.data["forms"] = []
        for form in loaded_json['forms']:
            self.data["forms"].append(form['name'])

    def get_attack_multiplier(self, other: list):
        """
        Get attack multiplier.

        self.pokemon is attacking, other is defending
        :param other: list of other pokemon2.data['types']
        Calculate Pokemons attack multiplier against others types and take the best result.
        get the initial multiplier from Fighting Multiplier matrix.
        For example if self.type == ['fire'] and other == ['ground']: return fighting_multipliers.csv.txt['fire']['ground']
        if the defendant has dual types, then multiply the multipliers together.
        if the attacker has dual-types, then the best option is
        chosen(attack can only be of 1 type, choose better[higher multiplier])
        :return: Multiplier.
        """
        multiplier = 0
        fighting_mps = World.get_fight_matrix()
        for attacker in self.data['types']:
            result = 1
            for defender in other:
                result = result * fighting_mps[attacker][defender]
            if result > multiplier:
                multiplier = result
        return multiplier

    def get_pokemon_attack(self, turn_counter):
        """
        Get pokemon attack.

        :param turn_counter: every third round the attack is empowered. (return self.data['special-attack'])
        otherwise basic attack is returned (self.data['attack'])
        """
        return self.data['attack'] if turn_counter % 3 else self.data['special-attack']

    def get_pokemon_defense(self, turn_counter):
        """
        Get Pokemon defence.

        Note: whatever the result is returned, return half of it instead (for example return self.data['defense'] / 2)
        :param turn_counter: every second round the defense is empowered. (return self.data['special-defense'])
        otherwise basic defense is returned (self.data['defense'])
        """
        return (self.data['defense'] / 2) if turn_counter % 2 else (self.data['special-defense'] / 2)

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
        return f"{self.data['name']} {self.score}"


if __name__ == '__main__':
    """
    w = World("Proov2", 0, 100)
    # print(len(w.pokemons), w.pokemons)
    pok1 = Pokemon("https://pokeapi.co/api/v2/pokemon/1/")
    pok2 = Pokemon("https://pokeapi.co/api/v2/pokemon/2/")
    print(pok1)
    print(pok2)
    print(w.choose_which_pokemon_hits_first(pok1, pok2))
    p1, p2 = w.choose_which_pokemon_hits_first(pok1, pok2)
    print(pok1.get_attack_multiplier(["grass", "fairy"]))

    w.pokemon_duel(p1, p1)
    print(pok2.score, pok2.data['hp'])
    print(w.get_leader_board())
    """
    world = World("PokeLand", 15, 20)
    world.fight()
    print(world.get_leader_board())
    # [nidoqueen 17, nidoking 16, arbok 15, fearow 15, sandslash 14, pidgeot 13, raichu 13,
    # sandshrew 13, nidorino 11, nidorina 10, pidgeotto 10, raticate 9, ekans 7, nidoran-m 6,
    # clefairy 5, nidoran-f 5, spearow 5, pidgey 3, pikachu 2, rattata 1]

    world = World("PokeLand", 65, 17)
    world.fight()
    print(world.get_leader_board())
    # [slowbro 16, slowpoke 14, machamp 12, victreebel 12, graveler 10, geodude 9, golem 9, machoke 8, tentacruel 8,
    # weepinbell 8, magneton 7, rapidash 6, machop 5, bellsprout 4, ponyta 3, tentacool 3, magnemite 2]
    """
    for po in world.pokemons:
        print(po)
    """
    world = World("PokeLand", 165, 27)
    world.fight()
    print(world.get_leader_board())
    # [ariados 23, sudowoodo 23, ampharos 22, crobat 21, lanturn 20, flaaffy 19, xatu 19, jumpluff 18, bellossom 16,
    # politoed 15, spinarak 15, sunflora 15, togetic 15, aipom 14, azumarill 13, skiploom 13, mareep 12, natu 12,
    world = World("PokeLand", 15, 4)
    world.fight()
    print(world.get_leader_board())
