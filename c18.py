print("합을 구할 데이터수와 질문 개수 :")

suNO, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
pSum = [0]
temp = 0
slist= []

for i in numbers:
    temp += i
    pSum.append(temp)


for i in range(quizNo):
    s, e = map(int, input().split())
    print(pSum[e] - pSum[s-1])

for i in range(quizNo):
    print(slist[i])