# -*- coding: utf-8 -*-
"""Check if given ID code is valid."""


def is_valid_year_number(year_number: int) -> bool:
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    return True if 0 <= year_number <= 99 else False


def is_valid_month_number(month_number: int) -> bool:
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    return True if 0 < month_number < 13 else False


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """
    Check if given value is correct for day number in ID code.

    :param gender_number: int
    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    full_year = get_full_year(gender_number, year_number)

    if full_year is False:
        return False

    if day_number > 31 or day_number < 1:
        return False

    if month_number > 12 or month_number < 1:
        return False
    else:
        if month_number == 2:
            if is_leap_year(year_number):
                return True if day_number <= 29 else False
            else:
                return True if day_number <= 28 else False
        else:
            return True if day_number <= days_in_month[month_number - 1] else False


def is_valid_gender_number(gender_number: int) -> bool:
    """
    Check if given value is correct for gender number in ID code.

    :param gender_number: int
    :return: boolean
    """
    return True if 0 < gender_number < 7 else False


def is_valid_birth_number(birth_number: int) -> bool:
    """
    Check if given value is correct for birth number in ID code.

    :param birth_number: int
    :return: boolean
    """
    return True if 0 < birth_number <= 999 else False


def is_valid_control_number(id_code: str) -> bool:
    """
    Check if given value is correct for control number in ID code.

    :param id_code: string
    :return: boolean
    """
    if len(id_code) < 11:
        return False

    multipliers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    multipliers_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    control_1 = 0
    control_2 = 0

    for pos in range(10):
        control_1 += int(id_code[pos]) * multipliers_1[pos]
        control_2 += int(id_code[pos]) * multipliers_2[pos]

    control_1 = control_1 % 11
    control_2 = control_2 % 11

    if control_1 != 10:
        number = control_1
    elif control_2 != 10:
        number = control_2
    else:
        number = 0

    return True if int(id_code[10]) == number else False


def is_leap_year(year_number: int) -> bool:
    """
    Check if given year is a leap year.

    :param year_number: int
    :return: boolean
    """
    if (year_number % 4) == 0:
        if (year_number % 100) == 0:
            if (year_number % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def get_gender(gender_number: int) -> str:
    """
    Define the gender according to the number from ID code.

    :param gender_number: int
    :return: str
    """
    if is_valid_gender_number(gender_number):
        if gender_number % 2:
            return "male"
        else:
            return "female"
    else:
        return False


def get_full_year(gender_number: int, year_number: int) -> int:
    """
    Define the 4-digit year when given person was born.

    Person gender and year numbers from ID code must help.
    Given year has only two last digits.
    :param gender_number: int
    :param year_number: int
    :return: int
    """
    if is_valid_gender_number(gender_number):
        if gender_number < 3:
            return 1800 + year_number
        elif 2 < gender_number < 5:
            return 1900 + year_number
        else:
            return 2000 + year_number
    else:
        return False


def get_birth_place(birth_number: int) -> str:
    """
    Find the place where the person was born.

    Possible locations are following: Kuressaare, Tartu, Tallinn, Kohtla-Järve, Narva, Pärnu,
    Paide, Rakvere, Valga, Viljandi, Võru and undefined. Lastly if the number is incorrect the function must return
    the following 'Wrong input!'
    :param birth_number: int
    :return: str
    """
    birth_place = {
        range(1, 11): "Kuressaare",
        range(11, 21): "Tartu",
        range(21, 221): "Tallinn",
        range(221, 271): "Kohtla-Järve",
        range(271, 371): "Tartu",
        range(371, 421): "Narva",
        range(421, 471): "Pärnu",
        range(471, 491): "Tallinn",
        range(491, 521): "Paide",
        range(521, 571): "Rakvere",
        range(571, 601): "Valga",
        range(601, 651): "Viljandi",
        range(651, 711): "Võru",
        range(711, 1000): "undefined"
    }

    if not is_valid_birth_number(birth_number):
        return ("Wrong input!")

    for number, city in birth_place.items():
        if birth_number in number:
            return city


def get_data_from_id(id_code: str) -> str:
    """
    Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a <gender> born on <DD.MM.YYYY> in <location>.
    :param id_code: str
    :return: str
    """
    if is_id_valid(id_code):
        return f"This is a {get_gender(int(id_code[0]))} born on {id_code[5:7]}.{id_code[3:5]}." \
               f"{get_full_year(int(id_code[0]), int(id_code[1:3]))} in {get_birth_place(int(id_code[7:10]))}."
    else:
        return "Given invalid ID code!"


def is_id_valid(id_code: str) -> bool:
    """
    Check if given ID code is valid and return the result (True or False).

    Complete other functions before starting to code this one.
    You should use the functions you wrote before in this function.
    :param id_code: str
    :return: boolean
    """
    if len(id_code) > 11 or len(id_code) < 11 or not id_code.isdigit():
        return False

    if not is_valid_gender_number(int(id_code[0])):
        return False

    if not is_valid_year_number(int(id_code[1:3])):
        return False

    if not is_valid_month_number(int(id_code[3:5])):
        return False

    if not is_valid_day_number(int(id_code[0]), get_full_year(int(id_code[0]), int(id_code[1:3])),
                               int(id_code[3:5]), int(id_code[5:7])):
        return False

    if not is_valid_birth_number(int(id_code[7:10])):
        return False

    return is_valid_control_number(id_code)


if __name__ == '__main__':
    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False
    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> true
    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False
    print("\nDay number:")
    print(is_valid_day_number(4, 5, 12, 25))  # -> True
    print(is_valid_day_number(3, 10, 8, 32))  # -> False
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False
    print("\nFebruary check:")
    print(
        is_valid_day_number(4, 96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(is_valid_day_number(4, 99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(is_valid_day_number(4, 8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(is_valid_day_number(4, 22, 4, 31))  # -> False (April contains max 30 days)
    print(is_valid_day_number(4, 18, 10, 31))  # -> True
    print(is_valid_day_number(4, 15, 9, 31))  # -> False (September contains max 30 days)
    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True
    print("\nControl number:")
    print(is_valid_control_number("49808270244"))  # -> True
    print(is_valid_control_number("60109200187"))  # -> False, it must be 6

    print("\nFull message:")
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998 in Tallinn."
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    # Comment these back in if you have completed other functions.
    print("\nChecking where the person was born")

    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"

    print("\nOverall ID check::")
    print(is_id_valid("49808270244"))  # -> True
    print(is_id_valid("12345678901"))  # -> False
    print("\nTest now your own ID code:")
    personal_id = input()  # type your own id in command prompt
    print(is_id_valid(personal_id))  # -> True
