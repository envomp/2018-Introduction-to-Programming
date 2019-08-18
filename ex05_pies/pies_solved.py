"""Ex05_pies solved."""
import csv


def get_competitors_list(filename) -> list:
    """
    Get the names of all registered competitors.

    :param filename: is the path to the file with the names of competitors.
    :return: a list containing the names of competitors.
    """
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def get_results_dict(filename) -> dict:
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
    comp_list = get_competitors_list(competitors_list)
    results_dict = get_results_dict(results)
    for name in list(results_dict.keys()):
        if name not in comp_list:
            del results_dict[name]
    return results_dict


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
    return dict(sorted(results.items(), key=lambda x: (x[1], competitors_list.index(x[0])), reverse=True))


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
    with open(file_to_write, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        place, name, result = 'Place', 'Name', 'Result'
        writer.writerow([place, name, result])

        filtered_dict = competitors_filter(competitors_list, results)
        competitors = get_competitors_list(competitors_list)
        sorted_dict = sort_results(competitors, filtered_dict)

        for index, name, result in enumerate(sorted_dict.items(), start=1):
            writer.writerow([index, name, result])


if __name__ == '__main__':
    pass
