"""Tests for ex05_pies."""
import pytest
import random
from pies import get_competitors_list, get_results_dict, competitors_filter,\
    sort_results, announce_winner, write_results_csv


COMPETITORS_1 = 'test_files/test_competitors1.txt'
COMPETITORS_2 = 'test_files/test_competitors2.txt'
RESULTS_1 = 'test_files/test_results1.txt'
RESULTS_2 = 'test_files/test_results2.txt'


@pytest.mark.timeout(1.0)
def test_get_competitors_list_correct_length():
    """Check the length of the competitors list."""
    assert len(get_competitors_list(COMPETITORS_1)) == 20
    assert len(get_competitors_list(COMPETITORS_2)) == 50


@pytest.mark.timeout(1.0)
def test_get_results_dict_correct_length():
    """Check the length of the results dictionary."""
    assert len(get_results_dict(RESULTS_1)) == 27
    assert len(get_results_dict(RESULTS_2)) == 63


def _get_results(path_to_file: str) -> dict:
    """
    Get the results dictionary for tests.

    :param path_to_file: is path to the test_resultsX.txt.
    :return: results dictionary.
    """
    with open(path_to_file) as file:
        lines = file.readlines()
        return {k: int(v) for k, v in (line.split(' - ') for line in lines)}


def _test_results_for_random_competitors(path_to_file: str, min_k: int, max_k: int):
    """
    Check whether the result is correct for random competitor.

    :param path_to_file: is path to the test_resultsX.txt.
    :param min_k: is the minimum keys length.
    :param max_k: is the maximum keys length
    :return: None
    """
    actual = get_results_dict(path_to_file)
    expected = _get_results(path_to_file)
    keys = random.choices(list(expected.keys()),
                          k=random.randint(min_k, max_k))
    for k in keys:
        assert actual[k] == expected[k]


@pytest.mark.timeout(1.0)
@pytest.mark.parametrize('competitor', ['Suzanne Vosburgh', 'Minh Buzbee', 'Hui Holly', 'Elmo Maya', 'Faye Muma'])
def test_get_results_dict_result_for_certain_competitors_1(competitor: str):
    """Check whether the result is correct for certain competitor."""
    actual = get_results_dict(RESULTS_1)
    expected = _get_results(RESULTS_1)
    assert actual[competitor] == expected[competitor]


@pytest.mark.timeout(1.0)
@pytest.mark.parametrize('competitor', ['Retha Cooperman', 'Alfreda Lafave', 'Frederic Woods', 'Fredric Cronin'])
def test_get_results_dict_results_for_certain_competitors_2(competitor: str):
    """Check whether the result is correct for certain competitor."""
    actual = get_results_dict(RESULTS_2)
    expected = _get_results(RESULTS_2)
    assert actual[competitor] == expected[competitor]


@pytest.mark.timeout(2.0)
def test_get_results_dict_results_for_random_competitors():
    """Check whether the result is correct for random competitor."""
    n = random.randint(0, 1)

    # For test_results1.txt
    if n == 0:
        _test_results_for_random_competitors(RESULTS_1, 5, 27)

    # For test_results2.txt
    else:
        _test_results_for_random_competitors(RESULTS_2, 10, 63)


@pytest.mark.timeout(1.0)
def test_competitors_filter_correct_length():
    """Check the length of the filtered results dictionary."""
    assert len(competitors_filter(COMPETITORS_1, RESULTS_1)) == 20
    assert len(competitors_filter(COMPETITORS_2, RESULTS_2)) == 50


def _get_illegal_competitors(path_to_competitors: str, path_to_results: str) -> list:
    """
    Get illegal competitors for tests.

    :param path_to_competitors: is the path to the test_competitorsX.txt.
    :param path_to_results: is the path to the test_resultsX.txt.
    :return: a list with illegal competitors.
    """
    with open(path_to_competitors) as c_file, \
            open(path_to_results) as r_file:
        names = c_file.read()
        results = [line.strip().split(' - ')[0] for line in r_file.readlines()]
        return [n for n in results if n not in names]


@pytest.mark.timeout(1.0)
@pytest.mark.parametrize('competitor', _get_illegal_competitors(COMPETITORS_1, RESULTS_1))
def test_competitors_filter_remove_illegal_competitors_1(competitor: str):
    """Check whether all illegal competitors have been filtered out correctly."""
    filtered = competitors_filter(COMPETITORS_1, RESULTS_1)
    assert competitor not in filtered


@pytest.mark.timeout(1.0)
@pytest.mark.parametrize('competitor', _get_illegal_competitors(COMPETITORS_2, RESULTS_2))
def test_competitors_filter_remove_illegal_competitors_2(competitor: str):
    """Check whether all illegal competitors have been filtered out correctly."""
    filtered = competitors_filter(COMPETITORS_2, RESULTS_2)
    assert competitor not in filtered


def _get_data_for_sorting(path_to_list: str, path_to_results: str) -> tuple:
    """
    Get the needed data to test sorting functionality.

    :param path_to_list: is the path to the test_competitorsX.txt.
    :param path_to_results: is the path to the test_resultsX.txt.
    """
    competitors = get_competitors_list(path_to_list)
    results = competitors_filter(path_to_list, path_to_results)
    return competitors, results


def _test_sorting_order(competitors: list, results: dict) -> None:
    """
    Check whether the sorted results are in correct order.

    :param competitors: is the list of the registered competitors.
    :param results: is the filtered results dictionary.
    :return: None.
    """
    sorted_ = sort_results(competitors, results)
    values = list(sorted_.values())
    assert all(values[i] >= values[i + 1] for i in range(len(values) - 1))


