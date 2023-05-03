from random import randrange

hap = lambda n1 = 10, n2 = 70, n3 = 50 : n1+n2+n3
print(hap())
print(hap(10, 20))

exList = [10, 20, 30, 40 ,50]
exList2 = exList*2
print(exList2)


def multiplyn(data, n) :
    return data * n

m = randrange(2, 6)
print('m =',m)
for k in range(len(exList)):
    exList[k] = multiplyn(exList[k], m)
print(exList)