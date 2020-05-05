---
layout: post
title: Project Euler - Problem 6
post-order: 006
---


## Problem #6

The sum of the squares of the first ten natural numbers is

$$1^2 + 2^2 + \cdots + 10^2 = 385$$

The square of the sum of the first ten natural numbers is

$$\left( 1 + 2 + \cdots + 10 \right) = 55^2 = 3025$$

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

### Solution #1

Let's run throug the numbers 1 to 100 adding all integers and, at the same time, adding all squares. In the end, we'll take the sum of all integers and square it, in order to compera to the sum of the squared integers.


```python
sum_of_integers = 0
sum_of_squares = 0
n = 100

for i in range(1, n+1):
    sum_of_integers += i
    sum_of_squares += i**2
    
print (sum_of_integers**2)
print(sum_of_squares)
```

    25502500
    338350


The difference can be found, well, by subtracting one number by the other:


```python
print (sum_of_integers**2 - sum_of_squares)
```

    25164150


### Solution #2

There are a few strategies that one can use to address this problem a little better. Analysing the sum of the integers, which later gets squared, we can use the formula for the sum of an arithmetic series:

$$\displaystyle S = \frac{n \cdot \left[ 2 \cdot u_1 + (n-1)  \cdot d \right]}{2} = \frac{n \cdot (n+1)}{2}$$

The sum of the first n integers can be calculated by the following:


```python
def sum_first_n_integers(n):
    sum_first_n_integers = (n*(n+1))/(2)
    return sum_first_n_integers
    
print(int(sum_first_n_integers(n)**2))
```

    25502500


Also, we can calculate the sum of the first n integers **squared** using the following formula (see [this](https://brilliant.org/wiki/sum-of-n-n2-or-n3/#) as a reference).


```python
def sum_first_n_integers_squared(n):
    sum_first_n_integers_squared = n*(n+1)*(2*n+1)/6
    return sum_first_n_integers_squared
    
print(int(sum_first_n_integers_squared(n)))
```

    338350


The difference is therefore


```python
print(int(sum_first_n_integers(n)**2) - int(sum_first_n_integers_squared(n)))
```

    25164150
