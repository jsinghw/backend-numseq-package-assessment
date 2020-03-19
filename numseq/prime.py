def primes(n):
    '''Return primes less than n'''
    # https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
    # Sieve of Eratosthenes
    if n < 1:
        return []
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime_list = []
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] is True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Print all prime numbers
    for p in range(n+1):
        if prime[p]:
            prime_list.append(p)
    return prime_list


def is_prime(m):
    '''Checks to see if m is  prime'''
    primes_list = primes(m)
    if m in primes_list:
        return True
    else:
        return False


print(is_prime(11))
