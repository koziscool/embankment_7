        
import time

def e1():
    return sum(filter( lambda n: n%3 == 0 or n%5 ==0, xrange(1, 1000)))

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 1 solution is:",  e1()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
