def suma(*args):
    value = 0
    for i in args:
        value += i 
    print(value)

suma(1,2,3,4,10)

def multi(*args):
    value = 1
    for m in args:
        value *= m
        print(value)
        
multi(6,2,3,6)    