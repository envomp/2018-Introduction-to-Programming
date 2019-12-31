"""Test magic.py functions."""
import magic
import pytest

wand1 = magic.Wand('Oak', 'Phoenix Feather', 40)
wand2 = magic.Wand('Birch', 'Dragon Heartstring', 10)
wand3 = magic.Wand('Pine', 'Unicorn Hair', 20)
wand4 = magic.Wand('Mapple', 'Veela Hair', 30)
wand5 = magic.Wand('Rowan', 'Thestral Hair', 50)
wand6 = magic.Wand('Oak', 'Unicorn Hair', 40)

wiz1 = magic.Wizard('Ron Weasley', 40, wand1)
wiz2 = magic.Wizard('Hermione Granger', 20, wand2)
wiz3 = magic.Wizard('Neville Longbottom', 35, wand3)
wiz4 = magic.Wizard('Draco Malfoy', 45, wand4)
wiz5 = magic.Wizard('Apolline Delacour', 45, wand5)

school1 = magic.WizardSchool('Beauxbatons Academy of Magic', 10)
school2 = magic.WizardSchool('Durmstrang Institute for Magical Learning', 2)
school3 = magic.WizardSchool('Hogwarts School of Witchcraft and Wizardry', 15)
school4 = magic.WizardSchool('Ilvermorny School of Witchcraft and Wizardry', 25)

house1 = magic.House('Mustang House', 20)
house2 = magic.House('Durmstrang House', 10)


def test_wand_exception():
    """Test that exception is raised for invalid Wand."""
    # Missing Core
    wand_bad = magic.Wand('Oak', '', 40)
    with pytest.raises(Exception) as e:
        assert magic.Wand.is_wand_correct(wand_bad)
    assert str(e.value) == "The wand like that does not exist!"

    # Missing Wood Type
    wand_bad = magic.Wand('', 'Phoenix Feather', 40)
    with pytest.raises(Exception) as e:
        assert magic.Wand.is_wand_correct(wand_bad)
    assert str(e.value) == "The wand like that does not exist!"


def test_is_wand_correct():
    """Test correct Wand."""
    assert magic.Wand.is_wand_correct(wand1) is None


def test_repr_str_wand():
    """Test str representation of Wand."""
    assert str(wand1) == 'Oak Wand with Phoenix Feather core (40)'
    assert repr(wand1) == 'Oak Wand with Phoenix Feather core (40)'


def test_create_wizard_correct_wand():
    """Test create Wizard with correct wand."""
    assert str(magic.Wizard('Ron Weasley', 40, wand1)) == 'Ron Weasley'


def test_exception_create_wizard_incorrect_wand():
    """Test that exception is raised for invalid Wand."""
    wand_bad = magic.Wand('', 'Phoenix Feather', 40)
    with pytest.raises(Exception) as e:
        assert magic.Wizard('Ron Weasley', 40, wand_bad)
    assert str(e.value) == "The wand like that does not exist!"


def test_repr_str_wizard():
    """Test str representation of Wand."""
    assert str(wiz2) == 'Hermione Granger'
    assert repr(wiz2) == 'Hermione Granger 20'


def test_set_wizard_wand_wand_already_set():
    """Test set wizard wand when wand already set."""
    assert wiz3.wand.owner == wiz3
    assert wiz3.wand == wand3
    assert wiz3.set_wand(wand4) is None
    assert wand3.owner is None
    assert wand4.owner == wiz3
    assert wiz3.wand == wand4


def test_create_school():
    """Test create School."""
    assert str(school1) == 'Beauxbatons Academy of Magic'
    assert school1.max_wizards == 10
    assert school1.name == 'Beauxbatons Academy of Magic'
    assert len(school1.wizards) == 0
    assert len(school1.houses) == 0
    assert school1.get_wizards_count() == 0
    assert school1.get_wizards() == []


def test_add_wizard_to_school():
    """Test add wizard to school."""
    assert school1.add_wizard(wiz1) is None
    assert len(school1.wizards) == 1
    assert school1.get_wizards_count() == 1
    assert repr(school1.get_wizards()[0]) == 'Ron Weasley 40'


