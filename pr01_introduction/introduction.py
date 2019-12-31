"""My first program."""


def conversation() -> None:
    """
    Little conversation with user.

    :return: None
    """
    name = input("Hello, my name is Python! Please type your name to continue our conversation. ").capitalize()
    answer = input("Have you programmed before? ").lower()

    if answer == 'yes':
        print(f"Congratulations, {name}! It will be a little bit easier for you.")
    elif answer == 'no':
        print(f"Don`t worry, {name}! You will learn everything you need.")
    else:
        print("Your input is incorrect!")


if __name__ == '__main__':
    conversation()
