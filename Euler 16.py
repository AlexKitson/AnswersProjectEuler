__author__ = 'Alex Kitson'
def digit_sum(x):
    if x==0:return 0
    return x%10+digit_sum(x/10)
print digit_sum(2**1000)