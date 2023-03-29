import random as r
import time as t

slot = [0, 0 ,0]
n = int(input('몇번 할건가요?'))
for k in range(n) :
    for k in range(3) :
        slot[k] = r.randrange(7,10) # 무작위 수 7, 8, 9 생성
        print('%d ' % slot[k], end = '')
        t.sleep(1)   
    if slot[0] + slot[1] + slot[2] == 21 :
        print('잭팟이 터졌다!!')
        break
    else :
        print('꽝')