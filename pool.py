N = int(input("1 размер бассейна"))
M = int(input("2 размер бассейна"))
x = int(input("расстояние до одного из длинных бортиков"))
y = int(input("расстояние до одного из коротких бортиков"))
N-y M-x y x 
if N >= M:#N-длинный
    if (N - y) >= (M - x):
        if (M - x) >= x:
            print(x)
        else:
            print(M - x)
    else:
        if (N - y) >= y:
            print(y) 
        else:
            print(N - y)
if N < M:#M-длинный
    if (M - y) >= (N - x):
        if (N - x) >= x:
            print(x)
        else:
            print(N - x)
    else:
        if (M - y) >= y:
            print(y) 
        else:
            print(M - y)
else:#квадратный бассейн N = M
    if x >= y:
        if (N - x) > y:
            print(y)
        else:
            print(N - x)
