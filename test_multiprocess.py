import multiprocessing
import os

def f(x):
    print(x*x)

p = multiprocessing.Process(target = f, args = (3, ))
p.start()
p.join()

with multiprocessing.Pool(5) as e:
    print(e.map(f, [1,2,3]))
