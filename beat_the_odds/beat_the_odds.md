# Beat the odds!

Fail Gitis: `beat_the_odds/beat_the_odds.py`

Selles ülesandes peate realiseerima osa õnneratta mängust. Õnneratas (Wheel of fortune) on mäng, kus mängijad keerutavad "õnneratast" ja kui neil veab, saavad arvata ette antud lauset.
Lause arvamine käib nii nagu poomismängus. Mängijale näidatakse lauset, kus algselt on kõik tähed peidetud. Mängija näeb vaid tühikuid sõnade vahel.
Mängija saab pakkuda ühe tähe. Kui see täht on lauses olemas, siis kõik positsioonid, kus esineb pakutud täht, avatakse.
Näiteks, kui arvatav lause on `tere tulemast` ja mängija pakub `t`, näeb ta sellist seisu: `t _ _ _   t _ _ _ _ _ _ t`
(siin näites on tähtede vahele pandud tühik, et oleks parem lugeda - ülesades sellist tühikut pole).

Ülesane eesmärk on etteantud seisu korral pakkuda parim täht.
Funktsioonile antakse ette sõnastik, mis määrab ära, milliseid sõnu saab kasutada lausete moodustamisel.
Arvatav lause on moodustatud nimetatud sõnadest. Funktsioon saab ette ka arvatud tähtede loetelu.
Kui täht on juba "arvatud" (pakutud), siis seda tähte enam pakkuda ei tohi (ei ole mõtet).
Samuti, pakutud tähtedega sõnu moodustada ei saa. Näiteks kui arvatav lause on: `h _ _` ja sõnaraamatus on `heh` ja `hea`,
siis sobib lahenduseks vaid `hea`. `heh` sisaldab `h` tähte, mis peaks olema juba avatud, kuna `h` täht on pakutud.
Samamoodi, kui arvatav lause on `_ _ _` ja sõnaraamatus on samamoodi `heh` ja `hea` ning pakutud on `a`, siis järelikult on algne sõna `heh`,
kuna `a` (`hea` sisaldab `a` tähte) ei sobi.

Parima tähe leidmiseks tuleb teha järgmist:

1. arvutate välja iga sõna kohta, mis on tõenäosus iga võimaliku tähe kohta, et seda tähte esineb vähemalt üks kord selles sõnas.
2. leiate maksimaalse tõenäosuse kõikide sõnade peale.
3. tagastate maksimaalse tõenäosusega tähe. Kui tähti on mitu, tagastate ükskõik millise neist.

Täpsemad näited on allpool funktsiooni kirjelduses.

Lisaks peate kirjutama funktsiooni, mis loeb failist sõnad ja tagastab sõnastiku, kus indeks on sõna ja väärtus on sõna kogus nimetatud failis.
Kui failis on kolm sõna: "tere", "mati", "mati", siis peaks tagastama: `{"tere": 1, "mati": 2}`. Samad sõnad ei pea olema järjest.

Näiteks võib faili sisu olla selline:

```
    mati
    tere
    mati
```

## Mall

`beat_the_odds.py`:

