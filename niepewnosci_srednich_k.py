from math import sqrt
from sympy import symbols
from lab1 import *

k11, k12, k21, k22 = symbols("k11, k12, k21, k22")
values = {k11: k1a, k12: k1b, k21: k2a, k22: k2b}

niepew = {k11: dk1a, k12: dk1b, k21: dk2a, k22: dk2b}

srednia_k1 = (k11 + k12) / 2
srednia_k2 = (k21 + k22) / 2

s = 0
for el in [k11, k12]:
    dif = srednia_k1.diff(el).subs(values).evalf()
    s += (dif * niepew[el]) ** 2
delta_k1 = sqrt(s)

s = 0
for el in [k21, k22]:
    dif = srednia_k2.diff(el).subs(values).evalf()
    s += (dif * niepew[el]) ** 2
delta_k2 = sqrt(s)

delta_k1 /= 1000
delta_k2 /= 1000

if __name__ == "__main__":
    print(delta_k1, "\n", delta_k2)
