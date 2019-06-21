import string

import pytest
import schedule
import random

empty_table = "------------------\n" + \
"|  time | items  |\n" + \
"------------------\n" + \
"| No items found |\n" + \
"------------------"

correct_table = "---------------------\n" + \
"|    time | items   |\n" + \
"---------------------\n" + \
"| 3:03 PM | correct |\n" + \
"---------------------"

def _create_table(rows):
    table_list = []
    timelen = max(4, max(len(x[0]) for x in rows))
    itemslen = max(5, max(len(x[1]) for x in rows))
    linerow = "-" * (7 + timelen + itemslen)
    table_list.append(linerow)
    table_list.append(f'| {"time":>{timelen}} | {"items":<{itemslen}} |')
    table_list.append(linerow)
    for row in rows:
        table_list.append(f'| {row[0]:>{timelen}} | {row[1]:<{itemslen}} |')
    table_list.append(linerow)
    return "\n".join(table_list)

def _check_table(text, expected):
    actual = schedule.create_schedule_string(text).strip()
    assert actual == expected.strip(), f"text:\n{text}\n\nactual:\n{actual}\n\nexpected:\n{expected}"

@pytest.mark.timeout(1.0)
def test_empty_text():
    assert schedule.create_schedule_string("").strip() == empty_table.strip()

@pytest.mark.timeout(1.0)
def test_no_times():
    _check_table("tere tere siin pole uhtegi kellaaega, aga moned numbrid on nagu 12 h .", empty_table)

@pytest.mark.timeout(1.0)
def test_simple_short_time_one_digit_hour():
    # this test is required for all the rest
    _check_table("go 15:03 correct done", correct_table)

@pytest.mark.timeout(1.0)
@pytest.mark.incgroup("correct")
def test_simple_correct_time():
    # this test is required for all the rest
    _check_table("go 15:03 correct done", correct_table)


@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_time_too_large():
    _check_table("s 24:00 wrong 23:60 wrong 11:66 wrong 15:03 correct 77:77 wrong done.", correct_table)

@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_time_wrong_separator():
    _check_table("s 11234 wrong 1112 wrong 123 wrong 15:03 correct 1000 wrong done.", correct_table)

@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_time_no_activity():
    _check_table("s 11:34 12:45 .  15:03 correct 11:12  ", correct_table)

@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_time_too_long():
    _check_table("s 111:34 wrong 12:451 wrong   15:03 correct 011:012 wrong 000:1 wrong ", correct_table)

@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_time_activity_ends_without_space():
    _check_table("jj  15:03 correct1a hj", correct_table)
    _check_table("jj  15:03 correct.a hj", correct_table)
    _check_table("jj  15:03 correct-b hj", correct_table)

@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_time_wrong_spacing():
    _check_table("s 11:34wrong wrong12:45 wrong  15:03 correct wrong11:12wrong", correct_table)

@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_time_with_multiple_spaces():
    _check_table("s asfasf  15:03       correct   11:12asdf", correct_table)

@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_time_correct_separator():
    for sep in "- q\\'\",.;´":
        _check_table(f"s asdf  15{sep}03 correct asfd", correct_table)

@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_duplicate_activities_with_same_time():
    _check_table("s 15:03 correct aa  15:03 correct 15:03 correct 15:3 correct ", correct_table)

@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_duplicate_activities_different_cases_with_same_time():
    _check_table("s 15:03 correcT aa  15:03 Correct 15:03 CORRECT", correct_table)

@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_short_time():
    table = _create_table([("1:12 AM", "abc")])
    _check_table("here 01:12 abc some more", table)

@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_multiple_activities_same_time():
    table = _create_table([("1:12 AM", "abc, def")])
    _check_table("here 01:12 abc some more 01:12 def", table)

@pytest.mark.timeout(1.0)
@pytest.mark.incgroupdepend("correct")
def test_multiple_activities_same_time_original_order():
    table = _create_table([("1:12 AM", "def, abc, yes")])
    _check_table("here 01:12 def some more 01:12 abc 1:12 YES", table)

