"""Day 4."""
import re

if __name__ == '__main__':
    count = 0
    for num in range(123257, 647016):
        i = str(num)
        if i[0] <= i[1] and i[1] <= i[2] and i[2] <= i[3] and i[3] <= i[4] and i[4] <= i[5] and len(set(i)) < 6:
            count += 1
    print(f"Answer 1: {count}")

    count = 0
    for num in range(123257, 647016):
        i = str(num)
        if i[0] <= i[1] and i[1] <= i[2] and i[2] <= i[3] and i[3] <= i[4] and i[4] <= i[5] and len(set(i)) < 6:
            abi = re.findall(r'((\w)\2{1,})', i)
            if len(abi) == 3 or (len(abi) == 1 and len(abi[0][0]) == 2) or \
                    (len(abi) == 2 and (len(abi[0][0]) == 2 or len(abi[1][0]) == 2)):
                count += 1

    print(f"Answer 2: {count}")
