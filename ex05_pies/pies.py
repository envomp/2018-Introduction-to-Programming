"""Ex05_pies solved."""
import csv


def get_competitors_list(filename) -> list:
    """
    Get the names of all registered competitors.

    :param filename: is the path to the file with the names of competitors.
    :return: a list containing the names of competitors.
    """
    pass


def get_results_dict(filename) -> dict:
    """
    Get the results and store them in the dictionary.

    Results are following the format 'Firstname Lastname - result'.
    You have to return a dict, where the names of the competitors
    are keys and the results are values.

    :param filename: is the path to the file with the results.
    :return: a dict containing names as keys and results as values.
    """
    pass


def competitors_filter(competitors_list: str, results: str) -> dict:
    """
    Filter out all illegal competitors.

    Illegal competitor is the one, whose name is not in the competitors list.
    You have to return a results dict, which doesn't contain illegal competitors results.
    You should use the methods defined above.

    :param competitors_list: is the path to the file with the names of competitors.
    :param results: is the path to the file with the results.
    :return: a dict with correct results.
    """
    pass


def sort_results(competitors_list: list, results: dict) -> dict:
    """
    Sort the filtered results dictionary.

    In order to find the winner you have to sort the results.
    The more pies the competitor has eaten, the better place they get.
    If there are multiple competitors with the same results, the better place
    goes to the one, who is on the higher place in the names list.

    :param competitors_list: is the list of the registered competitors.
    :param results: is the filtered results dictionary.
    :return: a sorted results dictionary.
    """
    pass


def announce_winner(results: dict) -> str:
    """
    Announce the winner of the competition.

    You have to return a string following this format (without curly brackets):
    'The winner of the "Pie Eating Competition" is {name} with {result} pies eaten.'

    :param results: is the filtered results dictionary.
    :return: a correct string.
    """
    pass


def write_results_csv(competitors_list: str, results: str, file_to_write) -> None:
    """
    Write the results to csv file.

    The csv file must contain three columns:
    1. Place;
    2. Name;
    3. Result.

    :param competitors_list: is the path to the file with the names of competitors.
    :param results: is the path to the file with the results.
    :param file_to_write: is the name of the csv file.
    :return: None
    """
    pass

# Some examples:
if __name__ == '__main__':
    pass
