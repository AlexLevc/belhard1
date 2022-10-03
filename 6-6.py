# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные
import random
lst = [random.randint(0,100) for i in range(20)]
print(lst)
def sel_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]

sel_sort(lst)
print(lst)

