"""Pizzeria."""
from math import pi, floor


class Chef:
    """Class Chef."""

    def __init__(self, name: str, experience_level: int):
        """Initiate class Chef."""
        self.name = name
        self.experience_level = experience_level
        self.money = 0

    def __repr__(self):
        """Print Chef's name and XP."""
        return f"Pizza chef {self.name.capitalize()} with {self.experience_level} XP"

    def __lt__(self, other):
        """Less than."""
        return self.experience_level < other.experience_level


class Pizza:
    """Class Pizza."""

    def __init__(self, name: str, diameter: int, toppings: list):
        """Initiate class Pizza."""
        self.name = name
        self.diameter = diameter
        self.toppings = toppings

    def calculate_complexity(self) -> int:
        """Calculate complexity."""
        complexity = 0
        for topping in self.toppings:
            complexity += len(topping) // 3
        return complexity

    def calculate_price(self) -> int:
        """Calculate price."""
        area = pi * (self.diameter / 2) ** 2
        price = floor((area / 40 + len(self.toppings) // 2) * 100) / 100
        return int(price * 100)

    def __repr__(self):
        """Print Pizza's name and price."""
        return f"{self.name.capitalize()} pizza with a price of {self.calculate_price() / 100}"

    def __lt__(self, other):
        """Less than."""
        return self.calculate_price() < other.calculate_price()


class Pizzeria:
    """Class Pizzeria."""

    def __init__(self, name: str, is_fancy: bool, budget: int):
        """Initiate class Pizzeria."""
        self.name = name
        self.is_fancy = is_fancy
        self.budget = budget
        self.chefs = []
        self.menu = []
        self.baked_pizzas = {}

    def add_chef(self, chef: Chef) -> Chef or None:
        """Add chef."""
        if chef not in self.chefs:
            if self.is_fancy:
                if chef.experience_level >= 25:
                    self.chefs.append(chef)
                    return chef
                else:
                    return None
            else:
                self.chefs.append(chef)
                return chef
        else:
            return None

    def remove_chef(self, chef: Chef):
        """Remove chef."""
        if chef in self.chefs:
            self.chefs.remove(chef)

    def add_pizza_to_menu(self, pizza: Pizza):
        """Add pizza to menu."""
        if len(self.chefs) and pizza not in self.menu and self.budget - pizza.calculate_price() >= 0:
            self.menu.append(pizza)
            self.budget -= pizza.calculate_price()

    def remove_pizza_from_menu(self, pizza: Pizza):
        """Remove pizza from menu."""
        if pizza in self.menu:
            self.menu.remove(pizza)

    def bake_pizza(self, pizza: Pizza) -> Pizza or None:
        """Bake pizza."""
        if pizza not in self.menu:
            return None
        for chef in self.get_chefs():
            if chef.experience_level >= pizza.calculate_complexity():
                chef.experience_level += len(pizza.name) // 2
                profit = pizza.calculate_price() * 4 + len(pizza.name)
                self.budget += profit // 2
                chef.money += profit // 2
                # self.baked_pizzas[pizza] = self.baked_pizzas.get(pizza, 0) + 1
                if not self.baked_pizzas.get(pizza):
                    self.baked_pizzas[pizza] = 1
                else:
                    self.baked_pizzas[pizza] += 1
                return pizza
        return None

    def get_pizza_menu(self) -> list:
        """Get pizza menu."""
        return sorted(self.menu, reverse=True)

    def get_baked_pizzas(self) -> dict:
        """Get baked pizzas."""
        return self.baked_pizzas

    def get_chefs(self) -> list:
        """Get chefs."""
        return sorted(self.chefs, reverse=False)

    def __repr__(self):
        """Print Pizzeria's name and number of chefs."""
        return f"{self.name.capitalize()} with {len(self.chefs)} pizza chef(s)."


if __name__ == '__main__':
    pizzeria1 = Pizzeria("Mama's Pizza", True, 10000)
    print(pizzeria1)  # Mama's pizza with 0 pizza chef(s).

    pizzeria1.add_chef(Chef("Clara", 24))
    print(pizzeria1)
    # Mama's pizza with 0 pizza chef(s). -> Clara was not added because of low XP (24) since it's a fancy pizzeria.

    pizza1 = Pizza("basic", 20, ["Cheese", "Ham"])
    print(pizzeria1.bake_pizza(pizza1))  # None -> No such pizza on the menu nor a chef in the pizzeria.

    ##########################################################
    sebastian = Chef("Sebastian", 58)
    charles = Chef("Charles", 35)
    kimi = Chef("Kimi", 83)

    pizzeria1.add_chef(sebastian)
    pizzeria1.add_chef(charles)
    pizzeria1.add_chef(kimi)

    print(pizzeria1.get_chefs())

    # Trying to order a pizza which is not on the menu.

    print(pizzeria1.bake_pizza(pizza1))  # None

    pizzeria1.add_pizza_to_menu(pizza1)  # Price is 8.85

    print(pizzeria1.budget)  # 9115
    print(pizzeria1.get_pizza_menu())  # [Basic pizza with a price of 8.85]

    print(pizzeria1.bake_pizza(pizza1))  # Basic pizza with a price of 8.85

    print(pizzeria1.get_chefs())
    # Charles was chosen to bake the pizza, because Charles' XP was the closest to pizza's complexity

    print(pizzeria1.budget)  # 10887
    print(charles.money)  # 1772

    print(pizzeria1.get_baked_pizzas())  # {Basic pizza with a price of 8.85: 1}

    ##########################################################
    pizzeria2 = Pizzeria("Maranello", False, 10000)

    fernando = Chef("Fernando", 9)
    felipe = Chef("Felipe", 6)
    michael = Chef("Michael", 17)
    rubens = Chef("Rubens", 4)
    eddie = Chef("Eddie", 5)

    pizzeria2.add_chef(fernando)
    pizzeria2.add_chef(felipe)
    pizzeria2.add_chef(michael)
    pizzeria2.add_chef(rubens)
    pizzeria2.add_chef(eddie)

    margherita = Pizza("Margherita", 20, ["Sauce", "Mozzarella", "Basil"])
    smoke = Pizza("Big Smoke", 30, ["nine", "NINE", "six w/dip", "seven", "45", "45 w/cheese", "SODA"])

    pizzeria2.add_pizza_to_menu(margherita)
    pizzeria2.add_pizza_to_menu(smoke)

    print(pizzeria2.get_pizza_menu())  # [Big smoke pizza with a price of 20.67, Margherita pizza with a price of 8.85]
    print(pizzeria2.get_chefs())
    # [Pizza chef Rubens with 4 XP, Pizza chef Eddie with 5 XP, Pizza chef Felipe with 6 XP, Pizza chef Fernando with 9 XP, Pizza chef Michael with 17 XP]

    pizzeria2.bake_pizza(margherita)
    print(pizzeria2.get_chefs())
    # [Pizza chef Rubens with 4 XP, Pizza chef Felipe with 6 XP, Pizza chef Fernando with 9 XP, Pizza chef Eddie with 10 XP, Pizza chef Michael with 17 XP]

    pizzeria2.bake_pizza(smoke)
    print(pizzeria2.get_chefs())
    # [Pizza chef Rubens with 4 XP, Pizza chef Felipe with 6 XP, Pizza chef Fernando with 9 XP, Pizza chef Eddie with 14 XP, Pizza chef Michael with 17 XP]
