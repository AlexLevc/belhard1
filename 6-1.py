#Написать функцию перевода десятичного числа в двоичное и обратно, без
#использования функции int
def binary(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s

def bin_dec(digit):
    dlina=len(digit)
    chislo=0
    for i in range(0, dlina):
        chislo=chislo+int(digit[i])*(2**(dlina-i-1))
    return chislo

while True:
    n = int(input())
    if n != 0:
        print(binary(n))
        print(bin_dec(binary(n)))
    else:
        break


