__author__ = 'Alex Kitson'
def factorial(x):
    if x==1:return 1
    return x*factorial(x-1)
def digit_sum(x):
    if x==0:return 0
    return x%10+digit_sum(x/10)
print digit_sum(factorial(100))