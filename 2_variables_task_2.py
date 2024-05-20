import math
a = float(input('Enter side a: '))
b = float(input('Enter side b: '))
c = float(input('Enter side c: '))
hp = (a+b+c)/2
s = math.sqrt(hp*(hp-a)*(hp-b)*(hp-c))
print('S=',s)