def _random_time(minh, maxh, minm, maxm):
    h = random.randint(minh, maxh)
    m = random.randint(minm, maxm)
    sep = random.choice(":,.-!?abAB=")
    timetuple = None
    if h in range(0, 24) and m in range(0, 60):
        h12 = h
        ampm = "AM"
        if h == 0:
            h12 = 12
        elif h == 12:
            ampm = "PM"
        elif h > 12:
            h12 = h - 12
            ampm = "PM"
        time12h = f"{h12}:{m:02} {ampm}"
        timetuple = (h, m, time12h)

    return f"{h:0{random.randint(1, 2)}}{sep}{m:0{random.randint(1, 2)}}", timetuple

def _random_str(minlen, maxlen):
    return "".join(random.choices(string.ascii_lowercase, k=random.randint(minlen, maxlen)))

def _random_upper(s):
    return "".join([random.random() > 0.5 and x.upper() or x for x in s])

def _random_test(n=100, activities_size=10, max_item_count=100):
    activities = []
    for _ in range(activities_size):
        activities.append(_random_str(5, 10))

    print(activities)
    for _ in range(n):
        item_count = random.randint(10, max_item_count)
        d = {}
        text_list = []
        # some noise
        for _ in range(random.randint(0, 10)):
            text_list.append(_random_str(5, 10))
        for i in range(item_count):
            timestr, timetuple = _random_time(-1, 25, -1, 60)
            activity = random.choice(activities)
            text_list.append(timestr + " " * random.randint(1, 4) + _random_upper(activity))
            if timetuple is not None:
                minutes = timetuple[0] * 60 + timetuple[1]
                if minutes not in d:
                    d[minutes] = []
                if activity not in [x[3] for x in d[minutes]]:
                    d[minutes].append(timetuple + (activity, ))
            # some noise
            for _ in range(random.randint(0, 10)):
                text_list.append(_random_str(5, 10))

        # let's start with space to simplify
        text = "start " + " ".join(text_list)
        # print("---")
        # print(text)

        actual_output = schedule.create_schedule_string(text)
        sd = sorted(d.items(), key=lambda x: x[0])
        # print("---")
        # print(sd)
        # (281, [(4, 41, '4:41 AM', 'xrwnaao'), (4, 41, '4:41 AM', 'bzqpiut')])
        max_len_time = max([len(x[1][0][2]) for x in sd])
        max_len_activities = max([len(", ".join(y[3] for y in x[1])) for x in sd])

        max_len_time = max(4, max_len_time)
        max_len_activities = max(5, max_len_activities)
        expected_list = []
        expected_list.append("-" * (7 + max_len_activities + max_len_time))
        expected_list.append(f"| {'time':>{max_len_time}} | {'items':<{max_len_activities}} |")
        expected_list.append("-" * (7 + max_len_activities + max_len_time))
        for el in sd:
            expected_list.append(f"| {el[1][0][2]:>{max_len_time}} | {', '.join(x[3] for x in el[1]):<{max_len_activities}} |")

        expected_list.append("-" * (7 + max_len_activities + max_len_time))
        # print("\n".join(expected_list))
        # print(actual_output)
        expected = "\n".join(expected_list)
        _check_table(text, expected)
        # assert actual_output == expected, f"text:\n{text}\n\nactual:\n{actual_output}\n\nexpected:\n{expected}"

@pytest.mark.timeout(10.0)
@pytest.mark.weight(5)
def test_random_small():
    _random_test(2, max_item_count=20)


@pytest.mark.timeout(10.0)
@pytest.mark.weight(10)
def test_random_medium():
    _random_test(10, max_item_count=50)

@pytest.mark.timeout(10.0)
@pytest.mark.weight(10)
def test_random_large():
    _random_test(100, max_item_count=400)