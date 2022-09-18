# Написать программу генерации треугольника паскаля указанной глубины
n = int(input())
tp = []
for i in range(n+1):
    tp.append([1]+[0]*n)

for i in range(1, n+1):
    for j in range(1, i+1):
        tp[i][j] = tp[i-1][j] + tp[i-1][j-1]
#for i in tp:
#    print(i)
for i in range(0, n+1):
    for j in range(0, i+1):
        print(tp[i][j], end=' ')
    print()