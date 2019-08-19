"""Tests for ex05_pies."""
import pytest
import random
from pies_solved import *  # TODO: Change import to 'pies'.


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
    keys = random.choices(list(expected.keys()), k=random.randint(min_k, max_k))
    for k in keys:
        assert actual[k] == expected[k]


@pytest.mark.timeout(1.0)
@pytest.mark.parametrize('competitor', ['Suzanne Vosburgh', 'Minh Buzbee', 'Hui Holly', 'Elmo Maya', 'Faye Muma'])
def test_get_results_dict_result_for_certain_competitor_1(competitor: str):
    """Check whether the result is correct for certain competitor."""
    actual = get_results_dict(RESULTS_1)
    expected = _get_results(RESULTS_1)
    assert actual[competitor] == expected[competitor]


@pytest.mark.timeout(1.0)
@pytest.mark.parametrize('competitor', ['Retha Cooperman', 'Alfreda Lafave', 'Frederic Woods', 'Fredric Cronin'])
def test_get_results_dict_results_for_certain_competitor_2(competitor: str):
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


def _get_illegal_competitors(competitors: str, results: str) -> list:
    """
    Get illegal competitors for tests.

    :param competitors: is the path to the test_competitorsX.txt.
    :param results: is path to the test_resultsX.txt.
    :return: a list with illegal competitors.
    """
    with open(competitors) as c_file, open(results) as r_file:
        names = c_file.read()
        results = [line.strip().split(' - ')[0] for line in r_file.readlines()]
        return [n for n in results if n not in names]


@pytest.mark.timeout(1.0)
@pytest.mark.parametrize('competitor', _get_illegal_competitors(COMPETITORS_1, RESULTS_1))
def test_competitors_filter_remove_illegal_competitors_1(competitor: str):
    """Check whether all illegal competitors have been filtered out correctly."""
    dict_ = competitors_filter(COMPETITORS_1, RESULTS_1)
    assert competitor not in dict_


@pytest.mark.timeout(1.0)
@pytest.mark.parametrize('competitor', _get_illegal_competitors(COMPETITORS_2, RESULTS_2))
def test_competitors_filter_remove_illegal_competitors_2(competitor: str):
    """Check whether all illegal competitors have been filtered out correctly."""
    dict_ = competitors_filter(COMPETITORS_2, RESULTS_2)
    assert competitor not in dict_


competitors_list = [
    'Detra Speirs', 'Suzanne Vosburgh', 'Garland Blann',
    'Amelia Gahagan', 'Quintin Fiorentino', 'Lorean Aldridge'
]
results_dict = {
    'Garland Blann': 15, 'Lorean Aldridge': 3, 'Quintin Fiorentino': 10,
    'Suzanne Vosburgh': 25, 'Detra Speirs': 25, 'Amelia Gahagan': 11
}
results_same = {
    'Quintin Fiorentino': 14, 'Amelia Gahagan': 14, 'Garland Blann': 14,
    'Lorean Aldridge': 14, 'Detra Speirs': 14, 'Suzanne Vosburgh': 14
}


@pytest.mark.timeout(1.0)
def test_sort_results_correct_length():
    """Check the length of the sorted results dictionary."""
    assert len(sort_results(competitors_list, results_dict)) == 6


@pytest.mark.timeout(1.0)
def test_sort_results_descending_order():
    """Check whether the sorted results are in descending order."""
    actual = sort_results(competitors_list, results_dict)
    values = list(actual.values())
    assert all(values[i] >= values[i + 1] for i in range(5))


@pytest.mark.timeout(1.0)
def test_sort_results_competitors_with_same_results():
    """Check whether the competitors with same results are sorted by their place in list."""
    actual = sort_results(competitors_list, results_same)
    expected = {
        'Detra Speirs': 14, 'Suzanne Vosburgh': 14, 'Garland Blann': 14,
        'Amelia Gahagan': 14, 'Quintin Fiorentino': 14, 'Lorean Aldridge': 14
    }
    assert actual == expected


@pytest.mark.timeout(1.0)
def test_announce_winner_correct_format():
    """Check the format of the winner announcement."""
    sorted_ = sort_results(competitors_list, results_dict)
    actual = announce_winner(sorted_)
    expected = "The winner of the \"Pie Eating Competition\" is Detra Speirs with 25 pies eaten."
    assert actual == expected


@pytest.mark.timeout(1.0)
def test_write_results_csv_correct_file():
    # For file from exercise
    with open('actual_results.csv', mode='w+') as actual, \
            open('results_test.csv') as expected:
        write_results_csv('competitors_list.txt', 'results.txt', 'actual_results.csv')
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
