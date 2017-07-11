
factorial = lambda n: reduce( lambda x, y: x*y, [1]+range(1, n))
combinations = lambda n, r: factorial(n) / factorial(r) / factorial(n-r)
is_pal = lambda n: int(str(n)[::-1]) == n

def primes_up_to(limit):
    primes = [2]
    current_counter = 3

    while primes[-1] < limit:
        is_prime = True
        for p in primes:
            if p*p > current_counter:
                break
            if current_counter % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(current_counter)
        current_counter += 1
    primes.pop()
    return primes

def make_n_primes(n):
    primes = [2]
    current_counter = 3

    while len(primes) < n:
        is_prime = True
        for p in primes:
            if p*p > current_counter:
                break
            if current_counter % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(current_counter)
        current_counter += 1
    return primes

def factorize_into_primes( n, primes ):
    current_quotient, prime_factors, primes_index = n, [], 0
    while current_quotient > 1:
        p = primes[ primes_index ]
        while current_quotient % p == 0:
            current_quotient /= p
            prime_factors.append(p)
        primes_index += 1
    return prime_factors

