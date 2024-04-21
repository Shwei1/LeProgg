from classes_531 import Rational
from equations_531 import Equations

e = Equations("input01.txt")
j = 1
for i in e.solve_equations():
    print(f"{j}: {i}")
    j += 1