from sympy import Symbol, solve, Abs


x = Symbol('x', real=True)


e = Abs(x) - 1

e1 = 2 * e.subs(x, e) - 1

s = solve(e1, x)

print(s)







