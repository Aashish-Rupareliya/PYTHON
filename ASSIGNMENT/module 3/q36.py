def check_number_in_range(number, start, end):
    if start <= number <= end:
        return True
    else:
        return False

number = 7
start_range = 1
end_range = 10
is_in_range = check_number_in_range(number, start_range, end_range)
print(f"The number {number} is in the range [{start_range}, {end_range}]: {is_in_range}")
