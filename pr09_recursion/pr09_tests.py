"""Tests, yay!"""


import pytest
from recursion import x_sum_loop, x_sum_recursion, remove_nums_and_reverse, task1, task2
from random import randint, choices
import string


# X_SUM_LOOP

def my_x_sum(nums, x):
    if len(nums) == 0 or x == 0:
        return 0
    sum = 0
    if x < 0:
        nums.reverse()
        x = -x
    for i in range(x - 1, len(nums), x):
        sum += nums[i]
    return sum


def my_reverse_and_remove_nums(string):
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    if len(string) == 0:
        return ""
    elif string[0] in nums:
        return remove_nums_and_reverse(string[1:])
    return remove_nums_and_reverse(string[1:]) + string[0]


def my_task2(string):
    if len(string) < 2:
        return string
    answer = string[0]
    prev = string[0]
    for c in string[1:]:
        if prev == c:
            answer += "-"
        answer += c
        prev = c
    return answer


@pytest.mark.timeout(10.0)
def test_x_sum_loop_has_iteration():
    try:
        x_sum_loop([3, 4, 5, 6] * 9999, 1)
    except RecursionError:
        pytest.fail("Where is iteration?")


@pytest.mark.timeout(1.0)
def test_x_sum_loop_examples():
    assert not x_sum_loop([], 3)
    assert x_sum_loop([2, 5, 6, 0, 15, 5], 3) == 11
    assert not x_sum_loop([0, 5, 6, -5, -9, 3], 1)
    assert x_sum_loop([43, 90, 115, 500], -2) == 158
    assert not x_sum_loop([1, 2], -9)
    assert not x_sum_loop([2, 3, 6], 5)
    assert x_sum_loop([6, 5, 3, 2, 9, 8, 6, 5, 4], 3) == 15


@pytest.mark.timeout(1.0)
def test_x_sum_loop_empty_list():
    assert x_sum_loop([], 3) == 0


@pytest.mark.timeout(1.0)
def test_x_sum_loop_insufficient_x():
    assert x_sum_loop([9], 8) == 0
    assert x_sum_loop([7, 7, 7], 0) == 0
    assert x_sum_loop([5, 4, 3], -5) == 0


@pytest.mark.timeout(1.0)
def test_x_sum_loop_positive_x():
    assert x_sum_loop([2, 3, 89, 23], 1) == 117
    assert x_sum_loop([0, 0, 3], 2) == 0
    assert x_sum_loop([-34, 17, 2, 9999, 5, 23, 1, 5, 3], 3) == 28


@pytest.mark.timeout(1.0)
def test_x_sum_loop_negative_x():
    assert x_sum_loop([5, 2, 4, -3], -2) == 9
    assert x_sum_loop([3, 3, 3, 3, 2], -1) == 14
    assert x_sum_loop([5, 2, 4, -3], -2) == 9
    assert x_sum_loop([5, 4, 3], -5) == 0


@pytest.mark.timeout(2.0)
def test_x_sum_loop_random_pos_index():
    data = []
    for _ in range(randint(5, 200)):
        data.append(randint(-2000, 2000))
    multiplier = randint(1, 30)
    assert x_sum_loop(data.copy(), multiplier) == my_x_sum(data.copy(), multiplier)


@pytest.mark.timeout(2.0)
def test_x_sum_loop_random_neg_index():
    data = []
    for _ in range(randint(5, 200)):
        data.append(randint(-2000, 2000))
    multiplier = randint(-30, -1)
    #print(data)
    assert x_sum_loop(data.copy(), multiplier) == my_x_sum(data.copy(), multiplier)


@pytest.mark.timeout(1.0)
def test_x_sum_loop():
    test_x_sum_loop_has_iteration()
    test_x_sum_loop_examples()
    test_x_sum_loop_empty_list()
    test_x_sum_loop_insufficient_x()
    test_x_sum_loop_positive_x()
    test_x_sum_loop_negative_x()
    test_x_sum_loop_random_pos_index()
    test_x_sum_loop_random_neg_index()


# X_SUM_RECURSION


@pytest.mark.timeout(10.0)
def test_x_sum_recursion_has_recursion():
    try:
        x_sum_recursion([3, 4, 5, 6] * 9999, 1)
        pytest.fail("Where is recursion?")
    except RecursionError:
        pass


