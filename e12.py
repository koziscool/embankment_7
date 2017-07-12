        
import time
from utils import num_divisors, primes_up_to

def e12():
    triangle = lambda n: n*(n+1)/2
    primes = primes_up_to(10**5)
    current_counter = 1

    while num_divisors( triangle( current_counter ), primes) <= 500:
        current_counter += 1
    return triangle( current_counter )

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 12 solution is:",  e12()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
