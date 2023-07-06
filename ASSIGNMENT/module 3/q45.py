def find_max_min(numbers):
    if len(numbers) == 0:
        return None
    else:
        maximum = max(numbers)
        minimum = min(numbers)
        return maximum, minimum

decimal_numbers = [3.14, 2.718, 1.618, 0.577, 2.236]
max_num, min_num = find_max_min(decimal_numbers)

print(f"Decimal Numbers: {decimal_numbers}")
print(f"Maximum Number: {max_num}")
print(f"Minimum Number: {min_num}")
