from sympy import Symbol, expand, Poly, solve, sin, latex

x = Symbol('x')
y = Symbol('y')

q = expand(sin(x + y), trig=True)
print(q)

q = expand((x + 1) ** 2)
print(q)
p = Poly(q, x)
c = p.coeffs()

q2 = x ** 13 - 2 * x ** 5 - x ** 3 - 20
s = solve(q2, x)

print(latex(q2))

