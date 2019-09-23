#По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. 
#Выведите показатель степени и саму степень.
#Операцией возведения в степень пользоваться нельзя!
N = int(input())
n = 1
i = 0
while n <= N:
    n *= 2
    i += 1
if N == 1:
    print(int(0), int(1))
else:
    print(i-1, int(n/2))
#правильное решение
#n = int(input())
#two_in_power = 2
#power = 1
#while two_in_power <= n:
#    two_in_power *= 2
#    power += 1
#print(power - 1, two_in_power // 2)
