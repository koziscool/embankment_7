        
import time
from utils import primes_up_to

def e10():
    return sum( primes_up_to(2 * 10 ** 6))

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 10 solution is:",  e10()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
