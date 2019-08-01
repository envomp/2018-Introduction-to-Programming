import pytest
import random
from ex14_pokemon.pokemon import World
import os
import glob


@pytest.mark.timeout(2.0)
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
def test_correct_pokemon_form_repr_and_str():
    world = World("PokeLand", 0, 1)
    assert world.pokemons[
               0].__str__() == """{"name": "bulbasaur", "speed": 45, "attack": 49, "defense": 49, "special-attack": 65, "special-defense": 65, "hp": 45, "types": ["poison", "grass"], "abilities": ["chlorophyll", "overgrow"], "forms": ["bulbasaur"], "moves": ["razor-wind", "swords-dance", "cut", "bind", "vine-whip", "headbutt", "tackle", "body-slam", "take-down", "double-edge", "growl", "strength", "mega-drain", "leech-seed", "growth", "razor-leaf", "solar-beam", "poison-powder", "sleep-powder", "petal-dance", "string-shot", "toxic", "rage", "mimic", "double-team", "defense-curl", "light-screen", "reflect", "bide", "sludge", "skull-bash", "amnesia", "flash", "rest", "substitute", "snore", "curse", "protect", "sludge-bomb", "mud-slap", "giga-drain", "endure", "charm", "swagger", "fury-cutter", "attract", "sleep-talk", "return", "frustration", "safeguard", "sweet-scent", "synthesis", "hidden-power", "sunny-day", "rock-smash", "facade", "nature-power", "ingrain", "knock-off", "secret-power", "grass-whistle", "bullet-seed", "magical-leaf", "natural-gift", "worry-seed", "seed-bomb", "energy-ball", "leaf-storm", "power-whip", "captivate", "grass-knot", "venoshock", "round", "echoed-voice", "grass-pledge", "work-up", "grassy-terrain", "confide"], "height": 7, "weight": 69, "base_experience": 64}"""
    assert world.pokemons[0].__repr__() == 'bulbasaur 0'


@pytest.mark.timeout(2.0)
@pytest.mark.incgroupdepend("correct")
def test_random_pokemon_correct_form_repr_and_writing_to_file():
    rando = random.randint(0, 900)
    world = World("PokeLand", rando, 1)
    f = open('all_pokemons_0_100000.txt')
    assert f.readlines()[rando] == world.pokemons[0].__str__() + '\n'


