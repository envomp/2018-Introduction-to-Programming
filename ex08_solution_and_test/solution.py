def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.
    (19, False) -> True
    (1, True) -> False.
    """
    return 18 <= time <= 24 or 5 <= time <= 7 and coffee_needed


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    pass


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    pass