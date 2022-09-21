# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза
spisok = [1, 2, 3, 4, 5, 6, 7]
def reverse(text):
    output = []
    for i in range(len(text)-1, -1, -1):
        output.append(text[i])
    return output
print(reverse(spisok))
