"""isPrime.py

Tests if number is prime or not
"""

def is_prime(num):
    for n in range(2,int(num/2)):
        if (num % n == 0):
            return "Nope! Div by "+str(n)

    return "Prime!"
