import random

def read_random_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        return random_line.strip()


filename = 'sample.txt'  # Replace with your file path
random_line = read_random_line(filename)
print("Random Line:", random_line)
