def check_perfect_number(number):
    if number <= 0:
        return False

    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)

    if sum(divisors) == number:
        return True
    else:
        return False


number = 28
is_perfect = check_perfect_number(number)
print(f"The number {number} is perfect: {is_perfect}")
