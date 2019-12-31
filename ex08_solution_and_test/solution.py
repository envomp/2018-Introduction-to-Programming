"""Three solutions to test."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if 1 <= time <= 4:
        return False
    if 5 <= time <= 17:
        return True if coffee_needed else False
    if 18 <= time <= 24:
        return True


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == b == c:
        return 10 if a == 5 else 5
    if a != b and a != c:
        return 1
    if b == a or c == a:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    if ordered_amount == 0:
        return 0

    if ordered_amount < 5:
        if small_baskets >= ordered_amount:
            return ordered_amount
        else:
            return -1
    else:
        needed_big_baskets = ordered_amount // 5
        needed_small_baskets = ordered_amount % 5
        needed_after_sub_big_baskets = (needed_big_baskets - big_baskets) * 5 + needed_small_baskets

        if big_baskets >= needed_big_baskets:
            return needed_small_baskets if small_baskets >= needed_small_baskets else -1
        else:
            return needed_after_sub_big_baskets if needed_after_sub_big_baskets <= small_baskets else -1


if __name__ == '__main__':
    # print(students_study(25, False))  # -> True
    # print(students_study(1, True))  # -> False
    # print(lottery(5, 5, 5))  # -> 10
    # print(lottery(2, 2, 1))  # -> 0
    # print(lottery(2, 3, 1))  # -> 1
    print(fruit_order(5, 2, 0))  # -> 0 O-ne tellimus, väljastatakse 0
    print(fruit_order(5, 1, 2))  # -> 2  Poolikut suurt ei väljastata
