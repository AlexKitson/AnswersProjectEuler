__author__ = 'Alex Kitson'
y=0
z=0
for x in range(1,101):
    z+=x
    y+=x**2
z=z**2
print z-y