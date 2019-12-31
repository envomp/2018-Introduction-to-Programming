"""Day 01."""


def calc_fuel_required(mass: int) -> int:
    """Calc fuel required."""
    return mass // 3 - 2


def calc_additional_fuel(mass: int) -> int:
    """Calc additional fuel."""
    if mass <= 0:
        return 0
    return mass + calc_additional_fuel(calc_fuel_required(mass))


if __name__ == '__main__':
    # Part 1
    total = 0
    with open('day01_data.txt', encoding='utf-8') as file:
        for line in file:
            total += calc_fuel_required(int(line))
    print(total)

    # Part 2
    total = 0
    with open('day01_data.txt', encoding='utf-8') as file:
        for line in file:
            total += calc_additional_fuel(calc_fuel_required(int(line)))
    print(total)
