#пользователь вводит 3 числа, найти среднее арифметическое с точностью 3
num1 = int(input('1-е число '))
num2 = int(input('2-е число '))
num3 = int(input('3-е число '))
sum = (num1 + num2 + num3)/3
sum = round(sum,3)
print(sum)