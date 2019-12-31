"""Day 06."""


def orbit_count_recur(d: dict, curnode: str, count: int, orbits: set) -> int:
    """Count orbits."""
    if curnode == 'COM':
        return count
    orbits.add(d[curnode])
    return orbit_count_recur(d, d[curnode], count + 1, orbits)


def make_child_parent_dict() -> dict:
    """Make child-parent dictionary."""
    d = {}
    with open('day06_data.txt', encoding='utf-8') as file:
        contents = file.read()
        for line in contents.splitlines():
            a = line.split(")")
            d[a[1]] = a[0]
    return d


if __name__ == '__main__':
    santa = set()
    you = set()

    dict = make_child_parent_dict()
    sum = 0

    for key in dict.items():
        sum += orbit_count_recur(dict, key[0], 0, santa)
    print(f"Answer 1: {sum}")

    santa = set()
    to_santa = orbit_count_recur(dict, 'SAN', 0, santa)
    to_you = orbit_count_recur(dict, 'YOU', 0, you)
    common = len(santa.intersection(you))
    print(f"Answer 2: {to_santa - common + to_you - common}")
