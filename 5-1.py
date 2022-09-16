# Вывести первые N чисел кратные М и больше К
n = int(input('введите кол-во чисел: '))
m = int(input("Введите делитель:"))
k = int(input("больше чем: "))
count = 0
while k > 0:
    k +=1
    if(k % m == 0):
        count +=1
        print(k)
    if count == n:
        break
