__author__ = 'Alex Kitson'
x=3
i=600851475143
while x<i:
    if i%x==0:
        i/=x
    x+=2
print i
