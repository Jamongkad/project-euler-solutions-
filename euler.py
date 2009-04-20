#!/usr/bin/env python
import math

def recursive_each(list, counter=0, callback=None):
    results = []
    if counter < len(list):
        results.append(callback(list[counter]))
        each(list, counter+1, callback)
    
    return results

def each(list, callback=lambda x : x):
    results = [callback(i) for i in list] 
    return results

def fact(x):
    if x == 0:
        return 1
    else: 
        return x * fact(x-1)

#memoized version
def fib(n):
   memo = {}
   if n not in memo: 
       memo[n] = fib(n-1) + fib(n-2)
   return memo[n]

#generative version
def ifib():
    a, b = 0, 1
    while 1: 
        yield a
    a, b = b, a + b

#euler version
def efib(maxNumber): 
    a, b = 0, 1
    while a < maxNumber:
        if a % 2 ==0:
            yield a
        a, b = b, a + b

def primes(n, factor):  
    factors = []
    while(n % factor != 0):
        factor += 1
        factors.append(factor)
    
    if n > factor:
        factors.extend(primes(n / factor, factor))

    return factors  
