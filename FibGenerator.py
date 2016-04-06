# Generator Function for creating fibonnaci series upto 10 elements
# fill in this function
def fib():
    a=1
    b=1
    yield b
    
    for x in range(0,10):
       	yield b
        a,b=b,a
        b=a+b
    pass #this is a null statement which does nothing when executed, useful as a placeholder.

# testing code
import types
if type(fib()) == types.GeneratorType:
    print ("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print (n)
        counter += 1
        if counter == 10:
            break
