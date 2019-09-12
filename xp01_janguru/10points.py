def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    alpha_a, alpha_b, possible_answers = jump_distance1 / sleep1, jump_distance2 / sleep2, []
    y_base_offset_a, y_base_offset_b = pos1 + jump_distance1, pos2 + jump_distance2
    if pos1 + jump_distance1 == pos2 + jump_distance2:
        return pos1 + jump_distance1
    for i in range(sleep1 + sleep2):
        try:
            if i >= sleep1:
                y_current_offset_a = y_base_offset_a
                y_current_offset_b = y_base_offset_b - (i - sleep1) * alpha_b
            else:
                y_current_offset_a = y_base_offset_a - i * alpha_a
                y_current_offset_b = y_base_offset_b
            x = round((y_current_offset_b - y_current_offset_a) / (alpha_a - alpha_b), 3)
            if not x.is_integer():
                continue
            y = alpha_a * x + y_base_offset_a if i >= sleep1 else alpha_b * x + y_base_offset_b
            if (y - pos1) % jump_distance1 == (y - pos2) % jump_distance2 == 0:
                possible_answers.append(int(y))
        except ZeroDivisionError:
            if y_current_offset_a == y_current_offset_b:
                cycle_mean = int(round(alpha_a * y_current_offset_a + y_current_offset_a, 0))
                return -1 if cycle_mean > y_base_offset_a and cycle_mean > y_current_offset_b else cycle_mean
    possible_answers = list(filter(lambda xi: xi >= y_base_offset_a and xi >= y_current_offset_b, possible_answers))
    return -1 if possible_answers.__len__() == 0 else min(possible_answers)


if __name__ == '__main__':
    print(meet_me(10, 7, 7, 5, 8, 6))
