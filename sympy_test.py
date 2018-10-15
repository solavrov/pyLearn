import sympy as sym

x = sym.Symbol('x')
y = sym.Symbol('y')

q = sym.expand(sym.sin(x + y), trig=True)
print(q)

q = sym.expand((x + 1) ** 2)
print(q)
p = sym.Poly(q, x)
c = p.coeffs()

q2 = x ** 13 - 2 * x ** 5 - x ** 3 - 20
s = sym.solve(q2, x)

