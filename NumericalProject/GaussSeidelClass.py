# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:20:27 2019

@author: esabn
"""

class GaussSeidel:
    
    def __init__(self, n, A, B, epsilon = 0.00001, i_max = 50, initial = [0]):
        self.A = A
        self.B = B
        self.n = n
        if (initial == [0]):
            self.inital = [0] * self.n
        else:
            self.inital = initial
        self.epsilon = epsilon
        self.i_max = i_max
        self.solution = [0] * self.n
        self.steps_dict = {}
        self.steps_dict["iteration"] = []
        l = ["x"+str(j+1) for j in range(n)]
        l2 = ["e"+str(j+1) for j in range(n)]

        for j in l:
            self.steps_dict[j] = []
        for j in l2:
            self.steps_dict[j] = []
    
    def runMethod(self):
        solutions = self.inital
        errors = [100] * self.n
        for itr in range(self.i_max):
            itr_num = itr + 1
            for k in range(self.n):
                solution_old = solutions[k]
                num =sum(-self.A[k][j] * solutions[j] for j in range(self.n) if k != j)
                solutions[k] = (self.B[k][0] + num) / A[k][k]
                errors[k] = abs((((solutions[k] - solution_old) / solutions[k])))
                
            self.steps_dict["iteration"].append(itr_num)
            for j in range(self.n):
                var_name = "x" + str(j+1)
                var_value = solutions[j]
                err_name = "e" + str(j+1)
                err_value = errors[j]
                self.steps_dict[var_name].append(var_value)
                self.steps_dict[err_name].append(err_value)
            if (max(errors) < self.epsilon):
                self.solution = solutions
                return
        self.solution = solutions
        return

A = [[12, 3, -5], [1, 5, 3], [3, 7, 13]]
B = [[1], [28], [76]]
gauss = GaussSeidel(3, A, B, initial = [1, 0, 1])
gauss.runMethod()
print(gauss.solution)
print(gauss.steps_dict)