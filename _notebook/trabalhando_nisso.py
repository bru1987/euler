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
