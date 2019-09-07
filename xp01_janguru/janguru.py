def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    alpha_a = jump_distance1 / sleep1
    y_base_offset_a = pos1 + jump_distance1

    alpha_b = jump_distance2 / sleep2
    y_base_offset_b = pos2 + jump_distance2

    possible_answers = []

    for i in range(sleep1):
        try:
            y_current_offset_a = y_base_offset_a - i * alpha_a
            y_current_offset_b = y_base_offset_b
            x = round((y_current_offset_b - y_current_offset_a) / (alpha_a - alpha_b), 10)
            y = alpha_a * x + y_base_offset_a
            print(x)
            if (y - pos1) % jump_distance1 == (y - pos2) % jump_distance2 == 0:
                possible_answers.append(int(y))
        except Exception:
            continue

    for j in range(sleep2):
        try:
            y_current_offset_a = y_base_offset_a
            y_current_offset_b = y_base_offset_b - j * alpha_b
            x = round((y_current_offset_b - y_current_offset_a) / (alpha_a - alpha_b), 10)
            y = alpha_a * x + y_base_offset_a
            print(x)
            if (y - pos1) % jump_distance1 == (y - pos2) % jump_distance2 == 0:
                possible_answers.append(int(y))
        except Exception:
            continue
    print()
    return -1 if possible_answers.__len__() == 0 else min(possible_answers)
