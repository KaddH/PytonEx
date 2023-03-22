sum = 0
n = int(input('어디까지 더할건가요?'))
i = 0
while i < n :
    i += 1
    if i % 2 == 0 :
        sum += i

print('%d' %sum)