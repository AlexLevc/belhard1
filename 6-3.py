# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]
def shift(lst, steps):
    if steps > 0:
        for i in range(steps):
            lst.append(lst.pop(0))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

shift(nums, steps=int(input()))
print(nums)
