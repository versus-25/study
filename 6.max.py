#Последовательность состоит из натуральных чисел и завершается числом 0. 
#Определите значение наибольшего элемента последовательности.
i = 0
N = int(input())
while N != 0:
    if i <= N:
       i = N
    N = int(input())
print(i)
