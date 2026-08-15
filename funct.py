#maximum of two using functions
def max_two(a,b):
    if a>b:
        return a
    else:
        return b
print(max_two(41,67))


#maximum of three using functions
def max_three(a,b,c):
    largest = a
    if b>largest:
        largest = b
        
    elif c>largest:
        largest =c
    return largest

print(max_three(23,90,21))

#factorial n using loops
def factorial(n):
    fact =1
    for i in range(1,n+1):
        fact*=i
    return fact
print(factorial(5))

#count digits
def count_digits(n):
    i=1
    while n>0:
        d=n%10
        i+=1
        n=n//10
    return i
print(count_digits(2988990))


#reverse a number
def reverse_number(n):
    i =0
    while n>0:
        d=n%10
        i =(i*10)+d
        n=n//10
        
    return i
print(reverse_number(89))

#sum of digit
def sum_number(n):
    i =0
    while n>0:
        d=n%10
        i+=d
        n=n//10
        
    return i
print(sum_number(897))


