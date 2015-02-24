__author__ = 'Alex Kitson'
fin=0
def d(n):
    r=0
    x=1
    while x<n/2+1:
        if n%x==0:r+=x
        x+=1
    return r
for a in range(1,10001):
    for b in range(1,a):
        if d(a)==b and d(b)==a:
            print a
            print b