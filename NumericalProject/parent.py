from sympy import *
from sympy.abc import x
from sympy.parsing.sympy_parser import (parse_expr, eval_expr,  stringify_expr,  _token_splittable,standard_transformations,
                                       implicit_multiplication_application,split_symbols_custom, implicit_application,
                                      function_exponentiation, convert_xor, factorial_notation)
import pandas as pd
class parent:
    
   def __init__(self):      
       self.list = []
       self.function = None
       self.derivative = None
       self.maxIteration = 50
       self.iteration = 0
       self.executionTime = 0
       self.epsilon = 0.00001
       self.initialPoint = 0
       self.appRoots = []
       self.errors = []    
       self.executionTime = 0;
       self.dic = {}
       return

   def setFuncionAndIntialpoint(self, function, xi, xii = None):
       self.function = self.parseFuncion(function)
       self.initialPoint = xi
       try:
           self.fx(function,xi)
       except:
           print("More than one variable !")
       self.calculateDerivative()
       return
   
   def setMaxIteration(self, maxIteration):
       self.maxIteration= maxIteration
       return

   def setEpsilon(self, epsilon):
        self.epsilon = epsilon
        return


   def parseFuncion(self, function):
       transformations = (standard_transformations + (implicit_multiplication_application, convert_xor, factorial_notation, function_exponentiation))
       function = str( parse_expr(function, transformations = transformations))
       function = function.replace("e", "2.7182818284590452") # to be solved later
       # print("after parsing : " , function)
       return function

   def calculateDerivative(self):
       self.derivative = str(diff(self.function))
       # print("after derivative : " , self.derivative)
       return

   def fx(self,function, approx):
       x = float(approx)
       return eval(function)
       

   def derivfx(self, function, approx):
        x = float(approx)
        return eval(function)

   def getErrors(self):
       return self.errors

   def getAppRoots(self):
       return self.appRoots

   def getSlopes(self):
       return self.slopes
   def getNumOfIteration(self):
       return self.iteration

   def saveDate(self):
       for i in range(self.iteration):
           self.list.append(i+1)
       self.dic = {}
       self.dic['iterations'] = self.list
       self.dic['appRoots'] = self.appRoots
       self.dic['errors'] = self.errors
       print(self.dic)
       self.save(self.dic, "save.csv")
       return self.dic
   def save(self, dict, filename):
        data_table = pd.DataFrame.from_dict(dict)
        data_table.to_csv(filename, index = False)