@pytest.mark.timeout(1.0)
def test_x_sum_recursion_examples():
    assert not x_sum_recursion([], 3)
    assert x_sum_recursion([2, 5, 6, 0, 15, 5], 3) == 11
    assert not x_sum_recursion([0, 5, 6, -5, -9, 3], 1)
    assert x_sum_recursion([43, 90, 115, 500], -2) == 158
    assert not x_sum_recursion([1, 2], -9)
    assert not x_sum_recursion([2, 3, 6], 5)
    assert x_sum_recursion([6, 5, 3, 2, 9, 8, 6, 5, 4], 3) == 15


@pytest.mark.timeout(1.0)
def test_x_sum_recursion_empty_list():
    assert x_sum_recursion([], 4) == 0


@pytest.mark.timeout(1.0)
def test_x_sum_recursion_insufficient_x():
    assert x_sum_recursion([5, 3], 3) == 0
    assert x_sum_recursion([4, 0, 90], 0) == 0
    assert x_sum_recursion([5, 30, 4, 0], -8) == 0


@pytest.mark.timeout(1.0)
def test_x_sum_recursion_positive_x():
    assert x_sum_recursion([8, 90, 12, 54, -66], 1) == 98
    assert x_sum_recursion([0, 0, 0, 0, 0, 0, 0, 0, 0], 3) == 0
    assert x_sum_recursion([0, 1, 2, 3, 4, 5, 6, 7], 2) == 16
    assert x_sum_recursion([-34, 9, 0, 12, 32, 8, 3, 12], 4) == 24


@pytest.mark.timeout(1.0)
def test_x_sum_recursion_negative_x():
    assert x_sum_recursion([3, -2, 3, 1, 9], -1) == 14
    assert x_sum_recursion([2, 4], -3) == 0
    assert x_sum_recursion([4, 90, 12, -40], -2) == 16
    assert x_sum_recursion([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], -5) == 13


@pytest.mark.timeout(2.0)
def test_x_sum_recursion_random_pos_index():
    data = []
    for _ in range(randint(5, 200)):
        data.append(randint(-2000, 2000))
    multiplier = randint(1, 30)
    assert x_sum_recursion(data.copy(), multiplier) == my_x_sum(data.copy(), multiplier)


@pytest.mark.timeout(2.0)
def test_x_sum_recursion_random_neg_index():
    data = []
    for _ in range(randint(5, 200)):
        data.append(randint(-2000, 2000))
    multiplier = randint(-30, -1)
    assert x_sum_recursion(data.copy(), multiplier) == my_x_sum(data.copy(), multiplier)


@pytest.mark.timeout(1.0)
def test_x_sum_recursion():
    test_x_sum_recursion_has_recursion()
    test_x_sum_recursion_examples()
    test_x_sum_recursion_empty_list()
    test_x_sum_recursion_insufficient_x()
    test_x_sum_recursion_positive_x()
    test_x_sum_recursion_negative_x()
    test_x_sum_recursion_random_pos_index()
    test_x_sum_recursion_random_neg_index()


# REMOVE_NUMS_AND_REVERSE


@pytest.mark.timeout(10.0)
def test_remove_nums_and_reverse_has_recursion():
    try:
        remove_nums_and_reverse("9823yfhui" * 9999)
        pytest.fail("Where is recursion?")
    except RecursionError:
        pass


@pytest.mark.timeout(1.0)
def test_remove_nums_and_reverse_examples():
    assert remove_nums_and_reverse("poo") == "oop"
    assert not remove_nums_and_reverse("3129047284")
    assert remove_nums_and_reverse("34e34f7i8l 00r532o23f 4n5oh565ty7p4") == "python for life"
    assert remove_nums_and_reverse("  k 4") == " k  "


@pytest.mark.timeout(1.0)
def test_remove_nums_and_reverse_empty_string():
    assert not remove_nums_and_reverse("")


@pytest.mark.timeout(1.0)
def test_remove_nums_and_reverse_no_nums():
    assert remove_nums_and_reverse("no nums here") == "ereh smun on"
    assert remove_nums_and_reverse("hihihi") == "ihihih"


@pytest.mark.timeout(1.0)
def test_remove_nums_and_reverse_contains_nums_only():
    assert not remove_nums_and_reverse("247298374892")
    assert not remove_nums_and_reverse("0")


