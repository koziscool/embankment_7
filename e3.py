        
import time
from utils import primes_up_to, factorize_into_primes

def e3():
    return max( factorize_into_primes(600851475143, primes_up_to(10**6) ) )

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 3 solution is:",  e3()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
