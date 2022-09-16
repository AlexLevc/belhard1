# Вывести четные числа от 2 до N по 5 в строку
N = int(input('введите число: '))
count = 0
for i in range(2, N+1):
    if (i % 2 == 0):
        print(i, end=", ")
        count +=1
    elif (count % 5 == 0):
        print( end='\n')