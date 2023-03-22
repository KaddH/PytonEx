print("===1부터 n가지의 짝수의 합 구하기 =")
sum = 0
n = int(input("어디가지 더할거야?"))
for i in range(2, n+1, 2) :
    sum += i

print('1부터 %d의 합 %d' %(n, sum))