"""EX15 Magic."""


class MismatchError(Exception):
    """Exception when Wand deos not exists."""

    pass


class Wand:
    """Wand."""

    def __init__(self, wood_type: str, core: str, score: int):
        """Class constructor."""
        self.wood_type = wood_type
        self.core = core
        self.score = score
        self.owner = None

    def set_wood_type(self, wood_type):
        """Wood type setter."""
        self.wood_type = wood_type

    def set_core(self, core):
        """Core type setter."""
        self.wood_type = core

    @staticmethod
    def is_wand_correct(wand):
        """Check if Wand is correct."""
        if not isinstance(wand, Wand) or not wand.wood_type or not wand.core:
            raise MismatchError("The wand like that does not exist!")

    def __repr__(self):
        """Representation of Wand."""
        return f"{self.wood_type} Wand with {self.core} core ({self.score})"


class Wizard:
    """Wizard."""

    def __init__(self, name: str, power: int, wand=None):
        """Class constructor."""
        self.name = name
        self.power = power
        self.school = None
        self.wand = None
        self.fights = 0

        try:
            if wand is not None:
                Wand.is_wand_correct(wand)
                self.wand = wand
                wand.owner = self
        except MismatchError:
            raise MismatchError("The wand like that does not exist!")

    def set_wand(self, wand: Wand):
        """Wand setter."""
        try:
            Wand.is_wand_correct(wand)
            if self.check_wand:
                self.wand.owner = None
            self.wand = wand
            wand.owner = self
        except MismatchError as e:
            print(e)

    @property
    def check_wand(self):
        """Check if Wizard have a wand."""
        return True if self.wand is not None else False

    def __repr__(self):
        """Representation of Wizard."""
        return f"{self.name} {self.power}"

    def __str__(self):
        """String representation of Wizard."""
        return self.name


class WizardSchool:
    """Wizard School."""

    def __init__(self, name: str, max_wizards: int):
        """Class constructor."""
        self.name = name
        self.max_wizards = max_wizards
        self.wizards = []
        self.houses = []

    def get_wizards_count(self):
        """Get Wizards count."""
        return len(self.wizards)

    def get_wizards(self):
        """Get Wizards list."""
        return self.wizards

    def add_wizard(self, wizard):
        """Add Wizard to School."""
        if isinstance(wizard, Wizard) and self.get_wizards_count() < self.max_wizards and \
                wizard not in self.get_wizards() and wizard.check_wand and wizard.school is None:
            self.wizards.append(wizard)
            wizard.school = self

    def remove_wizard(self, wizard):
        """Remove wizard from school."""
        if wizard in self.get_wizards():
            self.wizards.remove(wizard)
            wizard.school = None

    def punish_wizard_dec_power(self, wizard, power_to_dec):
        """Punish wizard: decrease power."""
        if wizard in self.get_wizards():
            wizard.power -= power_to_dec

    def praise_wizard_inc_power(self, wizard, power_to_inc):
        """Punish wizard: decrease power."""
        if wizard in self.get_wizards():
            wizard.power += power_to_inc

    def change_wizard_wand(self, wizard, new_wand):
        """Change Wizad wand."""
        if wizard in self.get_wizards():
            wizard.wand.owner = None
            wizard.set_wand(new_wand)

    def add_house(self, house):
        """Add house."""
        if isinstance(house, House) and house not in self.get_houses():
            self.houses.append(house)

    def remove_house(self, house):
        """Remove house."""
        if isinstance(house, House) and house in self.get_houses() and len(house.get_wizards()) == 0:
            self.houses.remove(house)

    def get_houses(self):
        """Get Houses list."""
        return self.houses

    def add_wizard_to_house(self, wizard, house):
        """Add wizard to House."""
        if wizard in self.get_wizards() and wizard not in self.get_house_wizards(house):
            house.add_wizard(wizard)

    def remove_wizard_from_house(self, wizard, house):
        """Remove wizard from House."""
        if wizard in self.get_wizards() and wizard in self.get_house_wizards(house):
            house.remove_wizard(wizard)

    def move_wizard_to_new_house(self, wizard, old_house, new_house):
        """Move wizard from old to new House."""
        if wizard in self.get_wizards() and wizard in self.get_house_wizards(old_house):
            old_house.remove_wizard(wizard)
            self.add_wizard_to_house(wizard, new_house)

    def get_sorted_wizards_by_name(self, reverse: bool = False):
        """Sort Wizards by name."""
        return sorted(self.wizards, key=lambda wizard: wizard.name, reverse=reverse)

    def get_sorted_wizards_by_power(self, reverse: bool = False):
        """Sort Wizards by power."""
        return sorted(self.wizards, key=lambda wizard: wizard.power, reverse=reverse)

    def get_sorted_wizards_by_fights(self, reverse: bool = False):
        """Sort Wizards by fights."""
        return sorted(self.wizards, key=lambda wizard: wizard.fights, reverse=reverse)

    def get_sorted_wizards_by_wand_score(self, reverse: bool = False):
        """Sort Wizards by Wand score."""
        return sorted(self.wizards, key=lambda wizard: wizard.wand.score, reverse=reverse)

    def get_sorted_houses_by_wizards_count(self, reverse: bool = False):
        """Sort Houses by Wizards count."""
        if reverse:
            return sorted(self.houses, key=lambda house: (-house.get_wizards_count(), house.name))
        else:
            return sorted(self.houses, key=lambda house: (house.get_wizards_count(), house.name))

    def get_houses_statistics(self):
        """Get Houses statistics."""
        houses = {}
        for house in self.get_sorted_houses_by_wizards_count(True):
            houses[house.name] = house.get_wizards_count()
        return houses

    def get_house_wizards(self, house):
        """Get House Wizards."""
        return house.get_sorted_wizards_by_name()

    def __repr__(self):
        """Representation of School."""
        return f"{self.name} {self.get_wizards()}"

    def __str__(self):
        """String representation of School."""
        return self.name

    @staticmethod
    def wizard_duel(wizard1: Wizard, wizard2: Wizard):
        """Wizard duel."""
        winner = None
        if wizard1.wand.score > wizard2.wand.score:
            winner = wizard1
            wizard1.power += wizard1.wand.score - wizard2.wand.score
            wizard2.power -= (wizard1.wand.score - wizard2.wand.score) // 2
        elif wizard1.wand.score < wizard2.wand.score:
            winner = wizard2
            wizard2.power += wizard2.wand.score - wizard1.wand.score
            wizard1.power -= (wizard2.wand.score - wizard1.wand.score) // 2
        wizard1.fights += 1
        wizard2.fights += 1

        return winner


