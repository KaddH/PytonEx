menu = ('기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거')
price = (4000, 4500, 5000, 7000)

menu_list = {}
for i in range(len(menu)):
    menu_list[menu[i]] = price[i]

menu_list['새우버거'] = 5500
del menu_list['기본햄버거']
menu_list['나이스 버거'] = 2000
print(menu_list)

for i in menu_list.keys():
    print(i, ':', menu_list[i])

