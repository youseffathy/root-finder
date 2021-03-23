import parent
from matplotlib import pyplot as plt
import numpy as np
import time
class NewtonRaphasonMethod(parent.parent):
    slopes = []

    def __init__(self):
        super(NewtonRaphasonMethod, self).__init__()
        return

    def calculateRoot(self):

        xi = self.initialPoint
        self.appRoots.append(float(xi))
        self.list.append(0)
        self.errors.append(None)
        error = 100
        start = time.time()
        while self.iteration < self.maxIteration and error >= self.epsilon:
            self.iteration = self.iteration + 1
            deriv = self.derivfx(self.derivative, xi)
            if (deriv <= 10 ** -7):
                deriv = 0
            self.slopes.append(float(deriv))
            try:  # in order to avoid division by zero when f'(x) = 0
                print(self.fx(self.function, xi), "------", deriv)
                xii = xi - (self.fx(self.function, xi) / deriv)
            except:
                self.appRoots.append(None)
                self.errors.append(None)
                raise ZeroDivisionError

            try:
                 error = abs((xii - xi) / xii * 100)
            except:
                self.errors.append(None)
                raise ZeroDivisionError
                 
            self.appRoots.append(float(xii))
            self.errors.append(float(error))
            xi = xii
        end = time.time()
        self.executionTime = end - start
        return self.appRoots[len(self.appRoots) - 1]


    def graph(self, counter):
        if counter >= len(self.appRoots):
            counter = len(self.appRoots)-1
        left = 0
        right = 0
        if (self.initialPoint > 0):
            right = self.initialPoint
            left = -self.initialPoint
        elif self.initialPoint == 0:
            right = 3
            left = -3
        else:
            right = -self.initialPoint
            left = self.initialPoint
        # range of f(x)
        xx = np.arange(left-1, right+1, 0.01)
        f = []
        for x in xx:
            f.append(self.fx(self.function, x))
        # plotting f(x)
        plt.plot(xx, f, 'b')
        f = []
        for x in self.appRoots:
            f.append(self.fx(self.function, x))
        # plotting tangents
        merged_list = [(self.appRoots[i], f[i]) for i in range(0, len(self.appRoots))]
        print("helooo",merged_list)
        # plot lines
        for i in range(counter):
            plt.plot([self.appRoots[i], self.appRoots[i+1]], [f[i], 0],'ro-')
            # a vertical line showing the new root
            plt.vlines(self.appRoots[i+1], ymin=0, ymax=f[i+1], color='g')

        plt.grid()
        plt.show()