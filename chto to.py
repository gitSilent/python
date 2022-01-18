mas = [int(el) for el in input("Введите массив ").split()]
k1 = int(input("k1 ввод "))
n = int(input("n ввод "))
for i in range(len(mas)):
    if mas[i]>0:
        mas[i]=mas[i]-k1
    elif mas[i]<0:
        mas[i]=mas[i]-n
print(mas)
