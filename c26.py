from random import randrange
from random import sample

mylotto = set()
while True:
    num = randrange(1, 45)
    print(num, end=' ')
    mylotto.add(num)
    if len(mylotto) == 6:
        break
print('\n집합: {}'.format(mylotto))
print('정렬리스트 : {}'.format(sorted(mylotto)))

print('\nsample로 번호리스트 만들기')
lotto = sample(range(1, 46), 6)
print('sample 한 함수 리스트 : {}'.format(lotto))
print('sample 함수 정렬리스트 : {}'.format(sorted(lotto)))