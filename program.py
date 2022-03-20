from asyncore import write
from multiprocessing.sharedctypes import Value
from classes import Pomiar, Szukana
import numpy as np
import sympy as sp
import csv


class Lab:
    def __init__(self, file, *szukane) -> None:
        self.filename = file.split(".")[0]
        self.oprac_file = self.filename + "_opracowane.csv"
        self.szukane_file = self.filename + "_szukane.csv"
        self.init_file_szukane()
        self.szukane = szukane
        self.pomiary = self.read_from_file(file)

    def read_from_file(self, file):
        headers = []
        data = []
        with open(file) as handle:
            data = handle.readlines()
        for line in data:
            try:
                float(line)
            except:
                headers.append(line)
        return self.extract_by_headers(data, headers)

    def extract_by_headers(self, data, headers):
        pomiary = []
        for n in range(len(headers) - 1):
            back = data.index(headers[n]) + 1
            front = data.index(headers[n + 1])
            dane = data[back:front]
            pomiar = Pomiar(headers[n], dane)
            pomiary.append(pomiar)
        return pomiary

    def opracuj_pomiary(self):
        header = ["nazwa_pomiaru", "jednostka", "srednia", "niepewnosc"]
        with open(self.oprac_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for pomiar in self.pomiary:
                row = [pomiar.name, pomiar.unit, pomiar.avg, pomiar.delta]
                writer.writerow(row)

    def oblicz(self, szukana, nazwa, *pomiary):
        pom = [self.pomiary[i - 1] for i in pomiary]
        val = None
        with open(self.szukane_file, "a", newline="") as f:
            writer = csv.writer(f)
            data = szukana.eval(*pom)
            row = [nazwa, ",".join([p.name for p in pom]), data[0], data[1]]
            writer.writerow(row)
            val = data[0]
        return val

    def init_file_szukane(self):
        header = ["niewiadoma", "pomiary", "wartosc", "niepewnosc"]
        with open(self.szukane_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
