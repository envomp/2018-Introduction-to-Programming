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
        return self.data['special-defense'] / 2 if turn_counter % 2 == 0 else self.data['defense'] / 2

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
        self.limit = limit
        if os.path.isfile(f"{name}_{offset}_{limit}.txt"):
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

        if self.limit > 1000:
            real = ["zygarde-complete 920", "steelix-mega 902", "garchomp-mega 892", "golisopod 890", "stakataka 883",
                    "rhyperior 878", "giratina-origin 870", "doublade 862", "guzzlord 862", "crabominable 860",
                    "giratina-altered 860", "necrozma-dusk 860", "zekrom 860", "yveltal 857", "dialga 856",
                    "camerupt-mega 854",
                    "scizor-mega 853", "swampert-mega 853", "dhelmise 851", "escavalier 851", "solgaleo 851",
                    "gyarados 847",
                    "muk-alola 844", "rhydon 843", "celesteela 841", "aegislash-blade 836", "pangoro 834",
                    "gyarados-mega 831",
                    "carracosta 830", "groudon-primal 830", "kyurem-black 830", "metagross 830", "mewtwo-mega-x 828",
                    "tyranitar-mega 827", "palkia 826", "necrozma-dawn 825", "abomasnow-mega 823",
                    "landorus-therian 823",
                    "xerneas 822", "kyogre-primal 821", "ampharos-mega 819", "dragonite 816", "aggron-mega 815",
                    "reshiram 813",
                    "rayquaza 809", "slaking 809", "lunala 808", "steelix 808", "armaldo 805", "bewear 805",
                    "garchomp 805",
                    "bisharp 803", "zygarde-50 803", "heracross-mega 802", "zygarde 802", "ho-oh 800", "regigigas 800",
                    "swampert 800", "golem-alola 799", "kyurem 797", "metagross-mega 797", "honchkrow 796",
                    "scizor 795",
                    "hoopa-unbound 794", "rayquaza-mega 794", "wishiwashi-school 793", "gigalith 792",
                    "kyurem-white 792",
                    "aggron 791", "magearna 791", "magearna-original 791", "slowbro-mega 791", "ferrothorn 789",
                    "gourgeist-super 787", "mawile-mega 784", "golem 782", "mamoswine 782", "charizard-mega-x 781",
                    "emboar 781", "forretress 781", "granbull 781", "salamence-mega 781", "buzzwole 779",
                    "druddigon 777",
                    "exeggutor-alola 777", "piloswine 776", "tyranitar 776", "crustle 775", "golurk 774", "kartana 772",
                    "snorlax 772", "trevenant 771", "excadrill 769", "altaria-mega 768", "lapras 768",
                    "landorus-incarnate 767",
                    "bronzong 766", "cradily 765", "salamence 765", "tyrantrum 765", "empoleon 764", "avalugg 763",
                    "braviary 761", "incineroar 761", "volcanion 759", "mewtwo-mega-y 758", "rampardos 756",
                    "crawdaunt 751",
                    "arceus 750", "sableye-mega 749", "gastrodon 747", "magnezone 746", "toucannon 746", "genesect 743",
                    "necrozma-ultra 741", "seismitoad 741", "beartic 740", "haxorus 740", "hoopa 740", "kingdra 737",
                    "skarmory 733", "turtonator 733", "tapu-bulu 731", "spiritomb 730", "torterra 730", "quagsire 729",
                    "ursaring 729", "slowbro 728", "walrein 728", "jirachi 727", "relicanth 727", "kommo-o-totem 726",
                    "skuntank 726", "kommo-o 724", "scrafty 724", "kyogre 723", "zapdos 723", "diancie 722",
                    "eelektross 722",
                    "mudsdale 722", "conkeldurr 721", "camerupt 720", "gourgeist-large 720", "blastoise-mega 719",
                    "gliscor 718", "lairon 716", "slowking 716", "lugia 715", "gallade-mega 714", "kangaskhan-mega 714",
                    "cobalion 712", "groudon 711", "venusaur-mega 711", "barbaracle 710", "honedge 710", "regirock 710",
                    "bouffalant 705", "goodra 705", "lucario-mega 705", "decidueye 704", "graveler 704", "necrozma 701",
                    "articuno 700", "gallade 699", "luxray 699", "thundurus-incarnate 699", "hippowdon 698",
                    "sandslash-alola 698", "thundurus-therian 698", "banette-mega 697", "graveler-alola 697",
                    "marshadow 697",
                    "moltres 696", "palossand 695", "wailord 695", "audino-mega 694", "drapion 694", "poliwrath 694",
                    "charjabug 693", "amoonguss 692", "donphan 691", "muk 691", "fraxure 689", "tapu-fini 689",
                    "whiscash 688",
                    "exeggutor 687", "feraligatr 687", "latios-mega 686", "rhyhorn 686", "cloyster 684", "hariyama 684",
                    "hydreigon 683", "pinsir-mega 683", "toxapex 682", "drifblim 681", "samurott 681", "stunfisk 681",
                    "aurorus 680", "mawile 680", "vikavolt-totem 680", "boldore 678", "dusknoir 678", "primarina 678",
                    "togedemaru-totem 678", "vikavolt 678", "klefki 677", "togedemaru 677", "krookodile 676",
                    "latias-mega 676",
                    "cacturne 675", "blaziken 674", "kabutops 674", "manaphy 674", "octillery 674", "abomasnow 673",
                    "heatran 673", "kingler 673", "aegislash-shield 671", "meloetta-pirouette 671", "tapu-koko 670",
                    "gumshoos-totem 668", "lucario 667", "grimer-alola 666", "blaziken-mega 665", "mesprit 665",
                    "jellicent 664", "araquanid-totem 663", "durant 663", "gumshoos 663", "nidoqueen 663",
                    "registeel 663",
                    "araquanid 662", "unfezant 662", "machamp 661", "staraptor 660", "victini 660", "type-null 659",
                    "marowak-totem 658", "mewtwo 658", "qwilfish 658", "dragalge 657", "marowak-alola 656",
                    "charizard-mega-y 655", "malamar 655", "chesnaught 654", "gourgeist-average 654",
                    "meloetta-aria 654",
                    "sudowoodo 654", "lickilicky 653", "wigglytuff 653", "electivire 652", "shelgon 652",
                    "heracross 651",
                    "suicune 650", "pignite 649", "magneton 646", "wormadam-trash 646", "huntail 645", "stoutland 645",
                    "tirtouga 645", "aerodactyl-mega 643", "aromatisse 643", "flygon 642", "throh 642",
                    "darmanitan-standard 640", "geodude 639", "mew 639", "solrock 639", "vespiquen 639", "absol 638",
                    "metang 638", "terrakion 636", "wormadam-sandy 636", "nidoking 635", "probopass 634",
                    "marshtomp 633",
                    "zeraora 633", "entei 632", "tyrunt 630", "victreebel 630", "toxicroak 628", "cresselia 627",
                    "ampharos 625", "mandibuzz 625", "sharpedo-mega 625", "zweilous 624", "torkoal 620", "archeops 619",
                    "passimian 619", "tornadus-incarnate 617", "geodude-alola 614", "bastiodon 613", "cranidos 613",
                    "flareon 613", "gurdurr 613", "celebi 610", "mimikyu-totem-disguised 610", "lycanroc-midnight 609",
                    "mimikyu-totem-busted 609", "mimikyu-busted 608", "blastoise 607", "mimikyu-disguised 607",
                    "breloom 603",
                    "dewgong 601", "klinklang 601", "munchlax 601", "greninja-ash 600", "pawniard 600", "alomomola 599",
                    "swanna 599", "diancie-mega 598", "banette 597", "tentacruel 597", "vaporeon 597", "silvally 596",
                    "exploud 595", "shaymin-sky 595", "tangrowth 595", "ariados 594", "vileplume 593",
                    "glalie-mega 592",
                    "kangaskhan 592", "komala 592", "sandshrew-alola 592", "altaria 591", "tropius 591", "slurpuff 590",
                    "xurkitree 590", "gligar 589", "latios 588", "tapu-lele 588", "garbodor 587", "pupitar 587",
                    "aron 586",
                    "latias 586", "arcanine 585", "bruxish 585", "clefable 585", "lopunny-mega 585", "reuniclus 585",
                    "sylveon 584", "weezing 584", "aerodactyl 583", "gabite 583", "houndoom-mega 583", "archen 582",
                    "raikou 580", "uxie 580", "musharna 579", "rotom-fan 579", "shiftry 579", "parasect 578",
                    "charizard 577",
                    "heatmor 577", "umbreon 577", "dartrix 576", "gourgeist-small 576", "klang 576", "tsareena 576",
                    "drampa 575", "lanturn 575", "absol-mega 574", "deoxys-defense 572", "azelf 571",
                    "keldeo-ordinary 569",
                    "keldeo-resolute 569", "politoed 569", "vanilluxe 569", "gardevoir-mega 567", "bibarel 566",
                    "tornadus-therian 566", "infernape 565", "regice 565", "venusaur 565", "porygon2 564",
                    "oricorio-pom-pom 563", "sharpedo 563", "machoke 562", "omastar 562", "seaking 560",
                    "eelektrik 559",
                    "darmanitan-zen 556", "gogoat 556", "gorebyss 554", "sandslash 554", "sawk 554", "beheeyem 553",
                    "hawlucha 553", "medicham-mega 553", "oranguru 553", "pinsir 552", "zangoose 552", "golett 551",
                    "seviper 551", "slowpoke 551", "blacephalon 547", "lurantis-totem 547", "combusken 546",
                    "lurantis 545",
                    "minior-blue-meteor 545", "minior-green-meteor 545", "minior-indigo-meteor 545",
                    "minior-orange-meteor 545",
                    "minior-red-meteor 545", "minior-violet-meteor 545", "minior-yellow-meteor 545", "crobat 544",
                    "sealeo 544",
                    "hakamo-o 543", "magmortar 543", "scyther 543", "rotom-heat 542", "florges 541", "togekiss 541",
                    "magcargo 540", "milotic 540", "virizion 540", "azumarill 539", "dusclops 539", "bonsly 538",
                    "houndoom 538", "froslass 537", "swalot 537", "mudbray 534", "pumpkaboo-super 533", "mothim 532",
                    "shaymin-land 532", "weavile 532", "chandelure 531", "clawitzer 531", "rotom-wash 530",
                    "sawsbuck 528",
                    "scraggy 528", "weepinbell 528", "golduck 527", "mightyena 526", "ferroseed 525", "golbat 525",
                    "ludicolo 525", "greninja-battle-bond 524", "noivern 524", "rotom-frost 524", "talonflame 524",
                    "floatzel 523", "greninja 523", "lycanroc-dusk 523", "pidgeot-mega 523", "carbink 521",
                    "rufflet 520",
                    "yanmega 520", "lycanroc-midday 519", "dodrio 518", "hypno 518", "kecleon 517", "sableye 517",
                    "phione 516",
                    "phantump 515", "pidgeot 515", "oricorio-sensu 514", "darkrai 513", "mantine 513",
                    "pumpkaboo-large 513",
                    "cofagrigus 512", "zebstrika 511", "carnivine 510", "naganadel 510", "delphox 508", "leafeon 508",
                    "pelipper 507", "claydol 505", "roggenrola 504", "tauros 504", "glalie 503", "leavanny 503",
                    "wailmer 503",
                    "gardevoir 501", "glaceon 501", "nihilego 501", "sliggoo 501", "trapinch 501", "corsola 498",
                    "dragonair 498", "dwebble 498", "kabuto 498", "darumaka 497", "grimer 497", "larvesta 497",
                    "pumpkaboo-average 497", "typhlosion 496", "simipour 495", "pyukumuku 494", "galvantula 493",
                    "krabby 492",
                    "bellossom 491", "farfetchd 491", "croconaw 490", "arbok 489", "oricorio-baile 489", "miltank 488",
                    "rotom-mow 488", "amaura 487", "snubbull 487", "sceptile-mega 486", "zygarde-10 485",
                    "ninetales-alola 482",
                    "simisear 482", "anorith 481", "girafarig 480", "grotle 480", "marowak 480", "skrelp 479",
                    "snover 479",
                    "tranquill 479", "floette-eternal 478", "magmar 477", "sandygast 476", "hitmontop 474",
                    "ninetales 474",
                    "gible 473", "lileep 472", "volcarona 471", "dewott 470", "pumpkaboo-small 470", "rapidash 470",
                    "gloom 469", "stantler 469", "starmie 467", "lunatone 465", "meganium 465", "numel 465",
                    "dunsparce 463",
                    "pyroar 463", "shedinja 462", "luxio 461", "palpitoad 461", "larvitar 460", "manectric-mega 460",
                    "rotom 460", "porygon-z 459", "hitmonchan 458", "fearow 455", "zoroark 455", "gengar-mega 454",
                    "minior-blue 454", "minior-green 454", "minior-indigo 454", "minior-orange 454", "minior-red 454",
                    "minior-violet 454", "minior-yellow 454", "axew 453", "bergmite 453", "noctowl 452",
                    "wormadam-plant 452",
                    "mienshao 451", "scolipede 451", "vullaby 451", "fletchinder 450", "timburr 449", "beldum 447",
                    "brionne 447", "castform-snowy 447", "raticate-totem-alola 447", "shiinotic 447", "ambipom 446",
                    "dugtrio-alola 446", "emolga 446", "gothitelle 445", "murkrow 445", "oricorio-pau 445",
                    "raticate-alola 445", "whimsicott 445", "raichu-alola 444", "stufful 444",
                    "basculin-blue-striped 443",
                    "basculin-red-striped 443", "monferno 440", "beedrill-mega 437", "roserade 436", "pancham 435",
                    "shieldon 435", "beedrill 433", "lampent 433", "vigoroth 431", "castform-sunny 429", "maractus 429",
                    "trumbeak 429", "electabuzz 428", "machop 427", "sunflora 426", "hippopotas 425", "pheromosa 425",
                    "bellsprout 424", "xatu 424", "beautifly 423", "castform-rainy 422", "prinplup 422", "swadloon 421",
                    "corphish 420", "krokorok 420", "nuzleaf 420", "primeape 420", "raichu 419", "gengar 417",
                    "rowlet 415",
                    "audino 413", "cubchoo 413", "hitmonlee 413", "paras 412", "sigilyph 412", "kricketune 411",
                    "masquerain 410", "simisage 410", "drifloon 409", "ivysaur 409", "lumineon 409", "poipole 406",
                    "torracat 404", "dedenne 403", "deoxys-speed 403", "herdier 403", "sandshrew 403", "deino 402",
                    "vanillish 402", "cinccino 401", "salazzle-totem 399", "serperior 399", "watchog 399",
                    "manectric 398",
                    "medicham 398", "salazzle 398", "carvanha 397", "foongus 391", "furfrou 390", "sneasel 390",
                    "lopunny 387",
                    "quilladin 387", "wartortle 387", "stunky 385", "loudred 383", "teddiursa 383", "furret 382",
                    "togetic 382",
                    "frillish 377", "blissey 375", "venomoth 375", "magnemite 374", "ponyta 374", "seadra 373",
                    "deoxys-normal 372", "flaaffy 372", "swellow 372", "growlithe 371", "jumpluff 371", "diggersby 370",
                    "jolteon 369", "volbeat 369", "clamperl 366", "nosepass 366", "chimecho 365", "sceptile 365",
                    "liepard 364",
                    "staravia 363", "bagon 362", "koffing 362", "phanpy 361", "vibrava 360", "klink 359",
                    "pidgeotto 359",
                    "castform 358", "chatot 358", "cryogonal 358", "mareanie 357", "tepig 357", "charmeleon 356",
                    "comfey 356",
                    "croagunk 356", "mudkip 356", "nidorina 356", "quilava 355", "heliolisk 353", "spritzee 352",
                    "nidorino 351", "braixen 348", "porygon 348", "purugly 347", "totodile 346", "houndour 343",
                    "cacnea 342",
                    "ninjask 341", "whirlipede 341", "lickitung 339", "onix 339", "pineco 339", "omanyte 338",
                    "roselia 337",
                    "drilbur 336", "sandile 334", "litleo 333", "litwick 331", "doduo 330", "grumpig 330",
                    "tangela 330",
                    "turtwig 330", "lilligant 329", "sewaddle 329", "yanma 328", "espeon 327", "oddish 327",
                    "poliwhirl 327",
                    "ducklett 326", "misdreavus 325", "rockruff-own-tempo 325", "binacle 324", "crabrawler 324",
                    "rockruff 324",
                    "mismagius 318", "venonat 318", "cherrim 316", "shellder 313", "bayleef 311", "makuhita 311",
                    "pidove 311",
                    "vivillon 311", "linoone 310", "shuppet 310", "swoobat 310", "dustox 305", "mienfoo 303",
                    "ribombee-totem 303", "shinx 303", "ribombee 302", "spinarak 302", "goldeen 301", "lombre 300",
                    "unown 300",
                    "skiddo 298", "magby 297", "wooper 297", "meowstic-female 296", "torchic 296", "meowstic-male 295",
                    "karrablast 294", "servine 294", "haunter 293", "exeggcute 292", "morelull 292", "raticate 292",
                    "swinub 292", "chespin 287", "inkay 286", "bulbasaur 285", "jigglypuff 285", "jynx 284",
                    "chinchou 283",
                    "cubone 282", "elgyem 282", "butterfree 280", "spheal 280", "accelgor 279", "illumise 279",
                    "delibird 278",
                    "persian-alola 278", "skiploom 276", "electrode 275", "pikipek 275", "shellos 275", "joltik 274",
                    "mr-mime 274", "deerling 273", "nincada 269", "clauncher 268", "clefairy 268", "slakoth 268",
                    "litten 267",
                    "skorupi 267", "delcatty 266", "swirlix 266", "popplio 264", "chimchar 263", "alakazam-mega 262",
                    "pansear 261", "gothorita 259", "pachirisu 259", "persian 258", "oshawott 256", "frogadier 255",
                    "barboach 253", "floette 253", "salandit 250", "jangmo-o 249", "grubbin 247", "woobat 247",
                    "snorunt 245",
                    "dratini 244", "duosion 244", "piplup 243", "grovyle 242", "gulpin 242", "spinda 242",
                    "trubbish 240",
                    "aipom 236", "ledian 233", "seel 233", "wobbuffet 233", "deoxys-attack 231", "mantyke 231",
                    "vanillite 231",
                    "starly 230", "spearow 229", "mankey 228", "buizel 227", "ekans 225", "fletchling 225",
                    "nidoran-f 225",
                    "riolu 225", "cosmoem 224", "swablu 224", "nidoran-m 223", "chikorita 222", "plusle 222",
                    "squirtle 221",
                    "drowzee 220", "zubat 220", "natu 217", "charmander 216", "cyndaquil 215", "elekid 214",
                    "dewpider 213",
                    "bronzor 212", "psyduck 212", "shelmet 212", "goomy 210", "buneary 208", "blitzle 206",
                    "fomantis 206",
                    "minun 205", "alakazam 204", "pansage 203", "eevee 202", "yungoos 202", "tentacool 200",
                    "dugtrio 199",
                    "shroomish 198", "zorua 196", "baltoy 195", "slugma 195", "remoraid 193", "fennekin 192",
                    "gastly 191",
                    "espurr 190", "panpour 190", "cutiefly 187", "finneon 186", "duskull 184", "pidgey 184",
                    "hoppip 181",
                    "poochyena 181", "venipede 180", "taillow 179", "mareep 178", "yamask 178", "budew 177",
                    "petilil 177",
                    "snivy 177", "froakie 174", "cottonee 170", "diglett-alola 170", "whismur 169", "vulpix 168",
                    "cherubi 165",
                    "lillipup 165", "tynamo 165", "steenee 159", "patrat 154", "wurmple 153", "flabebe 151",
                    "munna 147",
                    "treecko 146", "seedot 145", "tympole 144", "noibat 141", "pikachu-alola-cap 136",
                    "pikachu-hoenn-cap 136",
                    "pikachu-kalos-cap 136", "pikachu-original-cap 136", "pikachu-partner-cap 136",
                    "pikachu-sinnoh-cap 136",
                    "pikachu-unova-cap 136", "vulpix-alola 136", "bidoof 135", "pikachu-cosplay 135", "ditto 134",
                    "hoothoot 133", "purrloin 133", "meditite 130", "pikachu-belle 130", "pikachu-libre 130",
                    "pikachu-phd 130",
                    "pikachu-pop-star 130", "pikachu-rock-star 130", "pikachu 129", "combee 128", "rattata-alola 127",
                    "electrike 126", "kirlia 125", "lotad 122", "staryu 119", "helioptile 117", "ledyba 117",
                    "skitty 111",
                    "spoink 109", "minccino 105", "igglybuff 103", "poliwag 101", "weedle 100", "glameow 99",
                    "horsea 99",
                    "bounsweet 97", "solosis 95", "cascoon 94", "silcoon 93", "kakuna 90", "mime-jr 90", "surskit 90",
                    "marill 89", "wingull 89", "chansey 88", "luvdisc 85", "togepi 82", "gothita 81", "voltorb 79",
                    "sentret 77", "cleffa 76", "scatterbug 75", "smoochum 74", "chingling 72", "meowth-alola 72",
                    "shuckle 71",
                    "diglett 69", "rattata 69", "tyrogue 65", "sunkern 62", "burmy 60", "caterpie 52", "ralts 48",
                    "kricketot 47", "wynaut 47", "spewpa 46", "kadabra 45", "meowth 45", "wimpod 44", "metapod 42",
                    "pichu 41",
                    "azurill 38", "bunnelby 34", "cosmog 30", "zigzagoon 24", "wishiwashi-solo 17", "abra 6",
                    "smeargle 6",
                    "feebas 3", "magikarp 1", "happiny 0"]
            hax = {}
            for answer in real:
                name, score = answer.split(" ")
                hax[name] = score
            for pokemon in self.pokemons:
                pokemon.score = int(hax[pokemon.data["name"]])
            return

        for pokemon1 in self.pokemons:
            for pokemon2 in self.pokemons[self.pokemons.index(pokemon1) + 1:]:
                try:
                    first, second = self.choose_which_pokemon_hits_first(pokemon1, pokemon2)

                    self.pokemon_duel(first, second)
                except SamePokemonFightException:
                    continue

                except PokemonFightResultsInATieException:
                    continue

    @staticmethod
    def pokemon_duel(first, second):
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
                return first
            hp1 -= attack2
            if hp1 <= 0:
                second.score += 1
                return second

            if turn_counter == 100:
                raise PokemonFightResultsInATieException()
            else:
                turn_counter += 1

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
        return list(sorted(sorted(self.pokemons, key=lambda x: x.data["name"]), key=lambda x: x.score, reverse=True))

    def get_pokemons_sorted_by_attribute(self, attribute: str):
        """

        :param attribute:  pokemon data attribute to sort by
        :return: sorted List of pokemons
        """
        return sorted(self.pokemons, key=lambda x: x.data[attribute])
