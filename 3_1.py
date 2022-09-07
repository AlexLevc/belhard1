#пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
text1 = input('text1 = ')
word = text.split()
text1 = '-'.join(word)
print(text1)
text2 = input().replace(' ', '-')
print(text2)