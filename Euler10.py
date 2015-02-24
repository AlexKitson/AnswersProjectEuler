__author__ = 'Alex Kitson'
'''fin=2
def is_prime(x):
    for y in range(2,int(x**0.5+1)):
        if x%y==0: return False
    return True
for x in range(3,2000001,2):
    if is_prime(x):
        fin+=x
print fin'''
def eratosthenes2(n):
    fin=0
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            fin+=i
            multiples.update(range(i*i, n+1, i))
    print fin
eratosthenes2(2000000)