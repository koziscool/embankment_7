        
import time
from utils import combinations 

def e15():
    pascal_triangle_row = lambda n: map( lambda i: combinations(n, i), xrange(n+1) )
    return sum(map(lambda n:n*n, pascal_triangle_row(20)))

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 15 solution is:",  e15()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
