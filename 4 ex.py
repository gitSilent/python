mas = [int(el) for el in input("Введите массив без запятых").split()]
schet = 0
for i in range(len(mas)-1):
    if (mas[i] > 0 and mas[i+1] > 0) or (mas[i] < 0 and mas[i+1] < 0) :
        schet = schet
    else:
        schet = schet + 1
print(schet)

