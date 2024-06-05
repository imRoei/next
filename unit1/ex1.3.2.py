def is_prime(number):
    return all(number % i for i in range(2, number))

print(is_prime(43))