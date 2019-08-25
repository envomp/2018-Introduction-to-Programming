"""Tests for ex03 Id code."""
import pytest
from idcode import check_your_id, check_gender_number, check_born_order,
check_leap_year, check_day_number


def test_from_example_full_id():
    """

    Testing a full id code from the example
    given in the exercise

    :return: True
    """
    assert check_your_id("49808270244") is True


def test_id_code_wrong_numbers():
    """

    Testing a full id code with wrong
    numbers set

    :return: False  
    """
    assert check_your_id("12345678901") is False


def test_id_code_contains_letters():
    """
    Testing case when id code contains letters.

    :return: False
    """
    assert check_your_id("4980827k244") is False
    code = list("49808270244")
    for i in range(10):
        check_code = list(code)
        check_code[i] = 'a'
        assert check_your_id("".join(check_code)) is False


def test_id_code_too_short():
    """

    Testing too short id code

    :return: False
    """
    assert check_your_id("1254") is False


def test_id_code_too_long():
    """

    Testing too short id code

    :return: False
    """
    assert check_your_id("498082702441") is False


def test_id_code_correct():
    """

    Testing a full id code with correct
    numbers and length
    :return: True
    """
    assert check_your_id("60109200186") is True


@pytest.mark.parametrize("gender_number", [0, 1, 2, 5, 7, 8])
def test_from_example_gender_number(gender_number):
    """

    Testing possible wrong and correct digits
    chosen for gender number (from given example)

    :param gender_number: number
    :return: boolean
    """
    if gender_number == 0 or gender_number >= 7:
        assert check_gender_number(gender_number) is False
    else:
        assert check_gender_number(gender_number) is True


def test_year_number_two_digits():
    """

    Testing possible year numbers
    (0...99 -> True)
    (100 -> False)

    :return: boolean
    """
    assert check_year_number_two_digits(80) is True
    assert check_year_number_two_digits(100) is False
    assert check_year_number_two_digits(5) is True
    assert check_year_number_two_digits(0) is True
    assert check_year_number_two_digits(-2) is False
    assert check_year_number_two_digits(-20) is False


possible_months = [i for i in range(16)]


@pytest.mark.parametrize("month_number", possible_months)
def test_month_number(month_number):
    """

    Testing possible month numbers
    (1...12 -> True)
    (0 and 13...15 -> False)

    :param month_number: number
    :return: boolean
    """
    month_number -= 2
    if month_number <= 0 or month_number > 12:
        assert check_month_number(month_number) is False
    else:
        assert check_month_number(month_number) is True


def test_born_order():
    """

    Testing possible born order numbers

    :return: boolean
    """
    assert check_born_order(-1) is False
    assert check_born_order(0) is True
    assert check_born_order(1) is True
    assert check_born_order(872) is True
    assert check_born_order(315) is True
    assert check_born_order(1000) is False
    assert check_born_order(9999) is False
    assert check_born_order(99994) is False


def test_day_number_february_cannot_contain_more_days():
    """

    February cannot contain more days than
    allowed (more than 29)

    :return: False
    """
    assert check_day_number(2096, 2, 30) is False


def test_day_number_february_cannot_contain_29_days_when_not_leap_year():
    """

    February cannot contain 29 days when it is
    not a leap year

    :return: False
    """
    assert check_day_number(1899, 2, 29) is False


def test_day_number_february_contains_29_days_when_leap_year():
    """

    February contains 29 days when it
    is a leap year

    :return: True
    """
    assert check_day_number(2008, 2, 29) is True


months_30_days = [4, 6, 9, 11]


@pytest.mark.parametrize("month_number", months_30_days)
def test_day_number_month_cannot_contain_31_days(month_number):
    """

    Chosen months do not contain 31 days

    :return: False
    """
    assert check_day_number(1922, month_number, 31) is False


@pytest.mark.parametrize("wrong_leap_year", [1800, 1900, 2005, 2023, 2090])
def test_given_year_is_not_leap_year(wrong_leap_year):
    """
    Testing wrong leap year.

    :param wrong_leap_year: int
    :return: boolean
    """
    assert check_leap_year(wrong_leap_year) is False


@pytest.mark.parametrize("correct_leap_year", [1804, 2024, 2020, 1648, 2000])
def test_given_year_is_leap_year(correct_leap_year):
    """
    Testing correct leap year.

    :param correct_leap_year: int
    :return: boolean
    """
    assert check_leap_year(correct_leap_year) is True


def test_control_number_must_be_correct():
    """

    Given control number is correct in
    chosen ID code

    :return: True
    """
    assert check_control_number("49808270244") is True


def test_control_number_correct_second_round():
    """Second set of multipliers is needed."""
    assert check_control_number("51809170123") is True


def test_control_number_must_be_wrong():
    """

    Given control number is wrong in
    chosen ID code

    :return: False
    """
    assert check_control_number("60109200181") is False
    assert check_control_number("60109200182") is False
    assert check_control_number("60109200183") is False
    assert check_control_number("60109200184") is False
    assert check_control_number("60109200185") is False
    assert check_control_number("60109200187") is False
    assert check_control_number("60109200188") is False
    assert check_control_number("60109200189") is False
    assert check_control_number("60109200180") is False


def test_get_full_info_message():
    """

    Checking if the message gives correct
    information according to the template

    :return: string
    """
    assert get_data_from_id(
        "60109200186") == "This is a female born on 20.09.2001"


def test_cannot_get_info_id_is_wrong():
    """

    Cannot collect information from the ID code
    because the code is invalid

    :return: string
    """
    assert get_data_from_id("49808270249") == "Given invalid ID code!"


def test_getting_full_year_number():
    """

    Getting correct 4-digit year number

    :return: int
    """
    assert get_full_year(2, 2) == 1802
    assert get_full_year(3, 95) == 1995
    assert get_full_year(6, 5) == 2005


gender_numbers = [i for i in range(1, 7)]


@pytest.mark.parametrize("gender_number", gender_numbers)
def test_get_correct_gender_from_number(gender_number):
    """

    Checking if the gender number gives correct
    gender

    :param gender_number: number
    :return: string
    """
    if gender_number % 2 == 0:
        assert get_gender(gender_number) == "female"
    else:
        assert get_gender(gender_number) == "male"
