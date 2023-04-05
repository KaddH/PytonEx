menu = ('기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거')
price = (4000, 4500, 5000, 7000)

for i in range(len(menu)):
    print(i+1, '= ',menu[i], ' :', price[i])

lmenu = list(menu)
lprice = list(price)
lmenu.append('새우버거')
lprice.append(5500)

menu = tuple(lmenu)
price = tuple(lprice)
print('메뉴:',menu)
print('가격:',price)
