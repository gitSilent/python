#Напишите программу на Python для печати четных чисел из заданного списка.
def chet(massiv):
    chet_itog = []
    for i in range(len(massiv)):
        if massiv[i]%2==0:
            chet_itog.append(massiv[i])
    return(chet_itog)
print(chet([int(el) for el in input("Введите массив без запятых ").split()]))
