#Яша плавал в бассейне размером N × M метров и устал. 
#В этот момент он обнаружил, что находится на расстоянии x метров от одного из длинных бортиков 
#(не обязательно от ближайшего) и y метров от одного из коротких бортиков. 
#Какое минимальное расстояние должен проплыть Яша, чтобы выбраться из бассейна на бортик? 
#Программа получает на вход числа N, M, x, y. 
#Программа должна вывести число метров, которое нужно проплыть Яше до бортика.
N = int(input("1 размер бассейна"))
M = int(input("2 размер бассейна"))
x = int(input("расстояние до одного из длинных бортиков"))
y = int(input("расстояние до одного из коротких бортиков"))

if N >= M:#N-длинный
    if (N - y) >= y:
        if (M - x) >= x:
            if y >= x:
                print(x)
            else:
                print(y)
        else:
            if y >= (M - x):
                print(M - x)
            else:
                print(y)
    else:
        if (M - x) >= x:
            if (N - y) >= x:
                print(x)
            else:
                print(N - y)
        else:
            if (N - y) >= (M - x):
                print(M - x)
            else:
                print(N - y)
else:#M-длинный
    if (M - y) >= y:
        if (N - x) >= x:
            if y >= x:
                print(x)
            else:
                print(y)
        else:
            if y >= (N - x):
                print(N - x)
            else:
                print(y)
    else:
        if (N - x) >= x:
            if (M - y) >= x:
                print(x)
            else:
                print(M - y)
        else:
            if (M - y) >= (N - x):
                print(N - x)
            else:
                print(M - y)
