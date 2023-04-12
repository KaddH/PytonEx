menulist = ['기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거']
pricelist = [4000, 4500, 5000, 7000]
tlist = list(zip(menulist, pricelist))
dlist = dict(zip(menulist, pricelist))

for food, side in zip(menulist, pricelist) :
    print(food, '--->', side)

print(tlist)
print(dlist)

str1 = input('문자열을 입력하세요 : ')

for k in range(len(str1) - 1, -1, -1) :
    print(str1[k], end= '')