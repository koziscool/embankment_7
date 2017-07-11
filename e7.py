        
import time
from utils import make_n_primes

def e7():
    return make_n_primes(10001)[-1]

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 7 solution is:",  e7()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
