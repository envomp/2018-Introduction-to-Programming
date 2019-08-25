"""PR15 - Investigation. """


class Suspect:
    """Suspect"""

    def __init__(self, first_name, surname, gender, weight, height, street, rating):
        """Initialize the suspect"""
        self.first_name = first_name
        self.surname = surname
        self.gender = gender
        self.weight = weight
        self.height = height
        self.street = street
        self.rating = rating

    def __repr__(self):
        """Suspect object representation."""
        return self.first_name + " " + self.surname


def filter_list_by_street(suspect_list, street_name):
    """
    Return list of suspects who live on the given street.

    :param suspect_list: list of Suspect objects
    :param street_name: string
    :return:list of suspects who live on the given street
    """


def filter_list_by_gender(suspect_list, gender):
    """
    Return list of suspects of given gender or whose gender is "Undefined".

    :param suspect_list: list of Suspect objects
    :param gender: string "Felmale" or "Male"
    :return: list of suspects of given gender or whose gender is "Undefined"
    """


def filer_list_by_age(suspect_list, bottom_age, upper_age):
    """
    Filter out suspects who are younger than the bottom_age and older than the upper_age.

    :param suspect_list: list of Suspect objects
    :param bottom_age: int age
    :param upper_age: int age
    :return:
    """


def sort_by_name_length(suspect_list):
    """
    Sort list of suspects by the length of a suspects full name in descending order.

    :param suspect_list: list of Suspect objects
    :return: sorted list of suspects
    """


def filter_by_bmi(suspect_list):
    """
    Get all the suspects with normal complexion (bmi between 18.5 and 23). BMI = weight(kg)/ height^2(m).

    :param suspect_list: list of Suspect objects
    :return: lisgt of suspects with normal complexion
    """


def filter_by_initials(suspect_list, initials):
    """
    Get all the suspects with given initials.

    :param suspect_list: list of Suspect objects
    :param initials: string, example: "A.H."
    :return: list of suspects with given initials
    """


def increase_rating(suspect_list):
    """
    For each of the remaining suspects increase rating by 20%.

    :param suspect_list: list of Suspect objects
    :return: suspects list with updated rating
    """


def get_suspects_with_highest_rating(suspect_list):
    """
    Return list of suspects with highest rating.
    :param suspect_list:
    :return: list of suspects with highest rating
    """
