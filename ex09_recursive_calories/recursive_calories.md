# EX09

## Teooria

Enne ülesannete lahendamist oleks mõistlik tutvuga rekursiooniga Pydoc'i osakonnas.

### Abimaterjalid ülesande lahendamiseks

* Rekursioon: https://ained.ttu.ee/pydoc/recursion.html
* Järjend: https://ained.ttu.ee/pydoc/list.html
* Sõne: https://ained.ttu.ee/pydoc/string.html
* Sõnastik: https://ained.ttu.ee/pydoc/dict.html

## Ülesanne

Fail Gitis: ``ex09_recursion/recursive_calories.py``.

### Taust

Oled tudeng ja pead selle ära tegema, et 15p saada.

### Sisu

`def lets_count_calories(salad: float, chocolate_pieces: int, fridge_visits: int) -> int:` Funktsioon saab ette parameetri `salad` - salati koguse (ujukomaarvuna - *float*ina) kilogrammides (salati kogus on alati antud 100g täpsusega ehk üks koht peale koma, näiteks 1.6, aga mitte kunagi 1.62), `chocolate_pieces` - šokolaaditükkide koguse (täisarvuna - *int*ina) ning `fridge_visits` - külmkapi külastuste arvu, see arv inditseerib, mitu korda Sa maksimaalselt külmkapi kallal maiustamas tohid käia. Ülesandeks on lugeda kokku, mitu kalorit külmkapi külastuste ajal kokku tarbitakse. Sada grammi salatit annab 120 kalorit ning tükk šokolaadi 34 kalorit. Sa lähed külmkapist snäkki võtma seni, kuni külmkapi külastused pole otsas ning seal on salatit või šokolaadi. Kui külmkapis on salatit, sööd alati täpselt 100g salatit ära. Kui külmkapis on lisaks salatile ka šokolaadi, sööd ära ka kaks šokolaaditükikest (juhul, kui on ainult üks tükk, sööd selle). Kui külmkapis pole salatit, aga on šokolaadi, sööd ühe tüki šokolaadi. 

`def cycle(cyclists: list, distance: float, time: int = 0, index: int = None) -> string:` Funktsioon saab ette parameetri `cyclists` - ratturid (järjend, mis koosneb ennikutest kuju (sõne - ratturi nimi, int - kilomeetrid, kui palju rattur ees sõidab, int - minutid, kui kaua rattur ees sõidab)), `distance` - vahemaa (int, inditseerib, mitu km ratturid kokku sõitma peavad), `time` - aeg (int, minutid, kaua ratturid juba sõitnud on), `index` - indeks (int, indeks, mis aitab pidada meeles, milline rattur hetkel ees sõidab). Ülesandeks on leida, milline rattur sõidab esimesena üle finišijoone ning kui kaua ratturid kokku sõitnud on, k.a. viimase ratturi n-ö üleminutid. Kuna suurtel kiirustel on ratturitel raske sõita, siis vahetavad nad eessõitjat, et teised saaksid eessõitja tuules sõita ja puhata. Ratturid vahetavad eessõitjat vastavalt sellele, mitu kilomeetrit üks rattur ees sõitma peab. Kõigepealt sõidab ees listi esimene rattur, siis teine jne, kui viimane rattur on ära sõitnud ja veel on vaja sõita, siis hakkab ring jälle otsast peale (esimese ratturi kord jälle jne). Kui distants on negatiivne või rattureid pole, tuleb tagastada sõnum "Everyone fail.", vastasel juhul tuleb tagastada sõnum kujul "{rattur} is the last leader. Total time: {tunnid}h {minutid}min.", kus rattur on viimase eessõitja nimi, tunnid ja minutid on kogu distantsi läbimiseks kulunud aeg.

`def count_strings(data: list, pos=None, result: dict = None) -> dict:` Funktsioon saab ette parameetri `data` - andmed (järjend järjenditest, mis omakorda koosneb teadmata hulgast sõnedest), `pos` - positsioon (järjend kahest täisarvust, millest esimene inditseerib järjendi indeksit ning teine sõne indeksit järjendi sees) ja `result` - tulemus (sõnastik, kus saab hoida juba leitud võti-väärtus paare ning neid sinna siis juurde lisada). Ülesande eesmärk on tagastada sõnastik etteantud järjendi järjendite kõikidest sõnedest, kus võtmeks on sõne ning väärtuseks arv, mitu korda seda sõne kõikides järjendites kokku leidub. Sõnastik peab olema "sorteeritud" sõne esmakordse esinemise järgi järjendites (ehk teisisõnu pole sorteerida vaja).

