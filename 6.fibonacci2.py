#Дано натуральное число A. 
#Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φn = A. 
#Если А не является числом Фибоначчи, выведите число -1.
A = int(input())
n = 1
f = 1
f2 = 0
if A == 0:
    n = 1
else:
    while f < A:
        f, f2 = f + f2, f
        n += 1
    if f != A:
        n = -1
print(n)
