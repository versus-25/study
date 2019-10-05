#По данному числу n определите n-е число Фибоначчи φn.
N = int(input())
n = 0
f2 = 1
f = 0
if N == 0:
    f = 0
elif N == 1:
    f = 1
else:
    while n != N:
        if n == 0:
            f = 1
            f2= 0
        else:
            f, f2  = f + f2, f
        n += 1
print(f)
