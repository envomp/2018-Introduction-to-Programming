import pytest
from recursive_calories import lets_count_calories, cycle, count_strings
from random import randint, choices
import string

# LET'S COUNT CALORIES


def my_lets_count_calories(salad, chocolate_pieces, fridge_visits):
    if fridge_visits == 0 or round(salad, 2) == 0 and chocolate_pieces == 0:
        return 0
    elif round(salad, 2) == 0:
        if chocolate_pieces >= 2:
            return 2 * 34 + lets_count_calories(salad, chocolate_pieces - 2, fridge_visits - 1)
        else:
            return 34 + lets_count_calories(salad, chocolate_pieces - 1, fridge_visits - 1)
    else:
        if chocolate_pieces > 0:
            return 120 + 34 + lets_count_calories(salad - 0.1, chocolate_pieces - 1, fridge_visits - 1)
        else:
            return 120 + lets_count_calories(salad - 0.1, chocolate_pieces, fridge_visits - 1)


def my_cycle(cyclists: list, distance: float, time: int = 0, index: int = None):
    if index is None and distance <= 0 or not cyclists:
        return "Everyone fail."
    if index is None:
        index = 0
    time += cyclists[index][2]
    if round(distance - cyclists[index][1], 2) <= 0:
        hours = time // 60
        minutes = time % 60
        return cyclists[index][0] + " is the last leader. Total time: " + str(hours) + "h " + str(minutes) + "min."
    if index + 1 == len(cyclists):
        index = -1
    return cycle(cyclists, round(distance - cyclists[index][1], 2), time, index + 1)


def my_count_strings(data: list, pos=None, cache: dict=None):
    if len(data) == 0:
        return {}
    elif pos is None:
        pos = [0, 0]
        cache = {}
    if len(data[pos[0]]) == 0 and pos[0] + 1 != len(data):
        return count_strings(data, [pos[0] + 1, 0], cache)
    if data[pos[0]][pos[1]] in cache.keys():
        cache[data[pos[0]][pos[1]]] = cache.get(data[pos[0]][pos[1]]) + 1
    else:
        cache[data[pos[0]][pos[1]]] = 1
    if pos[1] == len(data[pos[0]]) - 1:
        if pos[0] == len(data) - 1:
            return cache
        return count_strings(data, [pos[0] + 1, 0], cache)
    return count_strings(data, [pos[0], pos[1] + 1], cache)


@pytest.mark.timeout(1.0)
def test_lets_count_calories_has_recursion():  # Works
    try:
        lets_count_calories(999999, 9999999, 9999999)
        pytest.fail()
    except RecursionError:
        pass


@pytest.mark.timeout(1.0)
def test_lets_count_calories_example():
    assert lets_count_calories(0.1, 3, 2) == 222
    assert lets_count_calories(0.4, 3, 2) == 308
    assert lets_count_calories(0, 4, 2) == 136
    assert lets_count_calories(3.4, 6, 0) == 0
    assert lets_count_calories(1.2, 5, 10) == 1370
    assert lets_count_calories(0.3, 8, 6) == 632


@pytest.mark.timeout(1.0)
def test_lets_count_calories_zero_calories():
    assert not lets_count_calories(5.6, 4, 0)
    assert not lets_count_calories(0, 0, 99)


@pytest.mark.timeout(1.0)
def test_lets_count_calories_more_chocolate():
    assert lets_count_calories(0.2, 5, 3) == 376
    assert lets_count_calories(0.2, 3, 3) == 342
    assert lets_count_calories(1.2, 70, 15) == 12 * 120 + 12 * 34 + 3 * 2 * 34


@pytest.mark.timeout(1.0)
def test_lets_count_calories_not_enough_snacks():
    assert lets_count_calories(0.9, 3, 40) == 9 * 120 + 3 * 34
    assert lets_count_calories(0, 40, 41) == 40 * 34


@pytest.mark.timeout(1.0)
def test_lets_count_calories_too_much_food():
    assert lets_count_calories(0.9, 3, 4) == 4 * 120 + 3 * 34
    assert lets_count_calories(12, 70, 15) == 15 * 120 + 15 * 34


@pytest.mark.timeout(1.0)
def test_lets_count_calories_random():
    salad = randint(1, 900) / 10
    chocolate = randint(1, 700)
    fridge_time = randint(1, 1000)
    assert lets_count_calories(salad, chocolate, fridge_time) == my_lets_count_calories(salad, chocolate, fridge_time)


@pytest.mark.timeout(1.0)
def test_lets_count_calories():
    test_lets_count_calories_has_recursion()
    test_lets_count_calories_example()
    test_lets_count_calories_zero_calories()
    test_lets_count_calories_more_chocolate()
    test_lets_count_calories_not_enough_snacks()
    test_lets_count_calories_too_much_food()
    test_lets_count_calories_random()


