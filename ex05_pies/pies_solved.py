"""Ex05_pies solved."""
import csv


def get_competitors_list(filename: str) -> list:
    """
    Get the names of all registered competitors.

    :param filename: is the path to the file with the names of competitors.
    :return: a list containing the names of competitors.
    """
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def get_results_dict(filename: str) -> dict:
    """
    Get the results and store them in the dictionary.

    Results are following the format 'Firstname Lastname - result'.
    You have to return a dict, where the names of the competitors
    are keys and the results are values.

    :param filename: is the path to the file with the results.
    :return: a dict containing names as keys and results as values.
    """
    with open(filename) as file:
        lines = file.readlines()
        return {k: int(v) for k, v in (line.split(' - ') for line in lines)}


def competitors_filter(path_to_competitors: str, path_to_results: str) -> dict:
    """
    Filter out all illegal competitors.

    Illegal competitor is the one, whose name is not in the registered competitors list.
    You have to return a results dict, which doesn't contain the results of illegal competitors.
    You should use the methods defined above.

    :param path_to_competitors: is the path to the file with the names of competitors.
    :param path_to_results: is the path to the file with the results.
    :return: a dict with correct results.
    """
    comp_list = get_competitors_list(path_to_competitors)
    results_dict = get_results_dict(path_to_results)
    for name in list(results_dict.keys()):
        if name not in comp_list:
            del results_dict[name]
    return results_dict


def sort_results(competitors_list: list, results: dict) -> dict:
    """
    Sort the filtered results dictionary.

    In order to find the winner you have to sort the results.
    Results have to be sorted based on the cakes eaten by the competitors.
    The sorted results must be in a descending order.
    This means that the more cakes the competitor has eaten the better place they get.
    If there are multiple competitors with the same result the better place goes to the
    competitor, whose place in the registered competitors list is higher.
    For example, if Mati and Kati both have 5 pies eaten and Kati is on a higher place
    than Mati in the registered competitors list, then the better place must go to Kati
    (i.e. Kati gets 4th place and mati gets 5th).

    :param competitors_list: is the list of the registered competitors.
    :param results: is the filtered results dictionary.
    :return: a sorted results dictionary.
    """
    by_index = dict(
        sorted(results.items(), key=lambda x: competitors_list.index(x[0])))
    return dict(sorted(by_index.items(), key=lambda x: x[1], reverse=True))


def announce_winner(results: dict) -> str:
    """
    Announce the winner of the competition.

    You have to return a string following this format (without curly brackets):
    'The winner of the "Pie Eating Competition" is {name} with {result} pies eaten.'

    :param results: is the filtered and sorted results dictionary.
    :return: a correct string.
    """
    name, result = list(results.items())[0]
    return f"The winner of the \"Pie Eating Competition\" is {name} with {result} pies eaten."


def write_results_csv(path_to_competitors: str, path_to_results: str, file_to_write: str) -> None:
    """
    Write the results to csv file.

    The csv file must contain three columns:
    1. Place;
    2. Name;
    3. Result.

    :param path_to_competitors: is the path to the file with the names of competitors.
    :param path_to_results: is the path to the file with the results.
    :param file_to_write: is the name of the csv file.
    :return: None
    """
    with open(file_to_write, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        place, name, result = 'Place', 'Name', 'Result'
        writer.writerow([place, name, result])

        competitors = get_competitors_list(path_to_competitors)
        filtered_dict = competitors_filter(path_to_competitors, path_to_results)
        sorted_dict = sort_results(competitors, filtered_dict)

        for index, item in enumerate(sorted_dict.items(), start=1):
            writer.writerow([index, item[0], item[1]])
