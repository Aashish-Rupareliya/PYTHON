def get_odd_number():
    try:
        number = int(input("Enter an odd number: "))
        if number % 2 == 0:
            raise ValueError("This is not an odd number.")
        print(f"{number} is an odd number.")
    except ValueError as ve:
        print(ve)

get_odd_number()
