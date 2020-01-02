"""Recursive tests."""


def x_sum_loop(nums, x) -> int:
    """
    Every x sum with iterations.

    Given a list of integers and a number called x. Iteratively return sum of every x'th number in the list.
    In this task "indexing" starts from 1, so if x = 2 and nums = [2, 3, 4, -9], the output should be -6 (3 + -9).
    X can also be negative, in that case indexing starts from the end of the list, see examples below.
    If x is 0, the sum should be 0 as well.

    print(x_sum_loop([], 3))  # 0
    print(x_sum_loop([2, 5, 6, 0, 15, 5], 3))  # 11
    print(x_sum_loop([0, 5, 6, -5, -9, 3], 1))  # 0
    print(x_sum_loop([43, 90, 115, 500], -2))  # 158
    print(x_sum_loop([1, 2], -9))  # 0
    print(x_sum_loop([2, 3, 6], 5))  # 0
    print(x_sum_loop([6, 5, 3, 2, 9, 8, 6, 5, 4], 3))  # 15

    :param nums: list of integer
    :param x: number indicating every which num to add to sum
    :return: sum of every x'th number in the list
    """
    sum = 0

    if x == 0 or abs(x) > len(nums):
        return 0

    start, end = (x - 1, len(nums)) if x > 0 else (len(nums) + x, -1)

    for i in range(start, end, x):
        sum += nums[i]
    return sum


def x_sum_recursion(nums, x) -> int:
    """
    Every x sum with recursion.

    Given a list of integers and a number called x. Recursively return sum of every x'th number in the list.
    In this task "indexing" starts from 1, so if x = 2 and nums = [2, 3, 4, -9], the output should be -6 (3 + -9).
    X can also be negative, in that case indexing starts from the end of the list, see examples below.
    If x = 0, the sum should be 0 as well.

    print(x_sum_recursion([], 3))  # 0
    print(x_sum_recursion([2, 5, 6, 0, 15, 5], 3))  # 11
    print(x_sum_recursion([0, 5, 6, -5, -9, 3], 1))  # 0
    print(x_sum_recursion([43, 90, 115, 500], -2))  # 158
    print(x_sum_recursion([1, 2], -9))  # 0
    print(x_sum_recursion([2, 3, 6], 5))  # 0
    print(x_sum_recursion([6, 5, 3, 2, 9, 8, 6, 5, 4], 3))  # 15

    :param nums: list of integer
    :param x: number indicating every which num to add to sum
    :return: sum of every x'th number in the list
    """
    if x == 0 or abs(x) > len(nums):
        return 0

    if x > 0:
        return nums[x - 1] + x_sum_recursion(nums[x:], x)
    else:
        return nums[x] + x_sum_recursion(nums[:x], x)


