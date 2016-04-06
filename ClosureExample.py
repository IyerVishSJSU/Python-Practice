# This code illustrates Closure example with help of a Nested Function. Print 9x5=45
#print "Hello, World!"

def multipier_of(n):
    def multipler(number):
        return number*n
    return multipler


solpart= multipier_of(5) 
print solpart (9)

    