def test_repr_str_school():
    """Test str representation of WizardSchool."""
    assert str(school1) == 'Beauxbatons Academy of Magic'
    assert repr(school1) == 'Beauxbatons Academy of Magic [Ron Weasley 40]'


def test_cant_add_wizard_scool_is_full():
    """Test add wizard if school is full."""
    assert school2.add_wizard(wiz3) is None
    assert school2.add_wizard(wiz4) is None
    assert len(school2.wizards) == 2
    assert school2.add_wizard(wiz3) is None
    assert len(school2.wizards) == 2


def test_cant_add_wizard_exists():
    """Test add wizard if wizard exists."""
    assert len(school1.wizards) == 1
    assert str(school1.get_wizards()[0]) == str(wiz1)
    assert school1.add_wizard(wiz1) is None
    assert len(school1.wizards) == 1
    assert str(school1.get_wizards()[0]) == str(wiz1)


def test_cant_add_wizard_from_the_other_school():
    """Test cant add wizard from the other school."""
    assert wiz3.school == school2


def test_remove_wizard_from_school():
    """Test remove wizard from school."""
    assert wiz4.school == school2
    assert school2.remove_wizard(wiz4) is None
    assert len(school2.wizards) == 1
    assert wiz4.school is None


def test_get_wizards_count():
    """Test get_wizards_count()."""
    assert school3.add_wizard(wiz5) is None
    assert school3.get_wizards_count() == 1


def test_punish_wizard_dec_power():
    """Test punish wizard by decreasing power."""
    wiz1.power = 20
    assert wiz1.power == 20
    assert school1.punish_wizard_dec_power(wiz1, 10) is None
    assert wiz1.power == 10


def test_praise_wizard_inc_power():
    """Test praise wizard by increasing power."""
    assert wiz1.power == 10
    assert school1.praise_wizard_inc_power(wiz1, 15) is None
    assert wiz1.power == 25


def test_change_wizard_wand():
    """Test change wizards wand."""
    assert wiz3.wand == wand4
    assert wand6.owner is None
    assert school2.change_wizard_wand(wiz3, wand6) is None
    assert wiz3.wand == wand6
    assert wand4.owner is None


def test_add_house_to_school():
    """Test add house to school."""
    assert school1.get_houses() == []
    assert school1.add_house(house1) is None
    assert str(school1.get_houses()[0]) == 'Mustang House'


def test_add_house_to_school_house_exists():
    """Test add house to school when house exists."""
    assert str(school1.houses[0]) == 'Mustang House'
    assert school1.add_house(house1) is None
    assert str(school1.houses[0]) == 'Mustang House'
    assert school1.add_house(house2) is None
    assert str(school1.houses) == '[Mustang House 0, Durmstrang House 0]'


def test_get_houses():
    """Test get_houses list."""
    assert str(school1.get_houses()) == '[Mustang House 0, Durmstrang House 0]'


def test_add_wizard_to_house():
    """Test add wizard to House."""
    wiz1.power = 40
    assert school1.add_wizard(wiz4) is None
    assert str(school1.get_wizards()) == '[Ron Weasley 40, Draco Malfoy 45]'
    assert school1.add_wizard_to_house(wiz1, house1) is None
    assert str(school1.get_houses()) == '[Mustang House 1, Durmstrang House 0]'
    assert school1.add_wizard_to_house(wiz4, house2) is None
    assert str(school1.get_houses()) == '[Mustang House 1, Durmstrang House 1]'


def test_remove_wizard_from_house():
    """Test remove wizard from House."""
    assert school1.remove_wizard_from_house(wiz4, house2) is None
    assert str(school1.get_houses()) == '[Mustang House 1, Durmstrang House 0]'


def test_move_wizard_to_new_house():
    """Test move wizard from old to new House."""
    assert school1.move_wizard_to_new_house(wiz1, house1, house2) is None
    assert str(school1.get_houses()) == '[Mustang House 0, Durmstrang House 1]'


