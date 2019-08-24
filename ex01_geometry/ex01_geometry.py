import math


def calculate_area():
    shape = input("Please insert geometric shape:")
    dimension = float(input("Please insert radius or side length in cm:"))
    if shape == "triangle":
        print(f"The area is {dimension**2 / 4 * math.sqrt(3)} cm^2")
    elif shape == "circle":
        print(f"The area is {3.14 * dimension**2} cm^2")
    elif shape == "square":
        print(f"The area is {dimension**2} cm^2")
    else:
        print("Shape is not supported.")


if __name__ == '__main__':
    calculate_area()
