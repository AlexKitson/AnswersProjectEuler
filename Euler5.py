__author__ = 'Alex Kitson'
fin=20
while True:
    fin+=20
    if fin%11==0 and fin%12==0 and fin%13==0 and fin%14==0 and fin%15==0 and \
        fin%16==0 and fin%17==0 and fin%18==0 and fin%19==0 and fin%20==0:
            break
print fin


'''def divisible(x):
    for y in range(11,21):
        if x%y!=0:
            return False
    return True'''