@pytest.mark.timeout(60.0)
@pytest.mark.incgroupdepend("correct")
def test_world_fight_between_all_pokemons():
    world = World("all_pokemons", 0, 100000)
    world.fight()
    real = ["zygarde-complete 904", "steelix-mega 894", "garchomp-mega 892", "stakataka 882", "golisopod 882",
            "giratina-origin 880", "rhyperior 876", "zekrom 864", "yveltal 863", "giratina-altered 863",
            "necrozma-dusk 858", "swampert-mega 857", "camerupt-mega 856", "crabominable 856", "dialga 856",
            "scizor-mega 855", "palkia 855", "dhelmise 854", "solgaleo 850", "necrozma-dawn 845", "escavalier 845",
            "celesteela 844", "gyarados 844", "doublade 840", "aegislash-blade 838", "rhydon 837", "guzzlord 836",
            "reshiram 836", "ampharos-mega 832", "gyarados-mega 832", "kyurem-black 832", "metagross 832",
            "xerneas 831", "pangoro 831", "groudon-primal 828", "lunala 828", "tyranitar-mega 827", "mewtwo-mega-x 827",
            "zygarde-50 826", "kyogre-primal 826", "zygarde 825", "garchomp 825", "abomasnow-mega 824", "muk-alola 823",
            "landorus-therian 822", "dragonite 817", "aggron-mega 815", "ho-oh 812", "rayquaza 810", "carracosta 808",
            "bisharp 806", "magearna-original 805", "magearna 805", "regigigas 805", "slaking 805",
            "metagross-mega 804", "kyurem-white 804", "heracross-mega 803", "kyurem 803", "hoopa-unbound 799",
            "rayquaza-mega 798", "armaldo 798", "swampert 797", "scizor 797", "wishiwashi-school 795", "honchkrow 795",
            "charizard-mega-x 794", "bewear 792", "slowbro-mega 788", "salamence-mega 784", "altaria-mega 784",
            "golem-alola 783", "mamoswine 782", "gigalith 781", "landorus-incarnate 779", "tyranitar 778",
            "steelix 778", "volcanion 777", "druddigon 777", "aggron 776", "mawile-mega 775", "ferrothorn 775",
            "kartana 774", "salamence 774", "golem 774", "tyrantrum 772", "golurk 772", "emboar 772", "excadrill 770",
            "arceus 765", "mewtwo-mega-y 764", "cradily 764", "genesect 763", "empoleon 763", "buzzwole 762",
            "magnezone 762", "trevenant 760", "gourgeist-super 757", "bronzong 757", "crustle 756",
            "exeggutor-alola 755", "incineroar 755", "piloswine 755", "granbull 755", "kingdra 754", "sableye-mega 753",
            "rampardos 753", "lapras 753", "braviary 752", "crawdaunt 749", "hoopa 747", "kommo-o-totem 746",
            "necrozma-ultra 745", "zapdos 745", "kommo-o 744", "turtonator 743", "haxorus 743", "blastoise-mega 742",
            "spiritomb 741", "jirachi 739", "kyogre 739", "toucannon 736", "tapu-bulu 735", "snorlax 733",
            "kangaskhan-mega 732", "diancie 729", "forretress 728", "gastrodon 727", "walrein 727", "ursaring 726",
            "seismitoad 725", "skarmory 725", "beartic 724", "avalugg 722", "cobalion 722", "eelektross 721",
            "torterra 721", "slowking 721", "venusaur-mega 720", "vikavolt-totem 719", "audino-mega 719",
            "necrozma 717", "vikavolt 717", "groudon 717", "thundurus-incarnate 716", "marshadow 715",
            "gallade-mega 714", "tapu-fini 714", "lugia 712", "slowbro 712", "lucario-mega 711", "gliscor 711",
            "primarina 710", "relicanth 708", "camerupt 707", "decidueye 706", "latios-mega 705", "articuno 705",
            "thundurus-therian 704", "conkeldurr 704", "gallade 704", "mewtwo 704", "gourgeist-large 702",
            "cloyster 702", "moltres 701", "banette-mega 700", "goodra 700", "barbaracle 698", "hydreigon 698",
            "luxray 698", "mudsdale 697", "scrafty 696", "sandslash-alola 694", "latias-mega 694", "skuntank 694",
            "meloetta-pirouette 693", "meloetta-aria 692", "tapu-koko 691", "manaphy 690", "regirock 690",
            "pinsir-mega 689", "kingler 687", "poliwrath 687", "palossand 686", "toxapex 685", "heatran 683",
            "aurorus 682", "mesprit 682", "klefki 681", "drapion 681", "fraxure 680", "lairon 680", "graveler 680",
            "feraligatr 679", "mew 679", "durant 678", "krookodile 678", "victini 677", "quagsire 676", "magneton 675",
            "blaziken 673", "cacturne 672", "togedemaru-totem 671", "honedge 671", "abomasnow 671", "exeggutor 671",
            "togedemaru 670", "dragalge 670", "samurott 669", "kabutops 669", "stunfisk 667", "hippowdon 667",
            "mawile 667", "donphan 667", "bouffalant 666", "whiscash 666", "blaziken-mega 665", "jellicent 665",
            "drifblim 665", "lucario 664", "graveler-alola 663", "charjabug 662", "dusknoir 662", "nidoqueen 661",
            "charizard-mega-y 660", "staraptor 660", "suicune 660", "muk 660", "registeel 658", "qwilfish 658",
            "unfezant 657", "heracross 657", "drampa 656", "chesnaught 656", "flygon 656", "type-null 655",
            "gourgeist-average 654", "electivire 654", "octillery 654", "ampharos 654", "rhyhorn 654", "amoonguss 653",
            "machamp 653", "zeraora 652", "marowak-totem 651", "aerodactyl-mega 651", "aromatisse 650",
            "marowak-alola 649", "wormadam-trash 648", "aegislash-shield 648", "absol 648", "hariyama 648",
            "malamar 647", "reuniclus 647", "huntail 644", "araquanid-totem 643", "wailord 643", "araquanid 642",
            "rotom-fan 641", "lickilicky 641", "vespiquen 641", "terrakion 639", "darmanitan-zen 638", "boldore 638",
            "entei 637", "nidoking 637", "tornadus-incarnate 636", "probopass 636", "mandibuzz 635", "toxicroak 634",
            "darmanitan-standard 633", "sharpedo-mega 630", "pignite 629", "stoutland 628", "metang 628",
            "cresselia 627", "victreebel 627", "sylveon 625", "solrock 625", "vaporeon 623", "archeops 621",
            "wormadam-sandy 620", "klinklang 620", "celebi 620", "xurkitree 618", "geodude 618", "silvally 617",
            "sudowoodo 616", "wigglytuff 615", "gumshoos-totem 614", "zweilous 613", "bastiodon 612", "passimian 610",
            "gumshoos 610", "latios 610", "musharna 609", "shelgon 609", "vileplume 608", "blastoise 608",
            "lycanroc-midnight 607", "tirtouga 607", "breloom 607", "glalie-mega 606", "flareon 606", "clefable 606",
            "charizard 606", "beheeyem 605", "greninja-ash 604", "lopunny-mega 603", "cranidos 603", "omastar 603",
            "diancie-mega 601", "latias 600", "banette 600", "swanna 599", "torkoal 598", "tentacruel 598",
            "shaymin-sky 597", "komala 597", "raikou 597", "marshtomp 596", "dewgong 594", "houndoom-mega 592",
            "tyrunt 592", "cofagrigus 592", "throh 592", "uxie 592", "rotom-wash 590", "porygon2 590",
            "gourgeist-small 589", "rotom-heat 589", "slurpuff 589", "arcanine 587", "tapu-lele 586", "bruxish 586",
            "mimikyu-totem-disguised 585", "keldeo-resolute 585", "keldeo-ordinary 585", "azelf 585", "togekiss 585",
            "gorebyss 585", "tropius 585", "gligar 585", "mimikyu-totem-busted 584", "clawitzer 584",
            "mimikyu-busted 583", "oricorio-pom-pom 583", "absol-mega 583", "archen 583", "mimikyu-disguised 582",
            "pawniard 582", "altaria 581", "oranguru 580", "rotom-frost 579", "deoxys-defense 578", "pupitar 578",
            "tornadus-therian 577", "tsareena 576", "lanturn 576", "geodude-alola 575", "venusaur 575", "klang 574",
            "aerodactyl 574", "politoed 570", "heatmor 569", "vanilluxe 568", "tangrowth 568", "milotic 568",
            "shiftry 568", "pinsir 568", "sharpedo 567", "weezing 567", "medicham-mega 566", "glaceon 566", "aron 566",
            "umbreon 566", "infernape 564", "crobat 564", "sealeo 563", "sandshrew-alola 562", "dartrix 562",
            "darkrai 562", "gurdurr 561", "exploud 561", "parasect 560", "gabite 559", "hawlucha 558", "chandelure 558",
            "garbodor 558", "grimer-alola 557", "pidgeot-mega 557", "minior-violet-meteor 556",
            "minior-indigo-meteor 556", "minior-blue-meteor 556", "minior-green-meteor 556", "minior-yellow-meteor 556",
            "minior-orange-meteor 556", "minior-red-meteor 556", "florges 556", "pelipper 556", "sawk 555",
            "gardevoir 555", "blacephalon 553", "zangoose 552", "ariados 552", "magcargo 550", "houndoom 549",
            "scyther 549", "weavile 548", "combusken 548", "hakamo-o 547", "magmortar 547", "ludicolo 545",
            "seaking 545", "shaymin-land 544", "gardevoir-mega 543", "noivern 542", "virizion 542", "regice 542",
            "eelektrik 541", "froslass 541", "golduck 541", "naganadel 540", "kangaskhan 539", "gogoat 538",
            "greninja-battle-bond 537", "rotom-mow 537", "nihilego 537", "golett 537", "carbink 536", "greninja 536",
            "seviper 536", "lurantis-totem 533", "talonflame 533", "lurantis 532", "floatzel 532", "bibarel 532",
            "delphox 529", "yanmega 529", "dusclops 527", "alomomola 526", "leafeon 526", "pumpkaboo-super 524",
            "zebstrika 524", "sableye 523", "lycanroc-dusk 522", "oricorio-sensu 522", "phione 522", "zygarde-10 521",
            "sandslash 521", "mothim 520", "volcarona 519", "claydol 519", "manectric-mega 518", "typhlosion 518",
            "machoke 518", "lycanroc-midday 517", "dodrio 517", "weepinbell 517", "swalot 516", "floette-eternal 515",
            "sawsbuck 515", "corsola 515", "galvantula 513", "glalie 513", "pidgeot 513", "golbat 512",
            "oricorio-baile 511", "ninetales-alola 510", "simipour 510", "scraggy 509", "pumpkaboo-large 507",
            "azumarill 507", "tauros 507", "slowpoke 507", "munchlax 506", "sceptile-mega 505", "ferroseed 504",
            "rotom 504", "mudbray 503", "sliggoo 503", "mantine 503", "leavanny 502", "phantump 499", "gothitelle 498",
            "bonsly 498", "simisear 496", "dragonair 496", "hypno 495", "carnivine 494", "mightyena 494", "arbok 494",
            "starmie 491", "pumpkaboo-average 490", "larvesta 489", "kabuto 489", "pyroar 488", "trapinch 486",
            "noctowl 486", "amaura 483", "lileep 483", "bellossom 482", "rapidash 482", "ninetales 481",
            "shiinotic 480", "scolipede 480", "anorith 480", "gloom 480", "dwebble 479", "snover 478", "skrelp 477",
            "lunatone 476", "magmar 476", "farfetchd 476", "marowak 475", "gengar-mega 474", "porygon-z 474",
            "croconaw 474", "pyukumuku 473", "krabby 473", "sigilyph 472", "girafarig 471", "pumpkaboo-small 470",
            "zoroark 470", "wormadam-plant 470", "emolga 469", "brionne 465", "whimsicott 465", "shedinja 465",
            "rufflet 462", "palpitoad 462", "fearow 462", "numel 460", "meganium 460", "oricorio-pau 459", "dewott 459",
            "kecleon 459", "stantler 459", "larvitar 458", "dugtrio-alola 456", "darumaka 456", "miltank 456",
            "hitmontop 455", "lampent 454", "shieldon 454", "grotle 454", "minior-violet 453", "minior-indigo 453",
            "minior-blue 453", "minior-green 453", "minior-yellow 453", "minior-orange 453", "minior-red 453",
            "beldum 452", "castform-snowy 450", "sandygast 450", "ambipom 449", "wailmer 449", "mienshao 448",
            "basculin-blue-striped 447", "basculin-red-striped 447", "roggenrola 447", "roserade 447", "electabuzz 446",
            "fletchinder 445", "masquerain 444", "hitmonchan 444", "raichu-alola 443", "castform-sunny 442",
            "vullaby 442", "monferno 442", "xatu 440", "deoxys-speed 439", "dedenne 439", "sunflora 439", "murkrow 438",
            "prinplup 437", "luxio 436", "chimecho 436", "gible 435", "beedrill-mega 434", "castform-rainy 434",
            "swadloon 433", "tranquill 433", "gengar 432", "raichu 432", "beautifly 431", "beedrill 431",
            "pheromosa 429", "ivysaur 429", "lumineon 427", "magnemite 426", "maractus 424", "medicham 421",
            "salazzle-totem 419", "dunsparce 419", "stufful 418", "salazzle 418", "manectric 418", "audino 416",
            "primeape 416", "raticate-totem-alola 415", "raticate-alola 414", "simisage 414", "vanillish 411",
            "nuzleaf 411", "bergmite 410", "cinccino 410", "serperior 410", "bellsprout 408", "krokorok 407",
            "togetic 407", "trumbeak 406", "pancham 406", "paras 406", "sneasel 405", "seadra 405", "grimer 404",
            "snubbull 402", "wartortle 402", "rowlet 400", "axew 400", "hitmonlee 400", "torracat 399", "poipole 394",
            "cubchoo 394", "corphish 392", "drifloon 391", "quilladin 389", "deino 389", "timburr 388", "frillish 387",
            "venomoth 387", "litwick 385", "diggersby 383", "kricketune 383", "carvanha 383", "porygon 383",
            "foongus 382", "watchog 382", "jolteon 382", "machop 382", "nosepass 381", "flaaffy 381", "hippopotas 380",
            "swellow 380", "ponyta 380", "jumpluff 378", "deoxys-normal 376", "vigoroth 375", "omanyte 373",
            "braixen 372", "clamperl 372", "liepard 371", "sceptile 371", "comfey 370", "lopunny 370", "chatot 369",
            "stunky 367", "grumpig 366", "charmeleon 366", "heliolisk 365", "quilava 365", "onix 365", "sandshrew 365",
            "furfrou 364", "lilligant 363", "vibrava 363", "growlithe 362", "klink 360", "mareanie 358",
            "cryogonal 357", "tangela 357", "whirlipede 355", "espeon 355", "castform 354", "roselia 353", "litleo 352",
            "volbeat 352", "houndour 352", "lickitung 352", "croagunk 351", "staravia 351", "duosion 347",
            "ninjask 347", "koffing 346", "oddish 346", "spritzee 345", "tepig 345", "misdreavus 345", "pidgeotto 345",
            "nidorino 344", "cherrim 342", "nidorina 342", "mudkip 340", "meowstic-female 336", "meowstic-male 336",
            "vivillon 334", "yanma 333", "sandile 332", "doduo 332", "herdier 331", "loudred 331", "cacnea 330",
            "purugly 329", "furret 329", "ribombee-totem 326", "swoobat 326", "ribombee 325", "blissey 325",
            "bayleef 325", "sewaddle 324", "drilbur 322", "binacle 321", "mismagius 321", "crabrawler 320",
            "phanpy 320", "ducklett 319", "totodile 319", "morelull 317", "butterfree 316", "rockruff-own-tempo 314",
            "exeggcute 314", "rockruff 313", "poliwhirl 313", "teddiursa 312", "persian-alola 310", "bagon 310",
            "electrode 310", "dustox 308", "lombre 307", "turtwig 305", "torchic 304", "haunter 303", "bulbasaur 302",
            "servine 301", "venonat 301", "elgyem 297", "gothorita 297", "mienfoo 296", "accelgor 296", "shellder 296",
            "linoone 295", "shuppet 294", "magby 294", "raticate 294", "illumise 293", "pineco 292", "goldeen 292",
            "skiddo 291", "spinarak 290", "karrablast 289", "chinchou 288", "delibird 287", "shinx 286", "unown 286",
            "joltik 282", "deerling 280", "alakazam-mega 277", "skiploom 277", "jynx 277", "swirlix 274", "chespin 274",
            "pikipek 273", "pidove 273", "skorupi 273", "swinub 273", "pansear 272", "persian 272", "frogadier 271",
            "popplio 270", "litten 270", "chimchar 270", "clefairy 270", "spheal 267", "mr-mime 266", "floette 265",
            "delcatty 265", "clauncher 264", "shellos 264", "makuhita 259", "pachirisu 257", "cubone 256",
            "oshawott 255", "inkay 254", "nincada 250", "spinda 249", "snorunt 248", "salandit 247", "jangmo-o 245",
            "barboach 245", "woobat 242", "piplup 242", "grubbin 241", "vanillite 241", "grovyle 240", "plusle 238",
            "gulpin 235", "wooper 235", "dratini 235", "trubbish 233", "charmander 231", "cyndaquil 230", "seel 229",
            "mankey 229", "aipom 228", "mantyke 227", "jigglypuff 227", "deoxys-attack 225", "chikorita 223",
            "ekans 223", "shelmet 222", "wobbuffet 222", "squirtle 222", "riolu 221", "espurr 220", "buizel 220",
            "natu 220", "psyduck 220", "spearow 219", "cosmoem 217", "elekid 217", "nidoran-m 217", "yamask 216",
            "swablu 216", "dewpider 215", "ledian 212", "fletchling 211", "minun 209", "pansage 208", "starly 207",
            "nidoran-f 206", "gastly 205", "drowzee 204", "shroomish 203", "blitzle 202", "zorua 201", "panpour 201",
            "dugtrio 201", "baltoy 200", "zubat 200", "fomantis 199", "fennekin 199", "buneary 199", "petilil 196",
            "cottonee 196", "bronzor 196", "slakoth 196", "goomy 195", "mareep 189", "finneon 187", "remoraid 187",
            "munna 186", "slugma 185", "cherubi 184", "solosis 183", "snivy 183", "budew 180", "froakie 179",
            "alakazam 178", "kirlia 177", "eevee 177", "hoppip 176", "cutiefly 174", "flabebe 173", "venipede 172",
            "tynamo 171", "tentacool 169", "yungoos 168", "duskull 167", "vulpix 167", "taillow 166",
            "diglett-alola 163", "steenee 163", "pidgey 161", "poochyena 155", "treecko 150", "tympole 146",
            "noibat 145", "electrike 144", "meditite 143", "vulpix-alola 142", "pikachu-partner-cap 139",
            "pikachu-alola-cap 139", "pikachu-kalos-cap 139", "pikachu-unova-cap 139", "pikachu-sinnoh-cap 139",
            "pikachu-hoenn-cap 139", "pikachu-original-cap 139", "pikachu-cosplay 138", "lillipup 136", "spoink 136",
            "staryu 136", "pikachu-libre 133", "pikachu-phd 133", "pikachu-pop-star 133", "pikachu-belle 133",
            "pikachu-rock-star 133", "pikachu 132", "seedot 131", "rattata-alola 129", "ditto 128", "helioptile 127",
            "hoothoot 125", "gothita 123", "patrat 121", "combee 120", "lotad 120", "purrloin 117", "chingling 113",
            "whismur 110", "bidoof 106", "wurmple 104", "ledyba 104", "horsea 102", "poliwag 102", "wingull 101",
            "glameow 100", "bounsweet 98", "minccino 98", "weedle 93", "surskit 91", "togepi 90", "voltorb 90",
            "luvdisc 88", "igglybuff 87", "cascoon 86", "mime-jr 85", "silcoon 85", "kakuna 85", "cleffa 83",
            "skitty 78", "marill 76", "smoochum 75", "meowth-alola 74", "diglett 67", "rattata 65", "burmy 63",
            "sunkern 62", "scatterbug 60", "ralts 57", "tyrogue 57", "sentret 57", "shuckle 54", "spewpa 51",
            "wimpod 50", "wynaut 47", "kadabra 46", "kricketot 44", "chansey 44", "meowth 44", "caterpie 44",
            "pichu 41", "metapod 40", "bunnelby 29", "azurill 29", "cosmog 27", "zigzagoon 23", "wishiwashi-solo 17",
            "smeargle 7", "abra 7", "feebas 3", "magikarp 2", "happiny 0"]
    index = 0
    for pokemon in world.get_leader_board():
        assert pokemon.__repr__() == real[index]
        index += 1
