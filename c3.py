import random

com = random.randrange(3)
user= int(input('가위0 바위1 보2 선택: '))
print('user= %d, com= %d' % (user, com))
print('%d', com)
if com == user :
    print('비겼습니다.')
elif (com == 0 and user == 2) or (com == 1 and user == 0) or (com == 2 and user == 1):
    print('유저가 이겼습니다.')
else :
    print('유저가 졌습니다.')