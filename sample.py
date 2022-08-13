def myDecorator(func):
    def AddMul(a,b):
        mul = a*b
        div = a/b
        sum = func(a,b)
        return mul, div, sum
    return AddMul

a,b = 10,11




@myDecorator
def func1(a,b):
    sum = a+b
    return sum
print(func1(a,b))