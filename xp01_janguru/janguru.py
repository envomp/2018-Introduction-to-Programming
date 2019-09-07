def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    alpha_a = jump_distance1 / sleep1
    y_base_offset_a = pos1 + jump_distance1

    alpha_b = jump_distance2 / sleep2
    y_base_offset_b = pos2 + jump_distance2

    possible_answers = []

    for i in range(sleep1 + sleep2):
        try:
            if i >= sleep1:
                i -= sleep1
                y_current_offset_a = y_base_offset_a
                y_current_offset_b = y_base_offset_b - i * alpha_b
            else:
                y_current_offset_a = y_base_offset_a - i * alpha_a
                y_current_offset_b = y_base_offset_b
            x = round((y_current_offset_b - y_current_offset_a) / (alpha_a - alpha_b), 10)
            y1 = alpha_a * x + y_base_offset_a
            y2 = alpha_b * x + y_base_offset_b
            if (y1 - pos1) % jump_distance1 == (y1 - pos2) % jump_distance2 == 0:
                possible_answers.append(int(y1))
            if (y2 - pos1) % jump_distance1 == (y2 - pos2) % jump_distance2 == 0:
                possible_answers.append(int(y2))
        except ZeroDivisionError:
            if y_current_offset_a == y_current_offset_b:
                print(alpha_b * y_current_offset_a + y_base_offset_b)
    possible_answers = list(filter(lambda xi: xi >= y_base_offset_a and xi >= y_current_offset_b, possible_answers))
    return -1 if possible_answers.__len__() == 0 else min(possible_answers)


if __name__ == '__main__':
    print(meet_me(1, 2, 1, 1, 2, 1))
    print(meet_me(1, 7, 1, 15, 5, 1))
