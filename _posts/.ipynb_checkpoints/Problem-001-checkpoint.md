---
layout: post
<<<<<<< HEAD:_posts/2020-05-05-problem-1.md
title:  Project Euler - Problem 1
=======
title: Project Euler - Problem 1
post-order: 001
>>>>>>> 8ee00623c28d5b0554a04a654a4dd831589eae98:_posts/.ipynb_checkpoints/Problem-001-checkpoint.md
---


## Problem #1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

### Solution #1

This is the brute force method. On the solution below, a counter is initiated from 1 up until 1000. Whenever i is a multiple of 3 or 5 (something that can be easily cheked with the modulus operator `%`), the variable `sum` (initiated in zero) will be incremented of `i`. The flowchart can be found XXX here XXX.


```python
import time

def solution_1 (n): # in this case n = 1000
    start = time.time()

    sum = 0

    for i in range (1,n):
        if (i % 3 == 0 or i % 5 == 0):
        # if the number is divisible by 3 or 5 
        # we add it to the variable sum
            sum += i

    elapsed = time.time() - start
    print (sum, "Elapsed time: ", elapsed, "s")

    return

solution_1(1000)
```

    233168 Elapsed time:  0.00014400482177734375 s


### Solution #2

A different approach would be to create three number lists: one with all multiples of 3, another with multiples of 5 and finally a list with multiples of 15 (3 times 5). We'll add the items of the first two lists and subtract the third list. To implement this solution, we will need to use `numpy`.


```python
import time
import numpy as np # importing numpy

def solution_2 (n): # in this case n = 1000

    start = time.time()

    sum = 0

    multiples_of_3 = np.arange(3, n, 3)
    multiples_of_5 = np.arange(5, n, 5)
    multiples_of_15 = np.arange(15, n, 15)

    sum = np.sum(multiples_of_3) + np.sum(multiples_of_5) - np.sum(multiples_of_15)

    elapsed = time.time() - start

    print (sum, "Elapsed time: ", elapsed, "s")

    return

solution_2(1000)
```

    233168 Elapsed time:  0.0001010894775390625 s


By quickly evaluating the two, you may think that there are no improvements on the methods described. Let's check if that is the case.

### Comparison of the methods

To really evaluate and show that one solution is much better than the other, let's do the same calculations but with a much higher number, like 5000000.


```python
solution_1(5000000)
solution_2(5000000)
```

    5833329166668 Elapsed time:  0.7977828979492188 s
    5833329166668 Elapsed time:  0.010927200317382812 s


It's clear that solution_2 performs better.
