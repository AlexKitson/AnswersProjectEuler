__author__ = 'Alex Kitson'
a=0
def trinum(x):
    if x==0:return 0
    return x+trinum(x-1)
while 1:
    b=0
    for x in range(1,trinum(a)+1):
        if trinum(a)%x==0:
            b+=1
    if b>500:
        print trinum(a)
        break
    a+=1