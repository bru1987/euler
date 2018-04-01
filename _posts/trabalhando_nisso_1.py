import numpy as np
import time

start = time.time()

def solution_2(n):
    series = [1, 2]
    a3 = series[-1] + series[-2]

    while (a3 < n):
        a3 = series[-1] + series[-2]
        series.append(a3)
    return series

solution_2(4000000)

evens = [series[x] for x in range(1,len(series), 3)]

elapsed = time.time() - start

print(np.sum(evens), elapsed)