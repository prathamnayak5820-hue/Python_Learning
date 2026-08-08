temps_c = [25, 30, 35, 40]
def fahrenit(x):
    f = (x*9/5)+32
    return f
a = list(map(fahrenit,temps_c))
print(a)






from functools import reduce
numbers = [i for i in range(1,11) if i%2==0]
print(numbers)
n = reduce(lambda x,y: x if x>y else y ,numbers)
print(n)