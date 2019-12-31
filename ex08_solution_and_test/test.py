"""Test solution.py tests."""
import solution


def test_students_study_night_with_coffee():  # Test 1
    """Coffee is not needed at night."""
    assert solution.students_study(1, True) is False


def test_students_study_night_wo_coffee():  # Test 2
    """Coffee is not needed at night."""
    assert solution.students_study(4, False) is False


def test_students_study_daytime_with_coffee():  # Test 3
    """Coffee is needed on daytime."""
    assert solution.students_study(5, True) is True


def test_students_study_daytime_wo_coffee():  # Test 4
    """Coffee is needed on daytime."""
    assert solution.students_study(17, False) is False


def test_students_study_coffee_not_important():  # Test 5 & 6
    """Coffee is not important."""
    assert solution.students_study(19, True) == solution.students_study(19, False)


def test_students_study_loop_evening_night():  # Test 7
    """Loop all values when time changes."""
    for i in range(18, 30):
        if (i % 25) != 0:
            if (i % 25) < 5:
                assert solution.students_study(i % 25, True) is False
            else:
                assert solution.students_study(i % 25, True) is True


def test_students_study_loop_day_evening():  # Test 8
    """Loop all values when time changes."""
    for i in range(5, 25):
        if i < 18:
            assert solution.students_study(i, False) is False
        else:
            assert solution.students_study(i, False) is True


def test_students_study_loop_coffee_important():  # Test 9
    """Loop all values when coffee important."""
    for i in range(1, 25):
        assert solution.students_study(i, True) is False if i < 5 else True


def test_students_study_loop_coffee_not_important():  # Test 10 & 12
    """Loop all values when coffee not important."""
    for i in range(1, 25):
        assert solution.students_study(i, False) is False if i < 18 else True


def test_students_study_loop_night_day():  # Test 11
    """Loop all values when time changes."""
    for i in range(1, 18):
        if i < 5:
            assert solution.students_study(i, True) is False
        else:
            assert solution.students_study(i, True) is True

# Tests 1-12 (12/12) passed


def test_lottery_all_equal_5():  # test 13
    """All equal 5."""
    assert solution.lottery(5, 5, 5) == 10


def test_lottery_all_equal_not_5():  # test 14
    """All equal not 5."""
    assert solution.lottery(4, 4, 4) == 5


def test_lottery_all_equal_neg():  # test 15
    """All equal negative."""
    assert solution.lottery(-5, -5, -5) == 5


def test_lottery_all_zero():  # test 16
    """All equal 0."""
    assert solution.lottery(0, 0, 0) == 5


def test_lottery_a_is_b():  # test 17
    """A is B or A is C."""
    assert solution.lottery(6, 6, 2) == 0


def test_lottery_a_is_c():  # test 18
    """A is B or A is C."""
    assert solution.lottery(7, 2, 7) == 0


def test_lottery_a_not_b_c_and_b_is_c():  # test 19
    """A not B and A not C and B == C."""
    assert solution.lottery(1, 2, 2) == 1


def test_lottery_a_not_b_and_a_not_c():  # test 20
    """A not B and A not C."""
    assert solution.lottery(4, 2, 1) == 1

# Tests 13-20 (8/8) passed


def test_fruit_order_all_0():  # test 21
    """All 0."""
    assert solution.fruit_order(0, 0, 0) == 0


def test_fruit_order_s_0_a_0():  # test 22
    """Small 0, Amount 0."""
    assert solution.fruit_order(0, 2, 0) == 0


def test_fruit_order_b_0_a_0():  # test 23
    """Big 0, Amount 0."""
    assert solution.fruit_order(2, 0, 0) == 0


def test_fruit_order_a_0():  # test 24
    """Amount 0."""
    assert solution.fruit_order(1, 2, 0) == 0


def test_fruit_order_a_6_s_0_b_1():  # tests 25 & 27
    """Can't take amount."""
    assert solution.fruit_order(0, 1, 6) == -1


def test_fruit_order_a_15_s_0_b_2():  # test 26
    """Can't take amount."""
    assert solution.fruit_order(0, 2, 15) == -1


def test_fruit_order_a_10_s_0_b_3():  # test 28
    """Exact amount taken from big when small is 0."""
    assert solution.fruit_order(0, 3, 10) == 0


def test_fruit_order_a_1_s_0_b_1():  # test 29
    """Amount cant taken."""
    assert solution.fruit_order(0, 1, 1) == -1


def test_fruit_order_a_10_s_23_b_0():  # tests 30 & 34
    """Full amount taken from small when big is 0."""
    assert solution.fruit_order(23, 0, 10) == 10


def test_fruit_order_a_7_s_6_b_0():  # test 31
    """Can't take amount."""
    assert solution.fruit_order(6, 0, 7) == -1


def test_fruit_order_a_5_taken_s():  # test 32
    """Amount taken from smalls."""
    assert solution.fruit_order(5, 0, 5) == 5


def test_fruit_order_a_2_s_1_b_0():  # test 33
    """Can't take amount. Not enough smalls."""
    assert solution.fruit_order(1, 0, 2) == -1


def test_fruit_order_big_amounts_to_test_for_loops():  # tests 35 & 44
    """Big amounts to test for loops."""
    assert solution.fruit_order(123456789, 197530864, 1000000000) == 12345680


def test_fruit_order_a_6_taken_s_b():  # test 36
    """Amount taken from smalls and big."""
    assert solution.fruit_order(1, 1, 6) == 1


def test_fruit_order_a_1_taken_s():  # test 37
    """Amount taken from smalls."""
    assert solution.fruit_order(1, 2, 1) == 1


def test_fruit_order_a_5_taken_b():  # test 38
    """Can't take amount from bigs."""
    assert solution.fruit_order(1, 1, 5) == 0


def test_fruit_order_loop():  # test 39
    """Loop 0-9."""
    for i in range(10):
        assert solution.fruit_order(i, i, i) == i % 5


def test_fruit_order_a_26_s_6_b_2():  # test 40 & 42
    """Can't take amount. Not enough big and small."""
    assert solution.fruit_order(6, 2, 26) == -1  # -> -1


def test_fruit_order_a_4_s_3_b_1():  # test 41
    """Can't take amount from big nor small."""
    assert solution.fruit_order(3, 1, 4) == -1


def test_fruit_order_a_519_s_3_b_104():  # test 43
    """Can't take amount."""
    assert solution.fruit_order(3, 104, 519) == -1

# Tests 21 - 44 (21/24) passed
