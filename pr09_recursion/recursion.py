"""Recursion is recursion."""


def recursive_reverse(s: str) -> str:
    """Reverse a string using recursion.

    recursive_reverse("") => ""
    recursive_reverse("abc") => "cba"

    :param s: string
    :return: reverse of s
    """
    return "" if not s else s[-1] + recursive_reverse(s[:-1])


def remove_nums_and_reverse(string):
    """
    Recursively remove all the numbers in the string and return reversed version of that string without numbers.

    print(remove_nums_and_reverse("poo"))  # "oop"
    print(remove_nums_and_reverse("3129047284"))  # empty string
    print(remove_nums_and_reverse("34e34f7i8l 00r532o23f 4n5ot565hy7p4"))  # "python for life"
    print(remove_nums_and_reverse("  k 4"))  # " k  "

    :param string: given string to change
    :return: reverse version of the original string, only missing numbers
    """
    if not string:
        return ""  # End of recursion
    else:
        return ("" if string[-1].isnumeric() else string[-1]) + remove_nums_and_reverse(string[:-1])


def task1(string):
    """
    Return True if string is the same from start to end and from end to start (mirrored), else return False.

    :param string: given string
    :return: figure it out

    for i in range(len(string)):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True
    """
    if not string:
        return True  # End of recursion

    if string[0] != string[-1]:
        return False
    else:
        return task1(string[1:-1])


def task2(string):
    """
    Put "-" between the following characters if they are the same.

    :param string: given string
    :return: figure it out

    if len(string) < 2:
        return string
    elif string[0] == string[1]:
        return string[0] + "-" + task2(string[1:])
    return string[0] + task2(string[1:])
    """
    out = ""
    if len(string) < 2:
        return string
    for i in range(len(string) - 1):
        out += string[i] + ("-" if string[i] == string[i + 1] else "")
    out += string[-1]
    return out


if __name__ == '__main__':
    print(recursive_reverse("abc"))
    print(remove_nums_and_reverse("34e34f7i8l 00r532o23f 4n5ot565yh7p4"))  # "python for life"
    print(task1("adfda"))
    print(task2("aaaaabaccc"))  # a-a-a-a-abac-c-c
