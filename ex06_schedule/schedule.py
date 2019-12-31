"""Create schedule from the given file."""
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """
    Create schedule file from the given input file.

    :param input_filename: Input file
    :param output_filename: Output file
    :return: None
    """
    with open(input_filename, encoding='utf-8') as file:
        text = file.read()

    with open(output_filename, mode='w', encoding='utf-8') as file:
        file.write(create_schedule_string(text))


def create_table(schedule: dict) -> list:
    """
    Create table and return list of table rows.

    :param schedule: schedule dictionary
    :return: list of table rows
    """
    table = []

    if not len(schedule):  # schedule is empty
        items_width = 6
        time_width = 5
    else:
        items_width = 5  # Length of header word 'items'
        time_width = 7  # Length of time '1:00 AM'

    for time in schedule:
        if len(get_formatted_time(time)) > time_width:
            time_width = len(get_formatted_time(time))
        if len(schedule[time]) > items_width:
            items_width = len(schedule[time])

    # Table header
    table.append("-" * (7 + time_width + items_width))
    table.append("| {:>{}} | {:<{}} |".format("time", time_width, "items", items_width))
    table.append("-" * (7 + time_width + items_width))

    if len(schedule):
        for time in sorted(schedule):
            am_pm_time = get_formatted_time(time)
            table.append(f"| {am_pm_time:>{time_width}} | {schedule[time]:<{items_width}} |")
    else:
        table.append("| No items found |")

    table.append("-" * (7 + time_width + items_width))

    return table


def create_schedule_string(input_string: str) -> str:
    """
    Create schedule string from the given input string.

    :param input_string: Input text string
    :return: Schedule table string
    """
    schedule = {}

    regex = r"(?:(?<=[ \n])|(?<=^))([0-9]{1,2})[^0-9]([0-9]{1,2})[ \n]+([a-z]+)"

    for match in re.finditer(regex, input_string, re.IGNORECASE):
        time = normalize(match.group(1) + ":" + match.group(2))

        if time is not None:
            if not schedule.get(time):
                schedule[time] = match.group(3).lower()
            elif match.group(3).lower() not in schedule[time]:  # duplicates not allowed
                schedule[time] = schedule[time] + ", " + match.group(3).lower()

    return "\n".join(create_table(schedule))


def normalize(input_time: str):
    """
    Add missing 0's to the minutes and hours.

    :param input_time: time string w/o leading zeroes
    :return: normalized time string
    """
    if not len(input_time):
        return None

    hours = int(input_time[:input_time.find(":")])
    mins = int(input_time[input_time.find(":") + 1:])

    if 0 <= hours < 24:  # if hours are correct
        hours = str(hours).zfill(2)
    else:
        return None

    if 0 <= mins < 60:  # if mins are correct
        mins = str(mins).zfill(2)
    else:
        return None

    return f"{hours}:{mins}"


def get_formatted_time(input_time: str) -> str:
    """Format 24 hour time to the 12 hour time.

    Why not to use strftime()?
    Because format code %-I (12-hour clock as a decimal number) is Platform specific

    :param input_time: 24 hour time
    :return: 12 hour time
    """
    if not len(input_time):
        return ""

    am_pm = "AM"

    if input_time.find(":"):
        hours = int(input_time[:input_time.find(":")])
        mins = int(input_time[input_time.find(":") + 1:])

        if 0 <= hours < 24 and 0 <= mins < 60:
            if int(hours / 12):
                am_pm = "PM"

            hours = hours % 12

            if not hours:  # 00:00 and 12:00
                hours = 12

            return f"{hours}:{str(mins).zfill(2)} {am_pm}"


if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