def test_remove_house_from_school():
    """Test remove house from school."""
    assert str(school1.get_houses()) == '[Mustang House 0, Durmstrang House 1]'
    assert school1.remove_house(house1) is None
    assert str(school1.get_houses()) == '[Durmstrang House 1]'


def test_remove_non_empty_house_from_school():
    """Test remove non-empty house from school."""
    assert str(school1.get_houses()) == '[Durmstrang House 1]'
    assert school1.remove_house(house1) is None
    assert str(school1.get_houses()) == '[Durmstrang House 1]'


def test_get_sorted_wizards_by_name_asc():
    """Test sort wizards by Name."""
    school2.remove_wizard(wiz3)
    school3.remove_wizard(wiz5)
    school1.add_wizard(wiz2)
    school1.add_wizard(wiz3)
    school1.add_wizard(wiz5)
    assert str(school1.get_sorted_wizards_by_name()) == '[Apolline Delacour 45, Draco Malfoy 45, Hermione Granger 20, ' \
                                                        'Neville Longbottom 35, Ron Weasley 40]'


def test_get_sorted_wizards_by_power_asc():
    """Test sort Wizards by power."""
    assert str(school1.get_sorted_wizards_by_power()) == '[Hermione Granger 20, Neville Longbottom 35, Ron Weasley 40, ' \
                                                         'Draco Malfoy 45, Apolline Delacour 45]'


def test_get_sorted_wizards_by_fights_asc():
    """Test sort Wizards by fights."""
    wiz1.fights = 5
    wiz1.fights = 2
    wiz1.fights = 3
    wiz1.fights = 4
    wiz1.fights = 1
    assert str(school1.get_sorted_wizards_by_fights()) == '[Draco Malfoy 45, Hermione Granger 20, Neville Longbottom 35,' \
                                                          ' Apolline Delacour 45, Ron Weasley 40]'


def test_get_sorted_wizards_by_wand_score_asc():
    """Test sort Wizards by Wand score."""
    assert str(school1.get_sorted_wizards_by_wand_score()) == '[Hermione Granger 20, Draco Malfoy 45, Ron Weasley 40, ' \
                                                              'Neville Longbottom 35, Apolline Delacour 45]'


def test_get_sorted_houses_by_wizards_count_asc():
    """Test sort Houses by Wizards count."""
    school1.add_house(house1)
    wiz2.power = 55
    school1.add_wizard_to_house(wiz2, house1)
    school1.add_wizard_to_house(wiz3, house1)
    school1.add_wizard_to_house(wiz4, house1)
    school1.add_wizard_to_house(wiz5, house2)
    assert str(house1.get_wizards()) == '[Hermione Granger 55, Neville Longbottom 35, Draco Malfoy 45]'
    assert str(house2.get_wizards()) == '[Ron Weasley 40, Apolline Delacour 45]'
    assert str(school1.get_sorted_houses_by_wizards_count()) == '[Durmstrang House 2, Mustang House 3]'


def test_get_houses_statistics_desc():
    """Test get Houses statistics."""
    assert str(school1.get_houses_statistics()) == "{'Mustang House': 3, 'Durmstrang House': 2}"


def test_wizard_duel():
    """Test wizard duel."""
    assert wiz2.power == 55
    assert wiz3.power == 35
    assert wiz2.wand.score == 10
    assert wiz3.wand.score == 40
    assert str(school1.wizard_duel(wiz2, wiz3)) == 'Neville Longbottom'  # winner is wiz3
    assert wiz2.power == 40  # power - ((40 - 10) / 2) wands diff / 2
    assert wiz3.power == 65  # power + (40 - 10) wands diff


def test_inc_power_with_letter():
    """Test increase power of Wizards with name started with given letter."""
    assert repr(school1.get_house_wizards(house1)) == '[Draco Malfoy 45, Hermione Granger 40, Neville Longbottom 65]'
    house1.inc_power_with_letter('N', 20)
    assert repr(school1.get_house_wizards(house1)) == '[Draco Malfoy 45, Hermione Granger 40, Neville Longbottom 85]'
