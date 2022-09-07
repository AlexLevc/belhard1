#пользователь вводит 3 числа, найти среднее арифметическое с точностью 3
num1 = int(input())
num2 = int(input())
num3 = int(input())
sum = (num1 + num2 + num3)/3
sum = round(sum,3)
print(sum)