```python

def read_words(filename):
    """
    Read file and return dictionary
    where keys represent words
    and values represent the count of the given word.

    Each word is on a separate line.
    :param filename: File to read
    :return: Dictionary of word counts
    """
    return {'word': 1}


def guess(sentence, guessed_letters, word_dict):
    """
    Offer the letter which would most probably
    give the best result.

    The goal of the game is to guess the sentence.
    The sentence is revealed by revealing letters.
    The player guesses a letter, if the letter
    exists in the sentence, all the given letters
    are revealed. The sentence is revealed when all
    the letters are revealed.

    The function should take into account possible
    words from word_dict parameter. The sentence is
    combined using the words from the dictionary and
    spaces between words.

    The sentence parameter represents the sentence
    to be guessed. The value consists of letters,
    spaces ( ) and underscores (_). Space represents
    the space between the words. Underscore indicates
    a letter which has to be guessed. Letter itself
    represents already guessed and revealed letters.

    In addition, the function takes guessed_letters
    parameter which indicates already guessed letters
    which are not in the sentence.

    The best guess is the letter which would have the
    highest probability to reveal letters in the sentence.
    It doesn't matter how many letters will be reveled,
    the function should take into account the probability
    that at least one letter would be revealed.

    Some examples:
    format:
    x)
    correct sentence
    sentence given to the function
    guessed_letters given to the function
    word_dict given to the function

    1)
    hi
    __
    []
    {"hi": 1}

    If the whole sentence is "hi" (one word)
    it is represented as "__".
    If the dictionary consists of only one word "hi",
    then the probability that "h" or "i" would reveal
    at least one letter is 100% for both.

    2)
    hi
    __
    []
    {"hi": 1, "he": 1}
    probabilities:
    h: 100%
    i: 50%
    e: 50%

    3)
    hi
    __
    []
    {"hi": 1, "he": 1, "so": 1}
    probs:
    h: 66%
    i: 33%
    e: 33%
    s: 33%
    o: 33%

    4)
    hi
    __
    []
    {"hi": 1, "he": 3, "so": 1}
    probs:
    h: 80% (4 cases out of 5)
    e: 60% (3 / 5)
    rest 20% (1 / 5)

    5)
    so fun
    __ ___
    {'this': 2, 'is':2, 'he': 3, 'so': 1, 'fun': 1, 'sun': 2, 'far': 1}
    as we have 2 words, we will give probabilities for both words separately:
    n: 0% 75% (3 out of 4): fuN, suN, suN, far
    u: 0% 75% the same
    s: 50% 50% in first word: So, iS, iS, he, he, he.
                second word: Sun, Sun, fun, far
    f: 0% 50%
    h: 50% 0%
    e: 50% 0%
    i: 33% 0%
    a: 0% 25%
    r: 0% 25%
    o: 16% 0%

    6)
    thin is test
    t___ __ t__t
    ['t'] - 't' is already guessed and revealed
    {'term': 3, 'is': 1, 'of': 1, 'that': 4, 'test': 5, 'thin': 2, 'tide': 2}
    as 't' is already revealed and guessed, the words
    in the sentence cannot contain any more 't' letters.
    The first word can be: term, thin, tide (others have another t)
    the hird word can be: that, test
    Percentages:
    e: 71% 0% 55%
    i: 57% 50% 0%
    s: 0% 50% 55%
    f: 0% 50% 0%
    ....

    :param sentence: Sentence to be guessed.
    :param guessed_letters: A list of already guessed letters
    (both revealed and not existing letters).
    :param word_dict: A dictionary of words and their counts.
    Use the output from read_words.
    :return: The letter with the best probability.
    """
    return 't'
```

Lisaks anname koodi, millega saate mängida arvamise mängu.
See loeb failist sõnad ja genereerib ette antud pikkusega lause.
Nüüd kutsutakse teie implementeeritud "guess" funktsiooni välja seni, kuni lause on arvatud.
Selles koodis te midagi muutma ei pea. Samuti ei pea seda tingimata esitama.

```python

import collections
import random
from heapq import nlargest

def the_game(filename, word_count):
    d = read_words(filename)
    c = collections.Counter(d)
    dictionary_size = sum(c.values())
    correct_sentence = " ".join([x for _, x in nlargest(word_count, ((random.random(), x) for x in c.elements()))])
    sentence = "".join([x if x == ' ' else '_' for x in correct_sentence])
    guessed_letters = []
    print("Correct sentence: " + correct_sentence)
    print(sentence)
    cnt = 0
    while True:
        guessed_letter = guess(sentence, guessed_letters, d)
        if guessed_letter is None or guessed_letter in guessed_letters:
            print("Nothing to guess any more, breaking.")
            break
        print('guessed:' + guessed_letter)
        guessed_letters.append(guessed_letter)
        sentence = "".join([c if c == guessed_letter else sentence[i] for i, c in enumerate(correct_sentence)])
        print("Sentence: " + sentence)
        cnt += 1
        if '_' not in sentence:
            print("Congrats! Number of guesses:" + str(cnt))
            break
```

Eelnevat funktsiooni saab kasutada selliselt.

`the_game('EX04.txt', 3)`

Loeb sõnad failist "EX04.txt" ja genereerib 3-sõnalise lause. Seejärel mängitakse mängu kuni lause arvamiseni.
