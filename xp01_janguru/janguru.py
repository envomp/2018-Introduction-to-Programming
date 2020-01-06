"""Jänguru."""
import math


def least_common_multiple(x: int, y: int) -> int:
    """
    Calculate least common multiple of two digits.

    :param x: digit 1
    :param y: digit 2
    :return: LCM of digits
    """
    return x * y // math.gcd(x, y)  # Greatest Common Divisor



def meet_me(pos1: int, jump_distance1: int, sleep1: int, pos2: int, jump_distance2: int, sleep2: int) -> int:
    """
    Calulate meeting point of two jängurus.
    :param pos1: start position of jänguru 1
    :param jump_distance1: jump distance of jänguru 1
    :param sleep1: sleep time of jänguru 1
    :param pos2: start position of jänguru 2
    :param jump_distance2: jump distance of jänguru 2
    :param sleep2: sleep time of jänguru 2
    :return: meeting point or -1 if there is no meeting point
    """
    if jump_distance1 / sleep1 == jump_distance2 / sleep2 and pos1 == pos2:  # Overlapping lines.
        return pos1 + jump_distance1

    calc_time = 0 if jump_distance1 / sleep1 == jump_distance2 / sleep2 else \
        round((pos2 - pos1) / (jump_distance1 / sleep1 - jump_distance2 / sleep2))

    time1 = (int(calc_time / sleep1) - sleep1 * 40) * sleep1 \
        if (int(calc_time / sleep1) - sleep1 * 40) * sleep1 > 0 else sleep1
    time2 = (int(calc_time / sleep2) - sleep2 * 40) * sleep2 \
        if (int(calc_time / sleep2) - sleep2 * 40) * sleep2 > 0 else sleep2

    prev_time = 0
    prev_delta = 0

    time = time1 if time1 < time2 else time2
    delta = abs((int(time / sleep1) * jump_distance1 + pos1) - (int(time / sleep2) * jump_distance2 + pos2))
    max_jump = least_common_multiple(sleep1, sleep2) * jump_distance1 / sleep1 \
        if jump_distance1 / sleep1 > jump_distance2 / sleep2 \
        else least_common_multiple(sleep1, sleep2) * jump_distance2 / sleep2

    while True:
        if sleep1 == sleep2:
            time = time1
            time1 += sleep1
        else:
            if time1 < time2:
                time = time1
                time1 += sleep1
            else:
                time = time2
                time2 += sleep2

        disk_time1 = math.floor(time / sleep1) if (jump_distance1 / sleep1) % 1 == 0 and jump_distance1 / sleep1 != 1 \
            else math.ceil(time / sleep1)
        disk_time2 = math.floor(time / sleep2) if (jump_distance2 / sleep2) % 1 == 0 and jump_distance2 / sleep2 != 1 \
            else math.ceil(time / sleep2)

        if time % least_common_multiple(sleep1, sleep2) == 0:
            delta = abs((disk_time1 * jump_distance1 + pos1) - (disk_time2 * jump_distance2 + pos2))
            max_jump = least_common_multiple(sleep1, sleep2) * jump_distance1 / sleep1 \
                if disk_time1 * jump_distance1 + pos1 < disk_time2 * jump_distance2 + pos2 \
                else least_common_multiple(sleep1, sleep2) * jump_distance2 / sleep2

        if time != prev_time and disk_time1 * jump_distance1 + pos1 == disk_time2 * jump_distance2 + pos2:
            return disk_time1 * jump_distance1 + pos1

        if (time != prev_time and delta > prev_delta and prev_delta > max_jump) or \
                (time != prev_time and time % least_common_multiple(sleep1, sleep2) == 0 and delta == prev_delta):
            return -1

        if time % least_common_multiple(sleep1, sleep2) == 0:
            prev_delta = delta

        prev_time = time


if __name__ == '__main__':
    meet_me(1, 2, 1, 2, 1, 1)  # = > 3
#     meet_me(1, 2, 3, 4, 5, 5)  # = > -1
#     meet_me(10, 7, 7, 5, 8, 6)  # = > 45
    meet_me(100, 7, 4, 300, 8, 6)  # = > 940
    meet_me(1, 7, 1, 15, 5, 1)  # = > 50
#     meet_me(0, 1, 1, 1, 1, 1)  # = > -1
