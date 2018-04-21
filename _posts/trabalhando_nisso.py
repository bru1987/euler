from math import sqrt
import time

def trial_division_primes(n):
    factors = []
    for i in range (2,int(sqrt(n))):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n/i))

    factors.sort()        
    prime_factors = factors
    to_remove = []
    
    for i in range (len(factors)-1,0,-1):
        a = i-1
        for ii in range (a,-1,-1):
            if prime_factors[i] % prime_factors[ii] == 0:
                to_remove.append(prime_factors[i])
            a = a - 1
    
    prime_factors = list(set(set(prime_factors) - set(to_remove)))

    return prime_factors

start = time.time()

prime_factors = trial_division_primes(600851475143)
prime_factors.sort()
print (prime_factors)
              
elapsed = time.time() - start