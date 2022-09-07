
# Пользователь вводит Имя, возраст и Город, сформировать приветственное сообщение путем формирования 3-мя способами
name = input()
surname = input()
town = input()
# 1-й способ
text1 = 'Hello! My name is ' + name + '. My surname is ' + surname + '. I from is ' + town + '.'
#2-й способ
text2 = 'Hello! My name is {}. My surname is {}. I from is {}.'.format(name, surname, town)
# 3-й способ
text3 = f'Hello! My name is {name}. My surname is {surname}. I from is {town}.'
print(text1)
print(text2)
print(text3)
