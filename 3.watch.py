#С начала суток часовая стрелка повернулась на угол в α градусов. 
#Определите на какой угол повернулась минутная стрелка с начала последнего часа. 
#Входные и выходные данные — действительные числа.
a = float(input())
h = a/30
m = h*60
M = (m%60)*360/60

print(M)
