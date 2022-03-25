from program import *
import math
from classes import Szukana
import sympy as sp

# zdefiniowanie wzorów i mierzonych niewiadomych
m, T = sp.symbols("m T")
expr = (4 * (sp.pi ** 2) * m) / T ** 2
k = Szukana(expr, m, T)

expr2 = (2 * math.pi) / T
w_exp = Szukana(expr2, T)


# init labu - pobranie pomiarów
lab = Lab("fizlab1.txt", k, w_exp)


# nadpisanie wartości średniej i niepewności okresów po podzieleniu przez 10
for n in range(2, 8):
    lab.pomiary[n].multiply_by(0.1)


# wpisanie do plików opracowań pomiarów i obliczeń niewiadomych

lab.opracuj_pomiary()

k1a, dk1a = lab.oblicz(k, "k1", 1, 3)
k2a, dk2a = lab.oblicz(k, "k2", 1, 5)
k1b, dk1b = lab.oblicz(k, "k1", 2, 4)
k2b, dk2b = lab.oblicz(k, "k2", 2, 6)
lab.oblicz(w_exp, "wsyn1", 7)
lab.oblicz(w_exp, "wasyn", 8)


# dodatkowe obliczenia

w = sp.Symbol("w")

m1 = lab.pomiary[0].avg / 1000
m2 = lab.pomiary[1].avg / 1000
k1 = (k1a + k1b) / 2000
k2 = (k2a + k2b) / 2000

delta_m1 = lab.pomiary[0].delta / 1000
delta_m2 = lab.pomiary[1].delta / 1000


# eq = (-m1*w**2+k1+k2)*(-m2*w**2+k2)-k2**2
# 1 - górne, 2 - dolne elementy

# drgania symetryczne - zamienione sprężyny

w_teoret1 = sp.solve((-m1 * w ** 2 + k1 + k2) * (-m2 * w ** 2 + k1) - k1 ** 2, w)

# drgania asymetryczne

w_teoret2 = sp.solve((-m1 * w ** 2 + k1 + k2) * (-m2 * w ** 2 + k2) - k2 ** 2, w)


if __name__ == "__main__":
    print(w_teoret1, "\n", w_teoret2)
