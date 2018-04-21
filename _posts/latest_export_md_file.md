
## Problem #3

The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?

### Solution #1

We can use the following algorithm to build a list with all divisors of `n`:


```python
import time

def divisors_1(n):

    start = time.time()

    # The number 1, obviously, will always be a divisor, so let's
    # initiate the list with it
    divisors = [1]

    for i in range (2,n+1): # Começando com o 2 já que obviamente todos são divisíveis por 1
        if n % i == 0:
            divisors.append(i)

    elapsed = time.time() - start
    
    return divisors

# Let´s test if the algorithm is working properly
divisors = divisors_1(95)
print (divisors,"\n", elapsed)
```

    [1, 5, 19, 95] 
     0.10687780380249023


Ok, it's all good. Now let's build a short code that evaluates all prime numbers from 1 to `n`:


```python
import time

def primes_1(n):

    start = time.time()

    # The number 1 is a prime number. Therefore, we shall start the list with it.
    primes = [1,2]

    for candidate_for_prime in range (3,n+1):
        # Let's evaluate all primes up till n
        # since all primes are odd, we can save some computing time
        # by using 2 as step and starting with 3
        
        for i in range (3,candidate_for_prime): 
            if (candidate_for_prime % i == 0):
                break
            elif ((candidate_for_prime % i != 0) & (i + 1 == candidate_for_prime)):
                primes.append(candidate_for_prime)

    elapsed = time.time() - start

    #print (primes,"\n", elapsed)
    
    return primes

primes = primes_1(95)
print (primes,"\n", elapsed)
```

    [1, 2, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89] 
     0.10687780380249023


We now have built two important blocks of code. Let'sdo a little test to find the intersection of the two sets above:


```python
set(divisors).intersection(primes)
```




    {1, 5, 19}



It all looks very nice and perfect, until you realise that 600851475143 is a huge number - it looks like you are dialing a phone number in South Africa. We need to deal with it. Are we really going to have a problem with this huge number? Let's test it with a pretty-big-but-not-huge number:


```python
import time

start = time.time()

divisors = divisors_1(32395)
primes = primes_1(32395)

print (set(divisors).intersection(primes))

elapsed = time.time() - start

print (elapsed)
```

    {1, 5, 11, 19, 31}
    14.906361103057861


Yes we will have an issue with this.

## Improvements on the algorithm

### Solution #2 - Trial Division algorithm

(explain trial division...)


```python
from math import sqrt
import time

def trial_division(n):
    factors = []
    for i in range (2,int(sqrt(n))):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n/i))
    return factors

start = time.time()

factors = trial_division(600851475143)
factors.sort()
print (factors)
              
elapsed = time.time() - start
```

    [71, 839, 1471, 6857, 59569, 104441, 486847, 1234169, 5753023, 10086647, 87625999, 408464633, 716151937, 8462696833]


We still need to check if they are primes. If they are divisible by each other, they must be eliminated.


```python
from math import sqrt
import time

def trial_division_primes(n):
    factors = []
    for i in range (2,int(sqrt(n))):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n/i))
    
    # We need to sort it, otherwise the algorithm won't work
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
```

    [71, 839, 1471, 6857]


Drop the mic.
