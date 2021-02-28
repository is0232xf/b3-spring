import time
import math

def for_loop(num):
    for i in range(num):
        if i % 2 == 0:
            print('Even')
            print(i)
        elif i % 2 == 1:
            print('Odd')
            print(i)
        time.sleep(1)

for_loop(5)
