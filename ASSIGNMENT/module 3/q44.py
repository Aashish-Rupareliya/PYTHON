def sum_of_divisors(number):
    divisors_sum = 0
    for i in range(1, number + 1):
        if number % i == 0:
            divisors_sum += i
    return divisors_sum

number = 12
divisors_sum = sum_of_divisors(number)
print(f"The sum of divisors of {number} is: {divisors_sum}")
