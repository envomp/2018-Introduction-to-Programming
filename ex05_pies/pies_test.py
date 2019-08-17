"""Tests for ex05_pies."""
import pytest
from pies_solved import *


def _get_illegal_competitors(competitors: str, results: str) -> list:
    names = open(competitors).read()
    results = [line.strip().split(' - ')[0] for line in open(results).readlines()]
    return [n for n in results if n not in names]


@pytest.mark.timeout(1.0)
def test_get_competitors_list_correct_length():
    """Check the length of the competitors list."""
    assert len(get_competitors_list('test_files/test_competitors1.txt')) == 50
    assert len(get_competitors_list('test_files/test_competitors2.txt')) == 20


@pytest.mark.timeout(1.0)
def test_get_results_dict_correct_length():
    """Check the length of the results dictionary."""
    assert len(get_results_dict('test_files/test_results1.txt')) == 63
    assert len(get_results_dict('test_files/test_results2.txt')) == 27


@pytest.mark.timeout(1.0)
def test_competitors_filter_correct_length():
    """Check the length of the filtered results dictionary."""
    assert len(competitors_filter('test_files/test_competitors1.txt', 'test_files/test_results1.txt')) == 50
    assert len(competitors_filter('test_files/test_competitors2.txt', 'test_files/test_results2.txt')) == 20


@pytest.mark.timeout(1.0)
@pytest.mark.parametrize('competitor', _get_illegal_competitors('test_files/test_competitors1.txt',
                                                                'test_files/test_results1.txt'))
def test_competitors_filter_remove_illegal_competitors_1(competitor):
    dict_ = competitors_filter('test_files/test_competitors1.txt', 'test_files/test_results1.txt')
    assert competitor not in dict_


@pytest.mark.timeout(1.0)
@pytest.mark.parametrize('competitor', _get_illegal_competitors('test_files/test_competitors2.txt',
                                                                'test_files/test_results2.txt'))
def test_competitors_filter_remove_illegal_competitors_2(competitor):
    dict_ = competitors_filter('test_files/test_competitors2.txt', 'test_files/test_results2.txt')
    assert competitor not in dict_