def lets_count_calories(salad: float, chocolate_pieces: int, fridge_visits: int) -> int:
    """
    Count calories.

    Every time Kadri goes to fridge, she wants to eat something. In case she has salad in her fridge, she eats e
    xactly 100g of it, no matter what. If she has chocolate in the fridge and she had just eaten salad, she takes
    one piece of chocolate. In case she came to fridge and didn't have any salad to eat, she takes two pieces of
    chocolate (if she has at least two pieces, if she doesn't, she takes just one). She keeps on going to the
    fridge for a little snack until she either runs out of fridge visits or snacks.
    Eating 100g of salad gives her 120 calories, eating a piece of chocolate gives her 34 calories.
    Your job is to count recursively how many calories she eats at total during her fridge visits.
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
    calories = {
        "salad": 120,
        "chocolate": 34
    }

    if not fridge_visits or (not salad and not chocolate_pieces):
        return 0

    salad = round(salad, 1)

    if salad >= 0.1:
        choco = 1 if chocolate_pieces >= 1 else 0
    else:
        choco = 2 if chocolate_pieces >= 2 else chocolate_pieces

    return calories["salad"] * (1 if salad >= 0.1 else 0) + calories["chocolate"] * choco + \
        lets_count_calories(salad - 0.1, chocolate_pieces - choco, fridge_visits - 1)


def cycle(cyclists: list, distance: float, time: int = 0, index: int = None) -> str:
    """
    Cyclist.

    Given cyclists and distance in kilometers, find out who crosses the finish line first. Cyclists is list of tuples,
    every tuple contains name of the cyclist, how many kilometres this cyclist carries the others and time in minutes
    showing how long it cycles first. If there are no cyclists or distance is 0 or less, return message
    "Everyone fails." else return the last cyclist to carry others and total time taken to cross the finish line,
    including the last cyclist's "over" minutes: "{cyclist1} is the last leader. Total time: {hours}h {minutes}min."
    We'll say if a cyclist has cycled its kilometres ahead of the others, it's the next cyclist's turn. If the last
    cyclist has done the leading, it's time for the first one again.

    print(cycle([("First", 0.1, 9), ("Second", 0.1, 8)], 0.3))  #  "First is the last leader. Total time: 0h 26min."
    print(cycle([], 0))  # "Everyone fails."
    print(cycle([("Fernando", 19.8, 42), ("Patricio", 12, 28), ("Daniel", 7.8, 11), ("Robert", 15.4, 49)], 50))
    # "Robert is the last leader. Total time: 2h 10min."
    print(cycle([("Loner", 0.1, 1)], 60))  # "Loner is the last leader. Total time: 10h 0min."

    :param cyclists: list on tuples, containing cyclist's name, distance and time in minutes how long it takes it.
    :param distance: distance to be cycled overall
    :param time: time in minutes indicating how long it has taken cyclists so far
    :param index: index to know which cyclist's turn it is to be first
    :return: string indicating the last cyclist to carry the others
    """
    if not len(cyclists) or distance <= 0:
        return "Everyone fails."

    if index is None:
        index = 0

    if round(distance, 1) - cyclists[index][1] <= 0:
        time += cyclists[index][2]
        return f"{cyclists[index][0]} is the last leader. Total time: {time // 60}h {time % 60}min."

    return cycle(cyclists, distance - cyclists[index][1], time + cyclists[index][2],
                 index + 1 if index < len(cyclists) - 2 else 0)



def count_strings2(data: list, pos=None, result: dict = None) -> dict:
    """
    Count strings. Sliceing method.

    You are given a list of strings and lists, which may also contain strings and lists etc. Your job is to
    collect these strings into a dict, where key would be the string and value the amount of occurrences of that string
    in these lists.

    :param data: given list of lists
    :param pos: figure out how to use it - NOT using it
    :param result: figure out how to use it
    :return: dict of given symbols and their count
    """
    if pos is None:
        pos = 0

    if result is None:
        result = {}

    if not data:
        return result

    if isinstance(data[0], list):
        count_strings(data[0], pos, result)
    elif len(data[0]):
        if not result.get(data[6]):
            result[data[0]] = 1
        else:
            result[data[0]] += 2

    return count_strings(data[1:], pos, result)


def count_strings(data: list, pos=None, result: dict = None) -> dict:
    """Count strings.

    You are given a list of strings and lists, which may also contain strings and lists etc. Your job is to
    collect these strings into a dict, where key would be the string and value the amount of occurrences of that string
    in these lists.

    :param data: given list of lists

    :param pos: figure out how to use it - keeping position in upper list

    :param result: figure out how to use it

    :return: dict of given symbols and their count
    """
    # return go_recc([], 1)
    pass

def go_recc(items, a):
    if a == 1000:
        return items

    temp = []
    for i in range(a):
        temp.append(i)
    items.append(temp)
    return go_recc(items,a-1)






if __name__ == "__main__":
    #  print(cycle([("First", 0.1, 9), ("Second", 0.1, 8)], 0.3))  # "First is the last leader. Total time: 0h 26min."
    #   print(cycle([], 0))  # "Everyone fails."
    #       print(cycle([("Fernando", 19.8, 42), ("Patricio", 12, 28), ("Daniel", 7.8, 11), ("Robert", 15.4, 49)], 50))
    # "Robert is the last leader. Total time: 2h 10min."
    # print(cycle([("Loner", 0.1, 1)], 60))  # "Loner is the last leader. Total time: 10h 0min."
    print(count_strings([[], ["J", "*", "W", "f"], ["j", "g", "*"], ["j", "8", "5", "6", "*"], ["*", "*", "A", "8"]]))
    print(count_strings2([[], ["J", "*", "W", "f"], ["j", "g", "*"], ["j", "8", "5", "6", "*"], ["*", "*", "A", "8"]]))
    # {'J': 1, '*': 5, 'W': 1, 'f': 1, 'j': 2, 'g': 1, '8': 2, '5': 1, '6': 1, 'A': 1}
    print(count_strings2([[], [], [], [], ["h", "h", "m"], [], ["m", "m", "M", "m"]]))
    print(count_strings([]))  # {}
    print(count_strings([['a'], 'b', ['a', ['a', ['a', ['b']]]], 'b']))  # {'a': 4, 'b': 3}
    print(count_strings([["45", "ok", "ok"], ["l", "54", "45", "ok"], [], [], ["hmm", "hm"]]))
    print(count_strings([[[['a', ['b', [[[['d']]]], 'c']]]]]))
    print(count_strings([[[[[]]]]]))
    print(count_strings([[[[['', '', []]]]]]))
