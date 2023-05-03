#fibonacci = [1, 1]

#for i in range(0, 1000):
#  fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

#print(fibonacci)
def fibo(n):
  if n<2 : return 1
  else : return fibo(n-1)+fibo(n-2)

for k in range(13):
  print('%d개월 후 토끼 수 = %d' %(k, fibo(k)))
