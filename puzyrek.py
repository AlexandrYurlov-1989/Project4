from random import randint

s = '0'

while s != '1' and s != '2':
    s = input("Выберите способ заполнения списка.\n1)Вручную\n2)Авто заполнение\n(Введите 1 или 2):")
else:
    N = int(input("Введите количество цифр в списке:"))
    a = []
      
    if (s == '1'):

        for i in range(N):
            a.append(input("ВВедите цифру: "))
        print(a)           
        for i in range(N-1):
            for j in range(N-i-1):
                if a[j] > a[j+1]:
                  a[j], a[j+1] = a[j+1], a[j]
        print(a)
    else: 
        for i in range(N):
            a.append(randint(1, 99))
        print(a)
 
        for i in range(N-1):
            for j in range(N-i-1):
                if a[j] > a[j+1]:
                 a[j], a[j+1] = a[j+1], a[j]
        print(a)


