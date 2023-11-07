def prime_checker(number):
    # check for prime number
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number}'s a prime number.")
    else:
        print(f"{number}'s not a prime number.")


n = int(input())  # Check this number
for i in range(2, n):
    prime_checker(number=i)

