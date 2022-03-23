from sympy import *
from niepewnosci_srednich_k import delta_k1, delta_k2
from lab1 import k1, k2, m1, m2, delta_m1, delta_m2

k_1, k_2, m_1, m_2, w = symbols("k_1, k_2, m_1, m_2, w")

values = {
    k_1:k1,
    k_2:k2,
    m_1:m1,
    m_2:m2,
}

deltas = {
    k_1:delta_k1,
    k_2:delta_k2,
    m_1:delta_m1,
    m_2:delta_m2,
}

#pierwszy zestaw - k_1 na dole

eq = (-m_1*w**2+k_1+k_2)*(-m_2*w**2+k_1)-k_1**2

#print(expand(eq))

eq = k_1*k_2 -(w**2)*(k_1*m_2+k_1*m_1+k_2*m_2) + m_1*m_2*w**4

a = m_1*m_2
b = -(k_1*m_2+k_1*m_1+k_2*m_2)
c = k_1*k_2

w1 = sqrt((-b + sqrt(b**2-4*a*c))/(2*a))
w2 = sqrt((-b - sqrt(b**2-4*a*c))/(2*a))

print(latex(w1.diff(k_1)))

delta_w1, delta_w2 = 0, 0

for el in values:
    dif1 = w1.diff(el).subs(values).evalf()
    delta_w1+=(dif1*deltas[el])**2
    dif2 = w2.diff(el).subs(values).evalf()
    delta_w2+=(dif2*deltas[el])**2

delta_w1, delta_w2 = sqrt(delta_w1), sqrt(delta_w2)



# drugi zestaw - k_2 na dole
eq = (-m_1*w**2+k_1+k_2)*(-m_2*w**2+k_2)-k_2**2

#print(expand(eq))

eq = k_1*k_2 -(w**2)*(k_1*m_2+k_2*m_1+k_2*m_2) + m_1*m_2*w**4

a = m_1*m_2
b = -(k_1*m_2+k_2*m_1+k_2*m_2)
c = k_1*k_2

w3 = sqrt((-b + sqrt(b**2-4*a*c))/(2*a))
w4 = sqrt((-b - sqrt(b**2-4*a*c))/(2*a))

delta_w3, delta_w4 = 0, 0

#print(latex(w3))

for el in values:
    dif3 = w3.diff(el).subs(values).evalf()
    delta_w3+=(dif3*deltas[el])**2
    dif4 = w4.diff(el).subs(values).evalf()
    delta_w4+=(dif4*deltas[el])**2

delta_w3, delta_w4 = sqrt(delta_w3), sqrt(delta_w4)

w1=w1.subs(values).evalf()
w2=w2.subs(values).evalf()
w3 = w3.subs(values).evalf()
w4=w4.subs(values).evalf()

prt={
    w1:delta_w1,
    w2:delta_w2,
    w3:delta_w3,
    w4:delta_w4
}



for key, el in prt.items():
    print(key, el)
