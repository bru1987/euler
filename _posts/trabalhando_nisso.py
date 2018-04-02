import time

def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

def new_approach(n):

    start = time.time()

    # We'll check primes up until this number
    largest_possible_divisor = int(n/2)
    flag_prime = 0
    flag_divisor = 0

    if largest_possible_divisor % 2 == 0:
        largest_possible_divisor = largest_possible_divisor - 1

    for i in range (largest_possible_divisor,1,-1):
        # Let's see if i is a divisor of n, starting by half of n, which is variable largest_possible_divisor
        if (n % i == 0):
            flag_divisor = 1
            # i is a divisor of the original number, so let's check if it's a prime
            sum_of_digits = sum_digits(i)
            ## checking if i is a prime
            for ii in range (i-1,1,-1):
                if (i % 2 == 0):
                    # checking divisibility by 2
                    # not a prime
                    flag_prime = 0
                    break
                elif (sum_of_digits % 3 == 0):
                    # checking divisibility by 3
                    # not a prime
                    flag_prime = 0
                    break
                elif (i % 10 == 0 or i % 10 == 5):
                    # checking divisibility by 5
                    # not a prime
                    flag_prime = 0
                    break
                elif (i % ii == 0):
                    # checking divisibility by any number
                    # not a prime
                    flag_prime = 0
                    break
                else:
                    # it may be a prime, keep looping
                    flag_prime = 1
                    # break
        else:
            flag_divisor = 0

        if flag_prime == 1:
            break

    largest_possible_divisor = i

    elapsed = time.time() - start

    print (largest_possible_divisor,"\n", elapsed,"\n")
    
    return

new_approach(60085147)
# 600851475143
