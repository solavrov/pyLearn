from sympy import *


x, y = symbols('x y')

e = sin(2*x+y)**2

e = expand(expand_trig(e))

print(e)
print(latex(e))


