"""PR15 - Investigation. """


class Suspect:
    """Suspect"""

    def __init__(self, first_name: str, surname: str, gender: str, age: int, weight: int, height: int, street: str,
                 rating: int):
        """Initialize the suspect"""
        self.first_name = first_name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.street = street
        self.rating = rating

    def increase_rating(self, points_to_add: int):
        """
        Increase rating by the given amount of points

        :param points_to_add: amount of points to add
        :return: None
        """
        self.rating += points_to_add

    def __repr__(self):
        """Suspect object representation."""
        return self.first_name


def filter_list_by_street(suspect_list: list, street_name: str) -> list:
    """
    Return list of suspects who live on the given street.

    :param suspect_list: list of Suspect objects
    :param street_name: string
    :return:list of suspects who live on the given street
    """


def filter_list_by_gender(suspect_list: list, gender: str) -> list:
    """
    Return list of suspects of given gender or whose gender is "Undefined".

    :param suspect_list: list of Suspect objects
    :param gender: string "Felmale" or "Male"
    :return: list of suspects of given gender or whose gender is "Undefined"
    """


def filer_list_by_age(suspect_list: list, bottom_age: int, upper_age: int) -> list:
    """
    Filter out suspects who are younger than the bottom_age and older than the upper_age.

    :param suspect_list: list of Suspect objects
    :param bottom_age: int age
    :param upper_age: int age
    :return: list of suspects with appropriate age
    """


def sort_by_name_length(suspect_list: list) -> list:
    """
    Sort list of suspects by the length of a suspects full name in descending order.

    :param suspect_list: list of Suspect objects
    :return: sorted list of suspects
    """


def filter_list_by_bmi(suspect_list: list) -> list:
    """
    Get all the suspects with normal complexion (bmi between 18.5 and 25). BMI = weight(kg)/ height^2(m).

    :param suspect_list: list of Suspect objects
    :return: list of suspects with normal complexion
    """


def increase_rating(suspect_list: list):
    """
    For each of the remaining suspects add 2 to rating.

    :param suspect_list: list of Suspect objects
    :return: None
    """


def filter_list_by_initials(suspect_list: list, initials: str) -> list:
    """
    Get all the suspects with given initials.

    :param suspect_list: list of Suspect objects
    :param initials: string, example: Ago Luberg = "A.L."
    :return: list of suspects with given initials
    """


def get_suspects_with_highest_rating(suspect_list: list) -> Suspect:
    """
    Return suspect with highest rating.
    :param suspect_list: list of Suspect objects
    :return: suspect with the highest rating
    """


if __name__ == "__main__":
    chrysa = Suspect("Chrysa", "Bygraves", "Female", 27, 97, 173, "Quiet", 4)
    norbie = Suspect("Norbie", "Lanyon", "Male", 23, 83, 194, "Criminal", 5)
    davida = Suspect("Davida", "Yate", "Female", 57, 135, 180, "Corrupted", 10)
    ed = Suspect("Ed", "Scini", "Female", 51, 118, 181, "Corrupted", 9)
    rand = Suspect("Rand", "Worcs", "Male", 39, 56, 169, "Criminal", 8)
    orlando = Suspect("Orlando", "Kienlein", "Male", 27, 72, 180, "Criminal", 4)
    philip = Suspect("Phillip", "Cakersgill", "Male", 29, 63, 169, "Criminal", 8)
    pavia = Suspect("Pavia", "Craft", "Male", 22, 64, 181, "Criminal", 2)
    tobit = Suspect("Tobit", "Messom", "Female", 61, 140, 177, "Corrupted", 7)
    eda = Suspect("Eda", "Merkle", "Female", 23, 55, 176, "Criminal", 4)
    lawrence = Suspect("Lawrence", "Lethebridge", "Female", 37, 148, 177, "Criminal", 7)
    randi = Suspect("Randi", "Codlin", "Male", 29, 76, 165, "Criminal", 2)
    jack = Suspect("Jack", "Duffan", "Male", 20, 68, 176, "Criminal", 3)

    suspects = [chrysa, norbie, davida, ed, rand, orlando, philip, pavia, tobit, eda, lawrence, randi, jack]

    filtered_by_street = filter_list_by_street(suspects, "Criminal")
    print(filtered_by_street)  # [Norbie, Rand, Orlando, Phillip, Pavia, Eda, Lawrence, Randi, Jack]

    filtered_by_gender = filter_list_by_gender(filtered_by_street, "Male")
    print(filtered_by_gender)  # [Norbie, Rand, Orlando, Phillip, Pavia, Randi, Jack]

    filtered_by_age = filer_list_by_age(filtered_by_gender, 18, 35)
    print(filtered_by_age)  # [Norbie, Orlando, Phillip, Pavia, Randi, Jack]

    sorted_by_name_length = sort_by_name_length(filtered_by_age)
    print(sorted_by_name_length)  # [Phillip, Orlando, Norbie, Randi, Pavia, Jack]

    filtered_by_bmi = filter_list_by_bmi(sorted_by_name_length)
    print(filtered_by_bmi)  # [Phillip, Orlando, Norbie, Pavia, Jack]

    increase_rating(filtered_by_bmi)
    print([x.rating for x in filtered_by_bmi])  # [10, 6, 7, 4, 5]

    filtered_by_initials = filter_list_by_initials(filtered_by_bmi, "P.C.")
    print(filtered_by_initials)  # [Phillip, Pavia]

    possible_killer = get_suspects_with_highest_rating(filtered_by_initials)
    print(possible_killer)  # Phillip
