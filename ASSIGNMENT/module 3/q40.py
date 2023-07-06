import math

def degree_to_radian(degrees):
    radians = math.radians(degrees)
    return radians

degrees = 45
radians = degree_to_radian(degrees)
print(f"{degrees} degrees is equal to {radians} radians.")
