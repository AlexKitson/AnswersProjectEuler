__author__ = 'Alex Kitson'
fin=[0,0]
def collatz(x):
    if x==1:return 1
    if x%2==0:return 1+collatz(x/2)
    return 1+collatz(3*x+1)
for x in range(1,1000000):
    if collatz(x)>fin[0]:
        fin[0]=collatz(x)
        fin[1]=x
print fin