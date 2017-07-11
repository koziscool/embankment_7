        
import time

def e2():
    fibo = [1, 2]
    while fibo[-1] < 4 * 10 ** 6:
        fibo.append( fibo[-1] + fibo[-2] )
    fibo.pop()

    return sum(filter(lambda n:n%2 == 0, fibo))

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 2 solution is:",  e2()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
