import time

def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

def new_approach(n):

    start = time.time()

    # We'll check primes up until this number
    largest_divisor = int(n/2)
    flag_prime = 0

    if largest_divisor % 2 == 0:
        largest_divisor = largest_divisor - 1

    while (largest_divisor > 1):
        # Let's see if i is a divisor of n, starting by half of n, which is variable largest_divisor
        if (n % i == 0):
            flag_divisor = 1
            # i is a divisor of the original number, so let's check if it's a prime
            sum_of_digits = sum_digits(i)
            ## checking if i is a prime
            for ii in range (i-1,1,-2):
                #it's not required to check if it's even
                if (sum_of_digits % 3 == 0):
                    # not a prime
                    flag_prime = 0
                elif (i % ii == 0):
                    # not a prime
                    flag_prime = 0
                else:
                    #it's a prime
                    flag_prime = 1
        else:
            largest_divisor = largest_divisor - 1
        if flag_prime == 1:
            break

    largest_divisor = i

    elapsed = time.time() - start

    print (largest_divisor,"\n", elapsed,"\n")
    
    return

new_approach(40)
