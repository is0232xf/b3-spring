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

def master_func():
    print('I am the master of this code (first time)')

def master_func2():
    print('I am the master of this code (second time)')

def collaborator_func():
        prinnt('I am a collaborator of this code')

for_loop(5)
master_func()