# CYCLE


@pytest.mark.timeout(1.0)
def test_cycle_has_recursion():  # Works
    try:
        cycle([("Meow", 0.1, 5)], 9999999)
        pytest.fail()
    except RecursionError:
        pass


@pytest.mark.timeout(1.0)
def test_cycle_example():
    assert cycle([("First", 0.1, 9), ("Second", 0.1, 8)], 0.3) == "First is the last leader. Total time: 0h 26min."
    assert cycle([], 0) == "Everyone fail."
    assert cycle([("Fernando", 19.8, 42), ("Patricio", 12, 28), ("Daniel", 7.8, 11), ("Robert", 15.4, 49)], 50) == \
           "Robert is the last leader. Total time: 2h 10min."
    assert cycle([("Loner", 0.1, 1)], 60) == "Loner is the last leader. Total time: 10h 0min."


@pytest.mark.timeout(1.0)
def test_cycle_everyone_fail():
    assert cycle([], 0) == "Everyone fail."


@pytest.mark.timeout(1.0)
def test_cycle_more():
    assert cycle([("Meow", 12.5, 37), ("Woof", 3.1, 8), ("Moo", 23.5, 61), ("Bulb", 2.6, 3)], 43) == \
           "Meow is the last leader. Total time: 2h 26min."
    assert cycle([("Slow", 13.5, 90), ("Fast", 32.1, 15), ("Random Guy", 4.5, 19)], 1267)


@pytest.mark.timeout(1.0)
def test_cycle_random():
    data = []
    whole_distance = randint(20, 2000)
    for _ in range(randint(5, 50)):
        name = ''.join(choices(string.ascii_lowercase, k=8))
        data.append((name.capitalize(), randint(30, 400) / 10, randint(1, 100)))
    assert cycle(data, whole_distance) == my_cycle(data, whole_distance)
    #cycle([("kaheksa!", 3, 1) * 50], 2000)


@pytest.mark.timeout(1.0)
def test_cycle():
    test_cycle_has_recursion()
    test_cycle_example()
    test_cycle_more()
    test_cycle_everyone_fail()
    test_cycle_random()


# COUNT STRINGS


@pytest.mark.timeout(1.0)
def test_count_string_has_recursion():  # Works
    try:
        count_strings([["k"] * 9999])
        pytest.fail()
    except RecursionError:
        pass


@pytest.mark.timeout(1.0)
def test_count_strings_example():
    assert count_strings([[], ["J", "*", "W", "f"], ["j", "g", "*"], ["j", "8", "5", "6", "*"], ["*", "*", "A", "8"]]) \
           == {'J': 1, '*': 5, 'W': 1, 'f': 1, 'j': 2, 'g': 1, '8': 2, '5': 1, '6': 1, 'A': 1}
    assert count_strings([[], [], [], [], ["h", "h", "m"], [], ["m", "m", "M", "m"]]) == {'h': 2, 'm': 4, 'M': 1}
    assert not count_strings([])


@pytest.mark.timeout(1.0)
def test_count_strings_contains_empty():
    assert count_strings([[], ["0", "k", "k"], [], ["y", "y", "y"]]) == {"0": 1, "k": 2, "y": 3}
    assert not count_strings([])


@pytest.mark.timeout(1.0)
def test_count_strings_case_matters():
    assert count_strings([["O", "o", "o", "O"], ["k", "K", "k", "k", "?", "?"]]) \
           == {"O": 2, "o": 2, "k": 3, "K": 1, "?": 2}


@pytest.mark.timeout(1.0)
def test_count_strings_more():
    assert count_strings([["45", "ok", "ok"], ["l", "54", "45", "ok"], [], [], ["hmm", "hm"]]) \
           == {'45': 2, 'ok': 3, 'l': 1, '54': 1, 'hmm': 1, 'hm': 1}


@pytest.mark.timeout(1.0)
def test_count_strings_random():
    data = []
    for _ in range(randint(3, 30)):
        small_data = []
        for _ in range(randint(0, 33)):
            small_data.append(''.join(choices(string.ascii_lowercase, k=1)))
        data.append(small_data)
    assert count_strings(data.copy()) == my_count_strings(data.copy())


@pytest.mark.timeout(1.0)
def test_count_strings():
    test_count_strings_example()
    test_count_strings_contains_empty()
    test_count_strings_case_matters()
    test_count_strings_more()
    test_count_strings_random()


test_lets_count_calories()
test_cycle_example()
test_count_strings()
