import math

shape = input("Please insert geometric shape:")
if shape == "circle":
    radius = float(input("Please insert radius in cm:"))
    area = math.pi * radius**2
    print(f"The area is {round(area, 2)} cm^2")
elif shape == "square":
    length = float(input("Please insert side length in cm:"))
    area = length**2
    print(f"The area is {round(area, 2)} cm^2")
elif shape == "triangle":
    length = float(input("Please insert side length in cm:"))
    area = math.sqrt(3) * length**2 / 4
    print(f"The area is {round(area, 2)} cm^2")
else:
    print("Shape is not supported.")