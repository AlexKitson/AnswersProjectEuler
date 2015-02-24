__author__ = 'Alex Kitson'
fin=0
def is_palindrome(x):
    if x==int(str(x)[::-1]):
        return True
    return False
m=[x*y for x in range(100,1000) for y in range(100,1000)]
for x in sorted(m):
    if is_palindrome(x):
        fin=x
print fin

#int("".join(list(reversed(str(x)))))