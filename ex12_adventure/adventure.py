"""Adventure."""


class Adventurer:
    """Class Adventurer."""

    def __init__(self, name: str, class_type: str, power: int, experience: int = 0):
        """Constructor that creates an Adventurer.

        :param name: Adventurer name
        :param class_type: Adventurer type
        :param power: Adventurer power
        :param experience: Adventurer experience
        :return: None
        """
        allowed_class_types = ["Fighter", "Druid", "Wizard", "Paladin"]
        self.name = name

        if class_type not in allowed_class_types:
            self.class_type = "Fighter"
        else:
            self.class_type = class_type

        self.power = power
        self.experience = experience

    def add_experience(self, exp: int):
        """
        Add experience to Adventurer.

        :param exp: experience to add
        :return: None
        """
        self.experience += exp

    def add_power(self, power: int):
        """
        Add power to Adventurer.

        :param power: power to add
        :return: None
        """
        self.power += power

    def __repr__(self):
        """Print Adventurer's name, power and XP."""
        return f"{self.name}, the {self.class_type}, Power: {self.power}, Experience: {self.experience}."

    def __lt__(self, other):
        """Less than."""
        return self.experience < other.experience


class Monster:
    """Class Monster."""

    def __init__(self, name: str, mon_type: str, power: int = 0):
        """Constructor that creates a Monster.

        :param name: Monster name
        :param mon_type: Monster type
        :param power: Monster power
        :return: None
        """
        self.name = name
        self.mon_type = mon_type
        self.power = power

    @property
    def monster_name(self) -> str:
        """
        Add Undead to Monster name if type is Zombie.

        :return: Name, str.
        """
        return "Undead " + self.name if self.mon_type == "Zombie" else self.name

    def __repr__(self):
        """Print Monster's name, power and XP."""
        return f"{self.monster_name} of type {self.mon_type}, Power: {self.power}."

    def __lt__(self, other):
        """Less than."""
        return self.power < other.power


