def calculate_trapezoid_area(base1, base2, height):
    area = (base1 + base2) * height / 2
    return area

base1 = 5
base2 = 7
height = 4
trapezoid_area = calculate_trapezoid_area(base1, base2, height)
print(f"The area of the trapezoid is: {trapezoid_area}")
