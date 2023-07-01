import random

def select_random_item(item_list):
    random_item = random.choice(item_list)
    return random_item


fruits = ["apple", "banana", "orange", "grape", "mango"]
random_fruit = select_random_item(fruits)
print("List of fruits:", fruits)
print("Randomly selected fruit:", random_fruit)
