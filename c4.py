import random

gnum = 0

while True :
    com = random.randrange(3)
    user= int(input('가위0 바위1 보2 선택: '))
    
    if user == 0 or user == 1 or user == 2 :
        print('user= %d, com= %d' % (user, com))
        gnum += 1
        if com == user :
            print('비겼습니다.')
        elif (com == 0 and user == 2) or (com == 1 and user == 0) or (com == 2 and user == 1):
            print('유저가 이겼습니다.')
        else :
            print('유저가 졌습니다.')
    else :
        print('%d회 경기했습니다. -- 이제그만 즐기세요 --' % gnum)
        break

    