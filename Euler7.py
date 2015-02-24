__author__ = 'Alex Kitson'
fin=0
x=3
n=1
def is_prime(x):
    for y in range(2,int(x**0.5+1)):
        if x%y==0: return False
    return True
while n<10001:
    if is_prime(x):
        fin=x
        n+=1
    x+=2
print fin