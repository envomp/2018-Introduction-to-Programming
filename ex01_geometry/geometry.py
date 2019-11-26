
first_contains_second, one_contains_another = lambda x, y: x in y, lambda x, y: first_contains_second(x, y) or first_contains_second(y, x)


if __name__ == '__main__':
    print(first_contains_second("bc", "abcd"))
    print(one_contains_another("bc", "abcd"))
    print(one_contains_another("abcd", "bc"))
