import newtonRaphason
import secent
import BisectionClass
import FalsePosition
import birgeVieta
import fixedPointIteration
import sympy
from sympy.abc import x
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from sympy import symbols
from sympy.plotting import plot

#obj2 = secent.secantMethod()
#obj2.setFuncionAndIntialpoint("2*x**2 + 2*x - 0.1", 1.5, 1)
#obj2.calculateRoot()
#print(obj2.getAppRoots())
#print(obj2.getErrors())
#print(obj2.saveDate())
#obj2.graph()


# print()
# print()
# print()

# obj = BisectionClass.Bisection("x^2 - 2 * x - 1", 2, 4)
# obj.runMethod()
# obj.graph()


# obj = FalsePosition.FalsePosition("x^2 - 2 * x - 1", 1, 4)
# obj.runMethod()
# obj.graph()




obj = newtonRaphason.NewtonRaphasonMethod()
obj.setFuncionAndIntialpoint("(x - 2)(x + 4)^4", -3)
obj.calculateRoot()
obj.saveDate()
obj.graph()


# obj4 = fixedPointIteration.FixedPointIterationMethod()
# obj4.setFuncionAndIntialpoint("cos (x) - 2*x", 2)                                      #"cos x - 2x**2 + 7 x + e^x"
# obj4.result()
# #print(obj4.getAppRoots())
# #print(obj4.getErrors())
# obj4.saveDate()                             #"7 x + sin 2*x**x + cos 2**x - x**2 + e^x + 2^x + x + 2**x + x**x + 2**(2*x) + log 2*x "
#
# obj4.graph()


# exp = sym.sympify(obj4.function)
# exp2 = sym.sympify("2**x")
# p = plot(exp)
# #p1 = plot(obj4.appRoots)
# p2 = plot(exp2) # keda kol wa7da lwa7daha
# p.extend(p2)
# p.show()

#obj3 = birgeVieta.birgeVietaMethod()
#obj3.setFuncionAndIntialpoint("x - 1", 0.5)
#print(obj3.calculateRoot())



