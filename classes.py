from math import sqrt
import numpy as np
import sympy as sp


# współczynniki Studenta-Fishera dla poziomu ufności 98%
student_fisher_98 = {
    2: 12.706,
    3: 4.303,
    4: 3.182,
    5: 2.776,
    6: 2.447,
    7: 2.365,
    8: 2.306,
    9: 2.262,
    10: 2.228,
}


class Pomiar:
    def __init__(self, info, dane) -> None:
        self.name = info.split()[0]
        self.symbol = info.split()[1]
        self.accuracy = float(info.split()[2])
        self.unit = info.split()[3]
        self.dane = np.array([float(i) for i in dane])
        self.num = len(self.dane)
        self.calculate()

    def calculate(self):
        self.std = np.std(self.dane) / sqrt(self.num)
        self.avg = np.mean(self.dane)
        if len(self.dane) <= 10:
            self.std *= student_fisher_98[len(self.dane)]
        self.delta = sqrt(self.std ** 2 + (self.accuracy ** 2) / 3)

    def get_info(self):
        info = f"{self.name}\nsrednia: {self.avg}\nniepewnosc calkowita: {self.delta}"
        print(info)

    # """
    # mnożnik: g --> kg /1000 czyli mnożnik 0.001
    # """
    # def change_units(self, unit, mnoznik):
    #     self.unit = unit
    #     self.dane *= mnoznik
    #     self.accuracy *= mnoznik
    #     self.calculate()

    """
    jeśli pomiar to krotność szukanej wartości
    """

    def multiply_by(self, n):
        self.avg *= n
        self.delta = sqrt((n * self.delta) ** 2)


class Szukana:
    def __init__(self, expr, *niewiadome) -> None:
        self.expr = expr
        self.symbols = dict()
        for n in niewiadome:
            self.symbols[str(n)] = n

    def diff(self, x):
        print(sp.latex(self.expr.diff(x)))

    def eval(self, *pomiary):
        val = self.value(*pomiary)
        delta = self.delta(*pomiary)
        return val, delta

    def value(self, *pomiary):
        d = dict()
        for p in pomiary:
            d[p.symbol] = p.avg
        return self.expr.subs(d).evalf()

    def delta(self, *pomiary):
        suma = 0
        values = dict()
        for p in pomiary:
            values[p.symbol] = p.avg
        for p in pomiary:
            dif = self.expr.diff(self.symbols[p.symbol]).subs(values).evalf()
            suma += (dif * p.delta) ** 2
        return sqrt(suma)