@pytest.mark.timeout(1.0)
def test_remove_nums_and_reverse_nums_and_other():
    assert remove_nums_and_reverse("34go550tta43 89r78e68v78e7r8se6 89t98h989a898t98 98s9t8r9898i98n9g89") \
           == "gnirts taht esrever attog"
    assert remove_nums_and_reverse("a89o5234 2 ok 34 ") == "  ko  oa"


@pytest.mark.timeout(1.0)
def test_remove_nums_and_reverse_random_small():
    stringie = ''.join(choices(string.ascii_letters + string.digits, k=35))
    assert remove_nums_and_reverse(stringie) == my_reverse_and_remove_nums(stringie)


@pytest.mark.timeout(2.0)
def test_remove_nums_and_reverse_random_medium():
    stringie = ''.join(choices(string.ascii_letters + string.digits, k=350))
    assert remove_nums_and_reverse(stringie) == my_reverse_and_remove_nums(stringie)


@pytest.mark.timeout(3.0)
def test_remove_nums_and_reverse_random_big():
    stringie = ''.join(choices(string.ascii_letters + string.digits, k=900))
    assert remove_nums_and_reverse(stringie) == my_reverse_and_remove_nums(stringie)


@pytest.mark.timeout(.0)
def test_remove_nums_and_reverse():
    test_remove_nums_and_reverse_has_recursion()
    test_remove_nums_and_reverse_examples()
    test_remove_nums_and_reverse_empty_string()
    test_remove_nums_and_reverse_no_nums()
    test_remove_nums_and_reverse_contains_nums_only()
    test_remove_nums_and_reverse_nums_and_other()
    test_remove_nums_and_reverse_random_small()
    test_remove_nums_and_reverse_random_medium()
    test_remove_nums_and_reverse_random_big()


# TASK1


@pytest.mark.timeout(10.0)
def test_task1_has_recursion():
    try:
        task1("hk" * 9999 + "h")
        pytest.fail("Where is recursion?")
    except RecursionError:
        pass


@pytest.mark.timeout(1.0)
def test_task1_empty_string():
    assert task1("")


@pytest.mark.timeout(1.0)
def test_task1_odd_length():
    assert task1("k")
    assert not task1("not")
    assert task1("jepppej")


@pytest.mark.timeout(1.0)
def test_task1_even_length():
    assert task1("11")
    assert not task1("23")
    assert not task1("joiojk")
    assert task1("meem")


@pytest.mark.timeout(1.0)
def test_task1():
    test_task1_has_recursion()
    test_task1_empty_string()
    test_task1_odd_length()
    test_task1_even_length()


# TASK2


@pytest.mark.timeout(10.0)
def test_task2_has_iteration():
    try:
        task2("meoww" * 9999)
    except RecursionError:
        pytest.fail("Where is iteration?")


@pytest.mark.timeout(1.0)
def test_task2_empty_string():
    assert not task2("")


@pytest.mark.timeout(1.0)
def test_task2_no_changes():
    assert task2("Absolutely no repetitions here!") == "Absolutely no repetitions here!"
    assert task2("CaSe MaTtErSsSsSs") == "CaSe MaTtErSsSsSs"
    assert task2("stil-l nope") == "stil-l nope"
    assert task2("o") == "o"


@pytest.mark.timeout(1.0)
def test_task2_change_string():
    assert task2("kkkk") == "k-k-k-k"
    assert task2("ookoo") == "o-oko-o"
    assert task2("---") == "-----"
    assert task2("oopplloo") == "o-op-pl-lo-o"


@pytest.mark.timeout(1.0)
def test_task2_random_small():
    stringie = ''.join(choices(string.ascii_lowercase, k=30))
    assert task2(stringie) == my_task2(stringie)


@pytest.mark.timeout(2.0)
def test_task2_random_medium():
    stringie = ''.join(choices(string.ascii_lowercase, k=300))
    assert task2(stringie) == my_task2(stringie)


@pytest.mark.timeout(3.0)
def test_task2_random_big():
    stringie = ''.join(choices(string.ascii_lowercase, k=900))
    assert task2(stringie) == my_task2(stringie)


@pytest.mark.timeout(1.0)
def test_task2():
    test_task2_has_iteration()
    test_task2_empty_string()
    test_task2_no_changes()
    test_task2_change_string()
    test_task2_random_small()
    test_task2_random_medium()
    test_task2_random_big()


test_x_sum_loop()
test_x_sum_recursion()
test_remove_nums_and_reverse()
test_task1()
test_task2()
