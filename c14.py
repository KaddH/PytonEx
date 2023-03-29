n=int(input("몇개의 데이터 처리 : "))
listex = []
sum = 0

print('%d개의 데이터 입력 : ' % n)
for k in range(n):
    listex.append(int(input())) 
    sum += listex[k] 

print('리스트 데이터의 합과 평균  : %d %.2f\n' % (sum, sum/n))

max, min = listex[0], listex[0]
for k in range(1, n):
    if listex[k] > max :
        max = listex[k]
    elif listex[k] < min :
        min = listex[k]

print('주어진 리스트는 최대값(%d)와 최소값(%d)를 입력했습니다.' %(max, min))