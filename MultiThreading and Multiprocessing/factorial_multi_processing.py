'''
Real-World Example: Multi-Processing for CPU - Bound Tasks
Scenerio: Factorial Calculation
Factorial Calculations, especially for large numbers,
involve significant computational work. Multiprocessing
can be used to distribute the workload across multiple CPU cores,
improving performance.
'''

import multiprocessing
import math
import time
import sys

# Increase the maximum number of digits for interger conversion
sys.set_int_max_str_digits(100000)

## function to compute factorials of a given number
def compute_factorial(number):
    print(f"compute_factorial({number})")
    result = math.factorial(number)
    print(f"compute_factorial({number}) = {result}")
    return result

if __name__ == "__main__":
    numbers = [5000,6000,7000,8000,9000,10000]

    start = time.time()

    ##create a pool of worker processes
    with multiprocessing.Pool() as pool:
        result = pool.map(compute_factorial, numbers)

    end_time = time.time()
    print(f"Result: {result}")
    print(f"compute_factorial({numbers}) = {end_time - start}")