class World:
    """Class World."""

    def __init__(self, pm: str):
        """Constructor that creates a World.

        :param pm: PythonMaster's name, string
        """
        self.pythonmaster = pm
        self.adventurerlist = []
        self.monsterlist = []
        self.graveyard = []
        self.active_adventurers = []
        self.active_monsters = []
        self.necromancer = False
        self.paladin = False

    def get_python_master(self) -> str:
        """Return PythnMaster's name."""
        return self.pythonmaster

    def add_adventurer(self, adventurer: Adventurer):
        """Add an Adventurer to the World."""
        if isinstance(adventurer, Adventurer):
            self.adventurerlist.append(adventurer)

    def add_monster(self, monster: Monster):
        """Add a Monster to the World."""
        if isinstance(monster, Monster):
            self.monsterlist.append(monster)

    def get_adventurerlist(self) -> list:
        """Return Adventurers list."""
        return self.adventurerlist

    def get_monsterlist(self) -> list:
        """Return Monsters list."""
        return self.monsterlist

    def get_graveyard(self) -> list:
        """Return Graveyard list."""
        return self.graveyard

    def change_necromancer(self, necro: bool):
        """Change necromancer."""
        self.necromancer = necro

    def revive_graveyard(self):
        """Revieve graveyard."""
        if self.necromancer:
            for dead in self.get_graveyard():
                if isinstance(dead, Monster):
                    dead.mon_type = 'Zombie'
                    self.add_monster(dead)
                else:  # Adventurer
                    self.add_monster(Monster("Undead " + dead.name, "Zombie " + dead.class_type, dead.power))
            self.graveyard = []
            self.necromancer = False

    def add_strongest(self, class_type: str):
        """Add strongest Adventurer to active_adventurers list."""
        out = [i for i in self.get_adventurerlist() if i.class_type == class_type]
        out = [a for a in out if a.power == max([a.power for a in out])]
        if len(out):
            self.active_adventurers.append(out[0])
            self.adventurerlist.remove(out[0])

    def add_weakest(self, class_type: str):
        """Add weakest Adventurer to active_adventurers list."""
        out = [i for i in self.get_adventurerlist() if i.class_type == class_type]
        out = [a for a in out if a.power == min([a.power for a in out])]
        if len(out):
            self.active_adventurers.append(out[0])
            self.adventurerlist.remove(out[0])

    def add_most_experience(self, class_type: str):
        """Add most experienced Adventurer to active_adventurers list."""
        out = [i for i in self.get_adventurerlist() if i.class_type == class_type]
        out = [a for a in out if a.experience == max([a.experience for a in out])]
        if len(out):
            self.active_adventurers.append(out[0])
            self.adventurerlist.remove(out[0])

    def add_least_experience(self, class_type: str):
        """Add least experienced Adventurer to active_adventurers list."""
        out = [i for i in self.get_adventurerlist() if i.class_type == class_type]
        out = [a for a in out if a.experience == min([a.experience for a in out])]
        if len(out):
            self.active_adventurers.append(out[0])
            self.adventurerlist.remove(out[0])

    def add_by_name(self, name: str):
        """Add specific Adventurer to active_adventurers list."""
        out = [i for i in self.get_adventurerlist() if i.name == name]
        if len(out):
            self.active_adventurers.append(out[0])
            self.adventurerlist.remove(out[0])

    def add_all_of_class_type(self, class_type: str):
        """Add all Adventurers of specific type to active_adventurers list."""
        out = [i for i in self.get_adventurerlist() if i.class_type == class_type]
        for adventurer in out:
            self.active_adventurers.append(adventurer)
            self.adventurerlist.remove(adventurer)

    def add_all(self):
        """Add all Adventurers to active_adventurers list."""
        out = [i for i in self.get_adventurerlist()]
        for adventurer in out:
            self.active_adventurers.append(adventurer)
            self.adventurerlist.remove(adventurer)

    def get_active_adventurers(self):
        """Get active Adventurers from active_adventurers list."""
        return sorted(self.active_adventurers, reverse=True)

    def add_monster_by_name(self, name: str):
        """Add specific Monster to active_monsters list."""
        out = [i for i in self.get_monsterlist() if i.name == name]
        if len(out):
            self.active_monsters.append(out[0])
            self.monsterlist.remove(out[0])

    def add_strongest_monster(self):
        """Add the strongest Monster to active_monsters list."""
        out = [i for i in self.get_monsterlist() if i.power == max([i.power for i in self.get_monsterlist()])]
        if len(out):
            self.active_monsters.append(out[0])
            self.monsterlist.remove(out[0])

    def add_weakest_monster(self):
        """Add the weakest Monster to active_monsters list."""
        out = [i for i in self.get_monsterlist() if i.power == min([i.power for i in self.get_monsterlist()])]
        if len(out):
            self.active_monsters.append(out[0])
            self.monsterlist.remove(out[0])

    def add_all_of_type(self, mon_type: str):
        """Add all Monsters of specific type to active_monsters list."""
        out = [i for i in self.get_monsterlist() if i.mon_type == mon_type]
        for monster in out:
            self.active_monsters.append(monster)
            self.monsterlist.remove(monster)

    def add_all_monsters(self):
        """Add all Monsters to active_monsters list."""
        out = [i for i in self.get_monsterlist()]
        for monster in out:
            self.active_monsters.append(monster)
            self.monsterlist.remove(monster)

    def get_active_monsters(self):
        """Get active Monsters from active_adventurers list."""
        return sorted(self.active_monsters, reverse=True)

    def remove_character(self, name: str):
        """Remove specific character from the World."""
        out = [i for i in self.get_adventurerlist() if i.name == name]
        if len(out):
            self.adventurerlist.remove(out[0])
        else:
            out = [i for i in self.get_monsterlist() if i.monster_name == name]
            if len(out):
                self.monsterlist.remove(out[0])
            else:
                out = [i for i in self.get_graveyard() if i.name == name]
                if len(out):
                    self.graveyard.remove(out[0])

    def remove_active_monsters(self):
        """Remove active Monsters."""
        out = [i for i in self.get_active_monsters()]
        for monster in out:
            self.active_monsters.remove(monster)
            self.monsterlist.append(monster)

    def remove_active_adventurers(self):
        """Remove active Adventurers."""
        out = [i for i in self.get_active_adventurers()]
        for adventurer in out:
            self.active_adventurers.remove(adventurer)
            self.adventurerlist.append(adventurer)

    def remove_active_monsters_to_graveyard(self):
        """Remove active Monsters to graveyard."""
        out = [i for i in self.get_active_monsters()]
        for monster in out:
            self.active_monsters.remove(monster)
            self.graveyard.append(monster)

    def remove_active_adventurers_to_graveyard(self):
        """Remove active Adventurers to graveyard."""
        out = [i for i in self.get_active_adventurers()]
        for adventurer in out:
            self.active_adventurers.remove(adventurer)
            self.graveyard.append(adventurer)

    def add_experience_to_active_adventurers(self, exp: int):
        """Add experience to Adventuresrs."""
        for adventurer in self.get_active_adventurers():
            adventurer.experience += exp

    def get_adventurers_power(self):
        """Get all Adventurers power."""
        power = 0
        for adventurer in self.get_active_adventurers():
            if self.paladin and adventurer.class_type == 'Paladin':
                power += 2 * adventurer.power
            else:
                power += adventurer.power
        return power

    def get_monsters_power(self):
        """Get all Monsters power."""
        power = 0
        for monster in self.get_active_monsters():
            power += monster.power
        return power

    def check_animal_ent_druid(self):
        """Check animal or Ent."""
        druid = [i for i in self.get_active_adventurers() if i.class_type == 'Druid']
        if len(druid):
            animal_ent = [i for i in self.get_active_monsters() if i.mon_type == 'Animal' or i.mon_type == 'Ent']
            if len(animal_ent):
                for monster in animal_ent:
                    self.active_monsters.remove(monster)
                    self.monsterlist.append(monster)

    def need_to_double_paladin_power(self) -> bool:
        """Double or not Paladin power."""
        monsters = [i for i in self.get_active_monsters() if i.mon_type == 'Zombie' or i.mon_type == 'Zombie Fighter'
                    or i.mon_type == 'Zombie Druid' or i.mon_type == 'Zombie Paladin' or i.mon_type == 'Zombie Wizard']
        if len(monsters):
            paladins = [i for i in self.get_active_adventurers() if i.class_type == 'Paladin']
            return True if len(paladins) else False

    def go_adventure(self, deadly=False):
        """Play Adventure."""
        self.check_animal_ent_druid()
        self.paladin = self.need_to_double_paladin_power()

        if self.get_adventurers_power() > self.get_monsters_power():
            if not deadly:
                exp_points = self.get_monsters_power() // len(self.get_active_adventurers())
                self.remove_active_monsters()
            else:  # deadly
                exp_points = (self.get_monsters_power() // len(self.get_active_adventurers())) * 2
                self.remove_active_monsters_to_graveyard()
            self.add_experience_to_active_adventurers(exp_points)
            self.remove_active_adventurers()
        elif self.get_adventurers_power() == self.get_monsters_power():
            if not deadly:
                exp_points = (self.get_monsters_power() // len(self.get_active_adventurers())) // 2
            else:
                exp_points = self.get_monsters_power() // len(self.get_active_adventurers())
            self.remove_active_monsters()
            self.add_experience_to_active_adventurers(exp_points)
            self.remove_active_adventurers()
        else:
            self.remove_active_monsters()
            if not deadly:
                self.remove_active_adventurers()
            else:
                self.remove_active_adventurers_to_graveyard()


if __name__ == "__main__":
    print("Kord oli maailm.")

    Maailm = World("Sõber")
    print(Maailm.get_python_master())  # -> "Sõber"
    print(Maailm.get_graveyard())  # -> []

    print()
    print("Tutvustame tegelasi.")
    Kangelane = Adventurer("Sander", "Paladin", 50)
    Tüütu_Sõber = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)
    Lahe_Sõber = Adventurer("Peep", "Druid", 25)
    Teine_Sõber = Adventurer("Toots", "Wizard", 40)

    print(Kangelane)  # -> "Sander, the Paladin, Power: 50, Experience: 0."
    # Ei, tüütu sõber, sa ei saa olla tulevikurändaja ja ninja, nüüd sa pead fighter olema.
    print(Tüütu_Sõber)  # -> "XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 999999, Experience: 0."

    print("Sa ei tohiks kohe alguses ka nii tugev olla.")
    Tüütu_Sõber.add_power(-999959)
    print(Tüütu_Sõber)  # -> XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 40, Experience: 0.
    print()
    print(Lahe_Sõber)  # -> "Peep, the Druid, Power: 25, Experience: 0."
    print(Teine_Sõber)  # -> "Toots, the Wizard, Power: 40, Experience: 0."
    print()
    Lahe_Sõber.add_power(20)
    print("Sa tundud kuidagi nõrk, ma lisasin sulle natukene tugevust.")
    print(Lahe_Sõber)  # -> "Peep, the Druid, Power: 45, Experience: 0."

    Maailm.add_adventurer(Kangelane)
    Maailm.add_adventurer(Lahe_Sõber)
    Maailm.add_adventurer(Teine_Sõber)
    print(Maailm.get_adventurerlist())  # -> Sander, Peep ja Toots

    Maailm.add_monster(Tüütu_Sõber)
    # Ei, tüütu sõber, sa ei saa olla vaenlane.
    print(Maailm.get_monsterlist())  # -> []
    Maailm.add_adventurer(Tüütu_Sõber)

    print()
    print()
    print("Oodake veidikene, ma tekitan natukene kolle.")
    Zombie = Monster("Rat", "Zombie", 10)
    GoblinSpear = Monster("Goblin Spearman", "Goblin", 10)
    GoblinArc = Monster("Goblin Archer", "Goblin", 5)
    BigOgre = Monster("Big Ogre", "Ogre", 120)
    GargantuanBadger = Monster("Massive Badger", "Animal", 1590)

    print(BigOgre)  # -> "Big Ogre of type Ogre, Power: 120."
    print(Zombie)  # -> "Undead Rat of type Zombie, Power: 10."
    Maailm.add_monster(GoblinSpear)

    print()
    print()
    print("Mängime esimese kakluse läbi!")
    Maailm.add_strongest("Druid")
    Maailm.add_strongest_monster()
    print(Maailm.get_active_adventurers())  # -> Peep
    print(Maailm.get_active_monsters())  # -> [Goblin Spearman of type Goblin, Power: 10.]

    Maailm.go_adventure(True)

    Maailm.add_strongest("Druid")
    print(Maailm.get_active_adventurers())  # -> [Peep, the Druid, Power: 45, Experience: 20.]
    print("Surnuaias peaks üks goblin olema.")
    print(Maailm.get_graveyard())  # ->[Goblin Spearman of type Goblin, Power: 10.]

    Maailm.add_monster(GargantuanBadger)
    Maailm.add_strongest_monster()

    Maailm.go_adventure(True)
    # Druid on loomade sõber, ja ajab massiivse mägra ära.
    print(Maailm.get_adventurerlist())  # -> Kõik 4 mängijat.
    print(Maailm.get_monsterlist())  # -> [Massive Badger of type Animal, Power: 1590.]

    Maailm.remove_character("Massive Badger")
    print(Maailm.get_monsterlist())  # -> []

    print(
        "Su sõber ütleb: \"Kui kõik need testid andsid sinu koodiga sama tulemuse mille ma siin ette kirjutasin, peaks kõik okei olema, proovi testerisse pushida! \" ")
