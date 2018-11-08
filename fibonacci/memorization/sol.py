#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fib(n, lookup):
	if lookup[n] != None:
		return lookup[n]
	else:
		if n == 0:
			return 0
		if n == 1:
			return 1
		else:
			lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)
			return lookup[n]

# Driver program to test the above function 
def main(): 
	n = 34
	# Declaration of lookup table 
	# Handles till n = 100 
	lookup = [None]*(101) 
	print ("Fibonacci Number is ", fib(n, lookup) )

if __name__=="__main__": 
	main() 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
# modified by gaojx