class House(WizardSchool):
    """House of Wizard School."""

    def __init__(self, name: str, max_wizards: int):
        """Init."""
        super().__init__(name, max_wizards)

    def add_wizard(self, wizard):
        """Add Wizard to House."""
        if wizard.school is not None and (wizard.power > 30 or wizard.fights > 10) and wizard not in self.get_wizards():
            self.wizards.append(wizard)

    def remove_wizard(self, wizard):
        """Remove wizard from House."""
        if wizard in self.get_wizards():
            self.wizards.remove(wizard)

    def inc_power_with_letter(self, letter: str, power: int):
        """Increase power of Wizards with name started with given letter."""
        for wizard in [wizard for wizard in self.get_wizards() if wizard.name[0] == letter]:
            wizard.power += power

    def __repr__(self):
        """Representation of House."""
        return f"{self.name} {len(self.wizards)}"

    def __str__(self):
        """String representation of House."""
        return self.name


if __name__ == '__main__':
    wand1 = Wand('Oak', 'Phoenix Feather', 40)
    wand2 = Wand('Birch', 'Dragon Heartstring', 10)
    wand3 = Wand('Pine', 'Unicorn Hair', 20)
    wand4 = Wand('Mapple', 'Veela Hair', 30)
    wand5 = Wand('Rowan', 'Thestral Hair', 50)

    wiz1 = Wizard('Ron Weasley', 40, wand1)
    wiz2 = Wizard('Hermione Granger', 20, wand2)
    wiz3 = Wizard('Neville Longbottom', 35, wand3)
    wiz4 = Wizard('Draco Malfoy', 45, wand4)

    school1 = WizardSchool('Beauxbatons Academy of Magic', 10)
    school2 = WizardSchool('Durmstrang Institute for Magical Learning', 5)
    school3 = WizardSchool('Hogwarts School of Witchcraft and Wizardry', 15)
    school4 = WizardSchool('Ilvermorny School of Witchcraft and Wizardry', 25)

    print(f">> Add new school: {school1}")
    print(f">> Add 4 wizards to {school1}: {wiz2}, {wiz1}, {wiz3}")
    school1.add_wizard(wiz2)
    school1.add_wizard(wiz1)
    school1.add_wizard(wiz3)
    print(f"Get {school1} wizards: {school1.get_wizards()}")
    print(f"Get {school1} houses: {school1.get_houses()}")
    house1 = House('Mustang House', 20)
    house2 = House('Durmstrang House', 10)
    school1.add_house(house1)
    print(f">> Add {house1} to {school1}")
    school1.add_house(house2)
    print(f">> Add {house2} to {school1}")
    print(f"Get {school1.name} houses: {school1.get_houses()}")
    school1.add_wizard_to_house(wiz1, house1)
    print(f">> Add wizard {wiz1} to {house1}")
    school1.add_wizard_to_house(wiz2, house2)
    print(f">> Add wizard {wiz2} to {house2}")
    school1.add_wizard_to_house(wiz3, house1)
    print(f">> Add wizard {wiz3} to {house1}")
    print(f"Get {school1} houses: {school1.get_houses()}")
    print(f">> Add AGAIN wizard {wiz3} to {house1}")
    print(f"Get {school1} houses: {school1.get_houses()}")
    print(f">> Trying to add {wiz4} directly to house {house1}")
    house1.add_wizard(wiz4)
    print(f"Get {school1} houses: {school1.get_houses()} - NO SUCESS!")
    print(f">> Add wizard {wiz4} to {school1}")
    school1.add_wizard(wiz4)
    print(f">> And NOW we can add wizard {wiz4} to {house1}")
    school1.add_wizard_to_house(wiz4, house1)
    print(f"Get {school1} houses: {school1.get_houses()}")
    print(f"Get {school1} houses sort by wiz count: {school1.get_sorted_houses_by_wizards_count()}")
    print(f"Get {school1} all houses statistics: {school1.get_houses_statistics()}")
    print(f"Get house {house1} wizards: {school1.get_house_wizards(house1)}")
    print(f"Get house {house2} wizards: {school1.get_house_wizards(house2)}")
    print(f">> Move wizard {wiz3} from {house1} to {house2}")
    school1.move_wizard_to_new_house(wiz3, house1, house2)
    print(f"Get house {house1} wizards: {school1.get_house_wizards(house1)}")
    print(f"Get house {house2} wizards: {school1.get_house_wizards(house2)}")
    print(f">> Remove wizard {wiz3} from {house2}")
    school1.remove_wizard_from_house(wiz3, house2)
    print(f"Get house {house2} wizards: {school1.get_house_wizards(house2)}")
    print(f"Get {school1} wizards: {school1.get_wizards()}")
    print(f">> Remove wizard {wiz2} from {school1} AT ALL")
    school1.remove_wizard(wiz2)
    print(f"Get {school1} wizards: {school1.get_wizards()}")
    print(f"Get {school1} wizards sorted by power: {school1.get_sorted_wizards_by_power(True)}")
    print(f"Get wizard {wiz1} fights: {wiz1.fights}")
    print(f"Get wizard {wiz3} fights: {wiz3.fights}")
    print(f">> Make duel between {wiz1} and {wiz3}: winner is {school1.wizard_duel(wiz1, wiz3)}")
    print(f"Get {school1} wizards sorted by power: {school1.get_sorted_wizards_by_power(True)}")
    print(f"Get wizard {wiz1} fights: {wiz1.fights}")
    print(f"Get wizard {wiz3} fights: {wiz3.fights}")
    print(f"Get wizard {wiz3} wand type: {wiz3.wand}")
    print(f"Get wizard {wiz3} wand owner: {wiz3.wand.owner}")
    print(f">> Change wizard {wiz3} wand to new {wand5}")
    school1.change_wizard_wand(wiz3, wand5)
    print(f"Get wizard {wiz3} wand type: {wiz3.wand}")
    print(f"Get wizard {wiz3} wand owner: {wiz3.wand.owner}")
    print(f"Get free {wand3} wand owner: {wand3.owner}")
