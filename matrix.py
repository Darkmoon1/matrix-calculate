import multiprocessing
import time
import numpy as np
import scipy.io as sio

a,b = np.mgrid[0:4000,0:4000]
start = time.clock()
a1 = a[0:1000,0:4000]
a2 = a[1000:2000,0:4000]
a3 = a[2000:3000,0:4000]
a4 = a[3000:4000,0:4000]
# start1 = time.clock()
#c = np.dot(a,b)


def func1(a):
    d1 = np.matmul(a,b)

def func2(a):
    d2 = np.matmul(a,b)

def func3(a):
    d3 = np.matmul(a,b)

def func4(a):
    d4 = np.matmul(a,b)
if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)        

    pool.apply_async(func1,(a1,))
    pool.apply_async(func2,(a2,))
    pool.apply_async(func3,(a3,))
    pool.apply_async(func4,(a4,))

    pool.close()
    pool.join()

    # c = np.matmul(a,b)

    elapsed = (time.clock() - start)
    print("Time used:",elapsed)    
    print("Sub-process(es) done.")
