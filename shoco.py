#Шоколадка имеет вид прямоугольника, разделенного на n×m долек. 
#Шоколадку можно один раз разломить по прямой на две части. 
#Определите, можно ли таким образом отломить от шоколадки часть, состоящую ровно из k долек. 
#Программа получает на вход три числа: n, m, k и должна вывести YES или NO.

n = int(input("число долек шоколадки по горизонтали"))
m = int(input("число долек шоколадки по вертикали"))
k = int(input("количество долек шоколадки в отломленной части шоколадки"))

if k == 1 and (n == 1 or m == 1):
    print("yes")
elif (k%m == 0 and m*n >= k) or (k%n == 0 and m*n >= k):
    print("yes")
else:
    print("no")
