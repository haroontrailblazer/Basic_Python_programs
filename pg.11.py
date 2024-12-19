#Quadatric equation[ax^2 +bx +c =0]
import math
a=float(input('Enter coefficient a: '))
b=float(input('Enter coefficient b: '))
c=float(input('ENTER coefficient c: '))
d=b**2 - 4*a*c
if d > 0:
  root1=(-b+math.sqrt(d))/(2*a)
  root2=(-b-math.sqrt(d))/(2*a)
  print(f'Root 1:{root1}')
  print(f'Root 2:{root2}')
elif d==0:
  Root=-b/(2*a)
  print(f'Root: {Root}')
else:
  rp=-b/(2*a)
  im=math.sqrt(abs(d))/(2*a)
  print(f'Root 1:{rp}+{im}i')
  print(f'Root 2:{rp}-{im}i')
