CD5C5C = (205, 92, 92)
F08080 = (240, 128, 128)
FA8072	= (250, 128, 114)
E9967A	= (233, 150, 122)
FFA07A	= (255, 160, 122)
FF0000 = (255, 0, 0)

dict_color = { 'IndianRed' : CD5C5C,  'LightCoral' : F08080, 'Salmon' : FA8072,  'DarkSalmon' : E9967A,  'LightSalmon' : FFA07A, 'Red' : FF0000}
print(f"словарь цветов =  {dict_color}")

N = '0'

while N != 'IndianRed' and N != 'LightCoral'and N != 'Salmon' and N != 'DarkSalmon'and N != 'LightSalmon' and N != 'Red':
   N = (input("Цвета в славоре:\nIndianRed\nLightCoral\nSalmon\nDarkSalmon\nLightSalmon\nRed\nВведите цвет чтобы узнать его зачение RGB: "))
else:
    print(f"RGB={dict_color[N]}")