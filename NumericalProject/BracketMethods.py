from sympy import *
from sympy.abc import x
from sympy.parsing.sympy_parser import (parse_expr, eval_expr,  stringify_expr,  _token_splittable,standard_transformations,
                                       implicit_multiplication_application,split_symbols_custom, implicit_application,
                                      function_exponentiation, convert_xor, factorial_notation)
import pandas as pd

class BracketMethods:
     function = None
     solution = {}
     root = None
     execution_time = None
     itr_num = None
     precision = None
     self.executionTime = 0;
    
     def parseFuncion(self, function):
       transformations = (standard_transformations + (implicit_multiplication_application, convert_xor, factorial_notation, function_exponentiation))
       function = str( parse_expr(function, transformations = transformations))
       function = function.replace("e", "2.7182818284590452") # to be solved later
       # print("after parsing : " , function)
       return function
   
     def sub(self, value):
       x = float(value)
       return eval(self.function)
   
     def save(self, dict, filename):
        data_table = pd.DataFrame.from_dict(dict)
        data_table.to_csv(filename, index = False)
        
     def print_table(self, dict):
        data_table = pd.DataFrame.from_dict(dict)
        print(data_table)
