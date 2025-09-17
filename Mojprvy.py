print("Čauko, jednoducho ti viem vypočitať korene hocijakej rovnice. Len budem potrebovať zopar drobnosti")
a = int(input("A="))
b = int(input("B="))
c = int(input("C="))
print("Diky idem na to")
import math
from math import sqrt
x1 = (-b+sqrt(b**2 - 4 * a * c))/2*a
x2 = (-b-sqrt(b**2-4*a*c))/2 * a
print(x1,",",x2)