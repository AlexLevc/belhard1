# Дан список чисел, отсортировать его по возрастанию без использования sort и sorted
lst = [1, 2, 5, 3, 4, 8, 6]
n = len(lst)
for i in range(n):
    for j in range(1, n-i):
        if lst[j-1] > lst[j]:
             (lst[j-1], lst[j]) = (lst[j], lst[j-1])
print(lst)
