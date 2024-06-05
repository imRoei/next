def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_generator(n):
    number = n+1
    while True:
        if is_prime(number):
            yield number
        number += 1

def first_prime_over(n):
    return(next(prime_generator(n)))

print(first_prime_over(1000000))


