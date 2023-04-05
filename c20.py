import random
from random import randrange as ran # random 에서 randrange만 써서 random만 쓰면 되는데 as ran을 써서 random을 ran만 써도 사용가능

number = []
i = 0
for i in range(20):
    number.append(ran(0, 100))

i = int(input("몇번째 데이터를 원하시나요?"))
print(number)
number.sort()
print(number)
print(i, 'th data =', number[i-1])

count =1 
number2 = []
while count < 20:
    num = ran(0, 51)
    if num not in number2:
        number2.append(num)
        count += 1
number2.sort()
print(number2)

for d in range(i):
    mvalue = min(number2)
    di = number2.index(mvalue)
    del(number2[di])

print(i, 'th data = ', mvalue)
#print(number2)