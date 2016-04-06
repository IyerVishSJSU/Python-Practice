# Python script to implement partial functions in Python.
#Following is the exercise, function provided:
from functools import partial
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
#Code to create and print with partial function

db1= partial(func,5,5,10)
print db1(5)