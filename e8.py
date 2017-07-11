        
import time
from string_literals import e8_raw_digit_string

def e8():
    adjancency_length, max_prod = 13, 0
    digits = ''.join( e8_raw_digit_string.strip().split() )
    for start_index in xrange( len(digits) - adjancency_length ):
        current_prod = 1
        for char_index in xrange( start_index, start_index + adjancency_length ):
            current_prod *= int( digits[char_index] )
        if current_prod > max_prod:
            max_prod = current_prod
    return max_prod

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 8 solution is:",  e8()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
