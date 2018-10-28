from sympy import Symbol, expand, factor, solve, simplify, apart, together, collect, latex, preview


x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

print('EXPAND, FACTOR, SUBSTITUTE, SOLVE')
e = (x + 1) ** 2
print(e)
e = expand(e)
print(e)
e = factor(e)
print(e)
e = expand(e)
print(e)
e = e.subs(x ** 2, y)
print(e)
r = solve(e, y)[0]
print(r)

print('SIMPLIFY')
e = expand((x + 1) * (y + 1)) / (y + 1)
print(e)
e = simplify(e)
print(e)

print('TOGETHER, APART')
e = 1/x + 1/y + 1/z
print(e)
e = together(e)
print(e)
e = apart(e, x)
print(e)

print('COLLECT')
e = y*x**2 + z*x - z*x**2 + z**2 * x + y**3
print(e)
e = collect(e, x)
print(e)
e = expand(e)
e = collect(e, z)
print(e)
print(latex(e))

print('PROBLEM_1')
e1 = 2*x + y + z - 1
e2 = x + 2*y + z - 2
e3 = x + y + 2*z - 3
s = solve([e1, e2], [x, y])
print(s)
e4 = e3.subs(x, s[x]).subs(y, s[y])
print(solve(e4))
s = solve([e1, e2, e3], [x, y, z])
print(s)

x_i_ice = Symbol('x_i^ice')
y_j_water = Symbol('y_j^water')
e5 = (1 + x_i_ice**2) / (1 + y_j_water**2)
print(latex(e5))
# preview(e3)
