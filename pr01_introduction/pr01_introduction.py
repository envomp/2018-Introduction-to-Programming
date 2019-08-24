def introduce():
    """Write a function which asks user name and gives suitable answer."""
    name = input("Hello, my name is Python! Please type your name to continue our conversation.")
    answer = input("Have you programmed before?")
    if answer == "Yes":
        print(f"Congratulations, {name}! It will be a little bit easier for you.")
    elif answer == "No":
        print(f"Don`t worry, {name}! You will learn everything you need.")
    else:
        print("Please answer Yes or No!")


if __name__ == "__main__":  # <- This line is needed for automatic testing
    introduce()
