# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число
num1 = int(input('введите первое число: '))
znak = input('введите действие: ')
num2 = int(input('введите второе число число: '))
if znak == '+':
    print(num1+num2)
elif znak == '-':
    print(num1-num2)
elif znak == '*':
    print(num1*num2)
elif znak == '/':
    if num2 != 0:
        print(num1/num2)
    else:
        print('na 0 ne delitsya')