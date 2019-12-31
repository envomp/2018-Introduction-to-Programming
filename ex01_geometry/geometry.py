"""Ask user a shape and a radius or a side length and calculate the shape area."""
import math


def calculate_area() -> None:
    """
    Ask shape and radius or side length and calculate the shape area.

    :return: None
    """
    shape = input("Please insert geometric shape: ")
    if shape == "square" or shape == "triangle":
        side = float(input("Please insert side length in cm: "))
        if shape == "square":
            area = round(side ** 2, 2)
        else:
            area = round(math.sqrt(3) / 4 * side ** 2, 2)
        print(f"The area is {area} cm^2")
    elif shape == "circle":
        radius = float(input("Please insert radius in cm: "))
        area = round(math.pi * radius ** 2, 2)
        print(f"The area is {area} cm^2")
    else:
        print("Shape is not supported.")


if __name__ == "__main__":
    calculate_area()