def _test_places_for_certain_competitors(path_to_list: str, path_to_results: str, competitor: str, place: int) -> None:
    """
    Check the places for certain competitors.

    :param path_to_list: is the path to the test_competitorsX.txt.
    :param path_to_results: is the path to the test_resultsX.txt.
    :param competitor: is the name of the competitor.
    :param place: is the expected place of the competitor.
    :return: None.
    """
    competitors, results = _get_data_for_sorting(path_to_list, path_to_results)
    sorted_ = sort_results(competitors, results)
    keys = list(sorted_.keys())
    assert keys.index(competitor) + 1 == place


def _test_winner_announcement(competitors: list, results: dict, name: str, result: int) -> None:
    """
    Check the format of the winner announcement.

    :param competitors: is the list of the registered competitors.
    :param results: is the filtered results dictionary.
    :param name: is the name of expected winner.
    :param result: is the result of expected winner.
    :return: None.
    """
    sorted_ = sort_results(competitors, results)
    actual = announce_winner(sorted_)
    expected = f'The winner of the "Pie Eating Competition" is {name} with {result} pies eaten.'
    assert actual == expected


@pytest.mark.timeout(1.0)
def test_sort_results_correct_length():
    """Check the length of the sorted results dictionary."""
    competitors1, results1 = _get_data_for_sorting(COMPETITORS_1, RESULTS_1)
    competitors2, results2 = _get_data_for_sorting(COMPETITORS_2, RESULTS_2)

    assert len(sort_results(competitors1, results1)) == 20
    assert len(sort_results(competitors2, results2)) == 50


@pytest.mark.timeout(1.0)
def test_sort_results_descending_order():
    """Check whether the sorted results are in descending order."""
    competitors1, results1 = _get_data_for_sorting(COMPETITORS_1, RESULTS_1)
    competitors2, results2 = _get_data_for_sorting(COMPETITORS_2, RESULTS_2)

    _test_sorting_order(competitors1, results1)
    _test_sorting_order(competitors2, results2)


@pytest.mark.timeout(1.0)
@pytest.mark.parametrize(
    'competitor,place',
    [('Audrea Fines', 5), ('Delora Deforest', 11), ('June Ambrosino', 14)]
)
def test_sort_results_places_for_certain_competitors_1(competitor, place):
    """Check the places for certain competitors."""
    _test_places_for_certain_competitors(COMPETITORS_1, RESULTS_1, competitor, place)


@pytest.mark.timeout(1.0)
@pytest.mark.parametrize(
    'competitor,place',
    [('Roger Aylor', 8), ('Suellen Lor', 13), ('Ming Lynam', 34), ('Emory Elms', 39), ('Nery Nagle', 48)]
)
def test_sort_results_places_for_certain_competitors_2(competitor, place):
    """Check the places for certain competitors."""
    _test_places_for_certain_competitors(COMPETITORS_2, RESULTS_2, competitor, place)


@pytest.mark.timeout(1.0)
def test_sort_results_competitors_with_same_results():
    """Check whether the competitors with same results are sorted by their place in list."""
    competitors_list = [
        'Detra Speirs', 'Suzanne Vosburgh', 'Garland Blann',
        'Amelia Gahagan', 'Quintin Fiorentino', 'Lorean Aldridge'
    ]
    same_results = {
        'Quintin Fiorentino': 14, 'Amelia Gahagan': 14, 'Garland Blann': 14,
        'Lorean Aldridge': 14, 'Detra Speirs': 14, 'Suzanne Vosburgh': 14
    }
    actual = sort_results(competitors_list, same_results)
    expected = {
        'Detra Speirs': 14, 'Suzanne Vosburgh': 14, 'Garland Blann': 14,
        'Amelia Gahagan': 14, 'Quintin Fiorentino': 14, 'Lorean Aldridge': 14
    }
    assert actual == expected


@pytest.mark.timeout(1.0)
def test_announce_winner_correct_format():
    """Check the format of the winner announcement."""
    competitors1, results1 = _get_data_for_sorting(COMPETITORS_1, RESULTS_1)
    competitors2, results2 = _get_data_for_sorting(COMPETITORS_2, RESULTS_2)

    _test_winner_announcement(competitors1, results1, 'Faye Muma', 15)
    _test_winner_announcement(competitors2, results2, 'Maryetta Delafuente', 23)


@pytest.mark.timeout(1.0)
def test_write_results_csv_correct_file():
    """Check the written results .csv file."""
    # For files from exercise
    with open('actual_results.csv', mode='w+') as actual, \
            open('correct_results.csv') as expected:
        write_results_csv('competitors_list.txt',
                          'results.txt', 'actual_results.csv')
        assert actual.read() == expected.read()

    # For test_competitors1.txt / test_results1.txt
    with open('actual_results1.csv', mode='w+') as actual1, \
            open('test_files/results_test1.csv') as expected1:
        write_results_csv(COMPETITORS_1, RESULTS_1, 'actual_results1.csv')
        assert actual1.read() == expected1.read()

    # For test_competitors2.txt / test_results2.txt
    with open('actual_results2.csv', mode='w+') as actual2, \
            open('test_files/results_test2.csv') as expected2:
        write_results_csv(COMPETITORS_2, RESULTS_2, 'actual_results2.csv')
        assert actual2.read() == expected2.read()
