
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

    print (divisors,"\n", elapsed)
    
    return divisors

# Let´s test if the algorithm is working properly
divisors = divisors_1(95)
```

    [1, 5, 19, 95] 
     9.059906005859375e-06


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

    print (primes,"\n", elapsed)
    
    return primes

primes = primes_1(95)
```

    [1, 2, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89] 
     0.0002231597900390625


We now have built two important blocks of code. Porém, vamos primeiramente fazer um teste com o número acima, encontrando a intersecção dos conjuntos apresentados.


```python
set(divisors).intersection(primes)
```




    {1, 5, 19}



It all looks very nice and perfect, until you realise that 600851475143 is a huge number - it looks like you are dialing a phone number in South Africa. We need to deal with it.

### Melhorias no algoritmo

Devemos encontrar o maior divisor primo de 600851475143, sendo assim a primeira coisa a fazer é melhorar a eficiência deste algoritmo já que o número é gigantesco.

- A checagem dos divisores pode parar quando o número analisado atinge a metade

### Using a different approach

Let's get the divisors of n/2 and then, for each, check if it's a prime number. We can keep on decreasing n as we go. Also, to check if the number is a prime, we do things like "check if the number is even" (that would make it not a prime), check if the sum of its algarisms is a multiple of 3 (so it's a multiple of 9) and so on, to make the process of finding if it's a prime a little more simple.


```python
import time

def new_approach(n):

    start = time.time()

    # Descobriremos os primos até deste número
    middle = int(n/2)
    largest = middle

    for i in range (middle,1,-1):
        # Let's see if i is a divisor of n, starting with half of n (any number above that isn't)
        if (n % i == 0):
            # i is a divisor, but we still need to check wether it's a prime number
            
            # Here we can simplify the problem: if n is even, ii will start on an
            # odd number. We can set the passo as 2 by 2. (i-1,1,-2)
            # Do the same if n is odd, but start the range in (i,1,-2)
            
            for ii in range (i-1,1,-1):
                largest = i # For now, i is winning the challenge
                if (i % ii == 0):
                    # i is not a prime number
                    primo = 0
                    break
                else:
                    # i is a prime number
                    primo = 1

            if primo == 1:
                break

    largest = i

    elapsed = time.time() - start

    print (largest,"\n", elapsed, middle)
    
    return

new_approach(13195)
```

    29 
     0.0009982585906982422 6597



```python

```

https://en.wikipedia.org/wiki/Divisibility_rule#Composite_divisors


```python
import time

def new_approach(n):

    start = time.time()

    # We'll check primes up until this number
    middle = int(n/2)
    largest = middle
    list = [1]

    for i in range (middle,2,-1):
        # Vamos avaliar se i é divisor do original n, começando pela metade dele
        if (n % i == 0):
            # i é divisor, precisamos ver se é prime
            for ii in range (i-1,2,-1): # Finalizando com o 2 já que obviamente todos são divisíveis por 1
                largest = i # Here we can modify the "check if it's a prime" part of the algorithm
                
                if (par):
                    prime = 0
                    break
                
                elif (soma dos algarismos % 3 == 0)
                    prime = 0
                    break

                elif (last two digits % 4 == 0)
                    prime = 0
                    break
                
                elif (i % ii == 0):
                    # i is not a prime
                    prime = 0
                    break

                else:
                    # é primo
                    primo = 1

            if primo == 1:
                break

    largest = i

    elapsed = time.time() - start

    print (largest,"\n", elapsed,"\n", list)
    
    return

new_approach(1319574)
```
