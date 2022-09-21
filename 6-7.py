def foo(numbers: list[int]) -> list[int]:
    res = []
    for i in range(len(numbers)):
        if i+1 != len(numbers):
            res.append(numbers[i-1] + numbers[i+1])
        else:
            res.append(numbers[i-1]+ numbers[0])
    return res

print(foo([1, 2, 3, 4, 5]))