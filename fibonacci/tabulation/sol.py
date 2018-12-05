#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(): 
    n = 888
    fib = []
    fib.append(0)
    fib.append(1)
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])

    # Declaration of lookup table 
    # Handles till n = 100 
    print ("Fibonacci Number is ", fib[n] )

if __name__=="__main__":
    import time

    start_time = time.time()
    # time.sleep(1)
    main()
    end_time = time.time()

    time_diff = end_time - start_time
    print("--- {} seconds ---".format(time_diff))


# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
