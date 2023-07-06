import math

def calculate_cylinder_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def calculate_cylinder_area(radius, height):
    base_area = math.pi * radius**2
    lateral_area = 2 * math.pi * radius * height
    total_area = 2 * base_area + lateral_area
    return total_area


radius = 3
height = 5

cylinder_volume = calculate_cylinder_volume(radius, height)
cylinder_area = calculate_cylinder_area(radius, height)

print(f"The volume of the cylinder is: {cylinder_volume}")
print(f"The total surface area of the cylinder is: {cylinder_area}")