### Mall

    """Let's count calories!"""
    
    
    def lets_count_calories(salad: float, chocolate_pieces: int, fridge_visits: int) -> int:
        """
        Every time you go to fridge, you want to eat something. In case you have salad in your fridge, you eat exactly 100g
        of it, no matter what. If you have chocolate in the fridge and you have just eaten salad, you take one piece of
        chocolate. In case you came to fridge and didn't have any salad to eat, you take two pieces of chocolate (if you
        have at least two pieces, if you don't, you take just one). You keep on going to the fridge for a little snack until
        you either run out of fridge visits or snacks.
    
        Eating 100g of salad gives you 120 calories, eating a piece of chocolate gives you 34 calories.
    
        Your job is to count recursively how many calories you eat at total during your fridge visits.
    
        Salad will always be given one decimal place after comma, for an example 5.7, but never like 3.87.
    
        print(lets_count_calories(0.1, 3, 2))  # 120 + 3*34 = 222
        print(lets_count_calories(0.4, 3, 2))  # 2*120 + 2*34 = 308
        print(lets_count_calories(0, 4, 2))  # 4 * 34 = 136
        print(lets_count_calories(3.4, 6, 0))  # 0
        print(lets_count_calories(1.2, 5, 10))  # 1200 + 5*34 = 1370
        print(lets_count_calories(0.3, 8, 6))  # 360 + 3*34 + 2*34 + 2*34 + 34 = 632
        
        :param salad: salad in the fridge, given in kilograms (1.2kg == 1200g).
        :param chocolate_pieces: pieces of chocolate in the fridge.
        :return: calories eaten while visiting fridge.
        """
        pass
    
    
    def cycle(cyclists: list, distance: float, time: int = 0, index: int = None) -> string:
        """
        Given cyclists and distance in kilometers, find out who crosses the finish line first. Cyclists is list of tuples,
        every tuple contains name of the cyclist, how many kilometres this cyclist carries the others and time in minutes
        showing how long it cycles first. If there are no cyclists or distance is 0 or less, return message "Everyone fail."
        else return the last cyclist to carry others and total time taken to cross the finish line, including the last cyclist's
        "over" minutes: "{cyclist1} is the last leader. Total time: {hours}h {minutes}min."
        We'll say if a cyclist has cycled its kilometres ahead of the others, it's the next cyclist's turn. If the last
        cyclist has done the leading, it's time for the first one again.
        
        print(cycle([("First", 0.1, 9), ("Second", 0.1, 8)], 0.3))  #  "First is the last leader. Total time: 0h 26min."
        print(cycle([], 0))  # "Everyone fail."
        print(cycle([("Fernando", 19.8, 42), ("Patricio", 12, 28), ("Daniel", 7.8, 11), ("Robert", 15.4, 49)], 50))  # "Robert is the last leader. Total time: 2h 10min."
        print(cycle([("Loner", 0.1, 1)], 60))  # "Loner is the last leader. Total time: 10h 0min."
        
        :param cyclists: list on tuples, containing cyclist's name, distance it cycles first and time in minutes how long it takes it.
        :param distance: distance to be cycled overall
        :param time: time in minutes indicating how long it has taken cyclists so far
        :param index: index to know which cyclist's turn it is to be first
        :return: string indicating the last cyclist to carry the others
        """
        pass
    
    def count_strings(data: list, pos=None, result: dict = None) -> dict:
        """
        You are given a list of lists which may or may not contain unknown, different amount of strings. Your job is to
        collect these strings into a dict, where key would be the string and value the amount of occurrences of that string
        in these lists. The dict should remain the same order as strings in the lists.
    
        print(count_strings([[], ["J", "*", "W", "f"], ["j", "g", "*"], ["j", "8", "5", "6", "*"], ["*", "*", "A", "8"]])) 
        # {'J': 1, '*': 5, 'W': 1, 'f': 1, 'j': 2, 'g': 1, '8': 2, '5': 1, '6': 1, 'A': 1}
        print(count_strings([[], [], [], [], ["h", "h", "m"], [], ["m", "m", "M", "m"]]))  # {'h': 2, 'm': 4, 'M': 1}
        print(count_strings([]))  # {}
    
        :param data: given list of lists
        :param pos: figure out how to use it
        :param result: figure out how to use it
        :return: dict of given symbols and their count
        """
        pass
