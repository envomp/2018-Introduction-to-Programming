import pytest
from pr04_filter import filter_vowels, longest_filtered_word, sort_list


@pytest.mark.timeout(1.0)
def test_filter_vowels_simple():
    assert filter_vowels("tallinn") == "tllnn"
    assert filter_vowels("hello") == "hll"


@pytest.mark.timeout(1.0)
def test_filter_vowels_empty_string():
    assert filter_vowels("") == ""


@pytest.mark.timeout(1.0)
def test_filter_vowels_uppercase():
    assert filter_vowels("ARaBiCa") == "RBC"
    assert filter_vowels("HeLLo") == "HLL"
    assert filter_vowels("MaCCHiaTo") == "MCCHT"


@pytest.mark.timeout(1.0)
def test_filter_vowels_mixed_letters():
    assert filter_vowels("SpoRt") == "SpRt"
    assert filter_vowels("MoNeyBaLl") == "MNyBLl"


@pytest.mark.timeout(1.0)
def test_longest_filtered_word():
    assert longest_filtered_word(["Bunny", "Tiger", "Bear", "Snake"]) == "Bnny"


@pytest.mark.timeout(1.0)
def test_longest_filtered_word_first_in_order():
    assert longest_filtered_word(["Macchiato", "Mochaccino", "Affogato", "Espresso", "Cappuccino"]) == "Mchccn"


@pytest.mark.timeout(1.0)
def test_longest_filtered_word_one_empty_string():
    assert longest_filtered_word([""]) == ""


@pytest.mark.timeout(1.0)
def test_longest_filtered_word_important_order():
    assert longest_filtered_word(["Macchiato", "Mochaccino", "Affogato", "Espresso", "Cappuccino"]) == "Mchccn"


@pytest.mark.timeout(1.0)
def test_sort_list():
    assert sort_list(["Bunny", "Tiger", "Bear", "Snake"]) == ["Bnny", "Tgr", "Snk", "Br"]
    assert sort_list(["Macchiato", "Mochaccino", "Affogato", "Espresso", "Cappuccino"]) == ["Mchccn", "Cppccn", "Mccht", "sprss", "ffgt"]


@pytest.mark.timeout(1.0)
def test_sort_list_empty_list():
    assert sort_list([]) == []
