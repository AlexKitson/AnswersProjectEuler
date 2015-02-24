__author__ = 'Alex Kitson'
x=1
y=2
z=x+y
fin=2
while z<=4000000:
    x=y
    y=z
    z=x+y
    if z%2==0:
        fin+=z
print fin