import random

print('여행어디로 갈래?')
trip = random.randrange(0,4)
if trip == 0 :
    print('제주도 가자')
elif trip == 1 :
    print('사이판 가자')
else :
    print('여행은 하와이지')