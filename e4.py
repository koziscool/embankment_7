        
import time
from utils import is_pal

def e4():
    max_pal = 0
    for i in xrange(100, 1000):
        for j in xrange(i+1, 1000):
            if is_pal(i*j) and i*j > max_pal:
                max_pal = i*j
    return max_pal

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 4 solution is:",  e4()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
