## processes that run in parallel 
## CPU-Bound Taks - Tasks that are heavy on CPU usage (e.g., mathematical computations, dataset )
## parallel execution- Multiple cores of the CPU 

import multiprocessing

import time 

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")
    
def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")

if __name__=="_main":

    ## create 2 processes 
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)


    ## start the process
    p1.start()
    p2.start()

    ## wait for the process to complete 
    p1.join()
    p2.join()