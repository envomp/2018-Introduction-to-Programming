"""PR15 - anonymous."""
from functools import reduce


class Person:
    """Person."""

    def __init__(self, first_name: str, surname: str, gender: str, age: int, weight: int, height: int, rating: int):
        """Initialize the Person object."""
        self.first_name = first_name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.rating = rating

    def increase_rating(self, number: int):
        """
        Multiply rating by the given number.

        :param number: multiplier
        :return: rating
        """
        self.rating *= number
        return self.rating

    def __repr__(self):
        """Person object representation."""
        return self.first_name


def find_the_tallest_person(person_list: list) -> Person:
    """
    Find the tallest person. If multiple people are of the same height return the first one on the list.

    :param person_list: input list
    :return: Person object
    """
    return max(person_list, key=lambda person: person.height)


def filter_list_by_gender(person_list: list, gender: str) -> list:
    """
    Return list of people who identify as gender or whose gender is "Undefined".

    :param person_list: input list
    :param gender: gender
    :return: list of people
    """
    return list(filter(lambda person: person.gender == gender or person.gender == "Undefined", person_list))


def filter_list_by_age(person_list: list, bottom_age: int, upper_age: int) -> list:
    """
    Filter out people who are younger than bottom_age and older than upper_age.

    :param person_list: input list
    :param bottom_age:
    :param upper_age:
    :return: list of people
    """
    return list(filter(lambda person: bottom_age <= person.age <= upper_age, person_list))


def filter_list_by_bmi(person_list: list) -> list:
    """
    Get all the people with normal complexion (bmi between 18.5 and 25). BMI = weight(kg)/ height^2(m).

    :param person_list: input list
    :return: list of people
    """
    return list(filter(lambda person: 18.5 <= person.weight / (person.height / 100)**2 <= 25, person_list))


def get_the_rating_product(person_list: list) -> int:
    """
    Return the result of multiplication of all the ratings.

    :param person_list: input list
    :return: product
    """
    return reduce((lambda x, y: x * y), map(lambda person: person.rating, person_list))


def sort_by_name_length(person_list: list) -> list:
    """
    Sort list of people by the length of their full name in descending order. Original list must remain unchanged.

    :param person_list: input list
    :return: sorted list of people
    """
    return sorted(person_list, key=lambda person: len(person.first_name + " " + person.surname), reverse=True)


def get_list_of_increased_ratings(person_list: list, number: int) -> list:
    """
    Return list of ratings of all people multiplied by the given number.

    :param number: multiplier
    :param person_list: input list
    :return: list of ratings
    """
    return list(map(lambda person: person.increase_rating(number), person_list))


def get_people_with_the_lowest_rating(person_list: list) -> list:
    """
    Return list of people with the lowest rating.

    :param person_list: input list
    :return: list of people
    """
    return list(filter(lambda person: person.rating <= min(map(lambda person: person.rating, person_list)), person_list))


if __name__ == "__main__":
    chrysa = Person("Chrysa", "Bygraves", "Helicopter", 27, 97, 173, 4)
    norbie = Person("Norbie", "Lanyon", "Unicorn", 23, 83, 194, 5)
    rand = Person("Rand", "Worcs", "Male", 39, 56, 169, 8)
    pavia = Person("Pavia", "Craft", "Unicorn", 22, 64, 181, 2)
    tobit = Person("Tobit", "Messom", "Female", 61, 140, 177, 7)
    eda = Person("Eda", "Merkle", "Undefined", 23, 55, 176, 2)

    list_of_people = [chrysa, norbie, rand, pavia, tobit, eda]
    print(find_the_tallest_person(list_of_people))  # Norbie
    print(filter_list_by_gender(list_of_people, "Unicorn"))  # [Norbie, Pavia, Eda]
    print(filter_list_by_age(list_of_people, 18, 35))  # [Chrysa, Norbie, Pavia, Eda]
    print(filter_list_by_bmi(list_of_people))  # [Norbie, Rand, Pavia]
    print(get_the_rating_product(list_of_people))  # 4480
    print(sort_by_name_length(list_of_people))  # [Chrysa, Norbie, Tobit, Pavia, Rand, Eda]
    print(get_list_of_increased_ratings(list_of_people, 2))  # [8, 10, 16, 4, 14, 4]
    print(get_people_with_the_lowest_rating(list_of_people))  # [Pavia, Eda]
