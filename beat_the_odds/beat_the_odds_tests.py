import collections
import os
import random
import tempfile

import pytest

import beat_the_odds


@pytest.mark.incgroup("examples")
@pytest.mark.timeout(1.0)
def test_given_examples():
    assert beat_the_odds.guess("__", [], {"hi": 1}) in ('h', 'i')
    assert beat_the_odds.guess("__", [], {"hi": 1, "he": 1}) == 'h'
    assert beat_the_odds.guess("__", [], {"hi": 1, "he": 1, "so": 1}) == 'h'
    assert beat_the_odds.guess('__', [], {'hi': 1, 'he': 3, 'o': 1}) == 'h'
    assert beat_the_odds.guess("__ ___", [], {'this': 2, 'is': 2, 'he': 3, 'so': 1, 'fun': 1, 'sun': 2, 'far': 1}) in ('n', 'u')
    assert beat_the_odds.guess("t___ __ t__t", ['t'], {'term': 3, 'is': 1, 'of': 1, 'that': 4, 'test': 5, 'thin': 2, 'tide': 2}) == 'e'


def _read_words(filename):
    """
    Read file and return dictionary
    where keys represent words
    and values represent the count of the given word.

    Each word is on a separate line.
    :param filename: File to read
    :return: Dictionary of word counts
    """
    d = {}
    with open(filename, 'r') as f:
        for line in f:
            word = line.strip()
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
    return d


def create_file_from_dict(d):
    ctr = collections.Counter(d)
    lst = list(ctr.elements())
    random.shuffle(lst)
    print('creating random file with {} lines'.format(len(lst)))
    f, filepath = tempfile.mkstemp()
    os.write(f, bytes("\n".join(lst), "utf-8"))
    os.close(f)
    return filepath


@pytest.mark.timeout(1.0)
def test_read_words_simple_file():
    d = {'tere': 1, 'tulemast': 2, 'mati': 4}
    filepath = create_file_from_dict(d)
    d2 = beat_the_odds.read_words(filepath)
    assert d == d2


@pytest.mark.timeout(1.0)
def test_read_words_larger_file():
    d = _read_words('beat_the_odds_4000.txt')
    filepath = create_file_from_dict(d)
    d2 = beat_the_odds.read_words(filepath)
    assert d == d2


@pytest.mark.timeout(3.0)
def test_read_words_larger_file_with_repeats():
    """4000 english words, add random repetitions [1..30] for each"""
    d = _read_words('beat_the_odds_4000.txt')
    for key in d:
        cnt = random.randint(1, 30)
        d[key] = cnt
    filepath = create_file_from_dict(d)
    d2 = beat_the_odds.read_words(filepath)
    assert d == d2


@pytest.mark.incgroupdepend("examples")
@pytest.mark.timeout(1.0)
def test_guess_none():
    d = {"aa": 1}
    g = beat_the_odds.guess("___", [], d)
    assert g is None


@pytest.mark.incgroupdepend("examples")
@pytest.mark.timeout(1.0)
def test_guess_one_word():
    d = {'is': 1}
    g = beat_the_odds.guess("__", [], d)
    assert g in ('i', 's')


@pytest.mark.incgroupdepend("examples")
@pytest.mark.timeout(1.0)
def test_guess_one_word_one_guessed_letter():
    d = {'is': 1}
    g = beat_the_odds.guess("_s", ['s'], d)
    assert g == 'i'


@pytest.mark.incgroupdepend("examples")
@pytest.mark.timeout(1.0)
def test_guess_one_word_one_misguessed_letter():
    d = {'is': 1}
    g = beat_the_odds.guess("__", ['g'], d)
    assert g in ('i', 's')


@pytest.mark.incgroupdepend("examples")
@pytest.mark.timeout(1.0)
def test_guess_sentence_with_revealed_letters():
    d = {"test": 2, "that": 3, "tear": 1, "is": 2, "of": 1}
    g = beat_the_odds.guess("t___ __", ['t'], d)
    assert g in ('e', 'a', 'r')
    g = beat_the_odds.guess("t___ _f", ['t', 'f'], d)
    assert g in ('e', 'a', 'r', 'o')


@pytest.mark.incgroupdepend("examples")
@pytest.mark.timeout(1.0)
def test_stuff():
    d = {'aaa': 2, 'aab': 2, 'bbb': 3}
    g = beat_the_odds.guess('___', [], d)
    assert g == 'b'
    g = beat_the_odds.guess('___', ['g'], d)
    assert g == 'b'


@pytest.mark.incgroupdepend("examples")
@pytest.mark.timeout(1.0)
def test_2():
    d = {'a': 1, 'b': 1, 'c': 1, 'ab': 1, 'abc': 1, 'bcc': 2}
    g = beat_the_odds.guess('_ __ ___', [], d)
    assert g in ('a', 'b', 'c')


@pytest.mark.incgroupdepend("examples")
@pytest.mark.timeout(1.0)
def test_3():
    d = {'aaaa': 1, 'bbbb': 2, 'aaab': 3, 'abba': 4, 'caba': 3, 'acce': 2, 'eaab': 3}
    g = beat_the_odds.guess('____ ____', [], d)
    assert g == 'a'


@pytest.mark.incgroupdepend("examples")
@pytest.mark.timeout(1.0)
def test_4():
    d = {'aaaa': 1, 'bbbb': 2, 'aaab': 3, 'abba': 4, 'caba': 3, 'acce': 2, 'eaab': 3}
    g = beat_the_odds.guess('____ ____', ['e'], d)
    assert g == 'b'


@pytest.mark.incgroupdepend("examples")
@pytest.mark.timeout(1.0)
def test_4():
    d = {'aaaa': 1, 'bbbb': 2, 'aaab': 3, 'abba': 4, 'caba': 3, 'acce': 2, 'eaab': 3}
    g = beat_the_odds.guess('____ ____', ['e', 'c'], d)
    assert g in ('a', 'b')


@pytest.mark.incgroupdepend("examples")
@pytest.mark.timeout(10.0)
def test_long():
    d = {}
    d['a' * 99999 + 'g'] = 10000
    d['b' * 100000] = 20000
    d['a' * 60000 + 'b' * 40000] = 30000
    d['b' * 59999 + 'a' * 40001] = 30000
    d['a' * 20000 + 'e' * 80000] = 8030
    s = '_' * 100000
    s = s + ' ' + s
    g = beat_the_odds.guess(s, ['e', 'c'], d)
    assert g in ('a', 'b')


@pytest.mark.incgroupdepend("examples")
@pytest.mark.timeout(1.0)
def test_position_probability_long_guessed_alot():
    d = {}
    d['a' * 99999 + 'g'] = 10000
    d['b' * 100000] = 20000
    d['a' * 60000 + 'b' * 40000] = 30000
    d['b' * 59999 + 'a' * 40001] = 30000
    d['a' * 20000 + 'e' * 80000] = 8030
    s = '_' * 100000
    s = s + ' ' + s
    guessed = list(map(chr, range(99, 123)))
    g = beat_the_odds.guess(s, guessed, d)
    assert g == 'b'


@pytest.mark.incgroupdepend("examples")
@pytest.mark.timeout(1.0)
def test_6():
    d = {'aaaa': 1, 'bbbb': 2, 'aaab': 3, 'abba': 4, 'caba': 3, 'acce': 2, 'eaab': 3}
    g = beat_the_odds.guess('a__a _a_a', ['e', 'a'], d)
    assert g in ('b', 'c')
