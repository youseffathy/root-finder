import parent
from matplotlib import pyplot as plt
import numpy as np
import time

class secantMethod(parent.parent):
    secondInitial = 0

    def __init__(self):
        super(secantMethod, self).__init__()
        self.secondInitial = 0
        return

    def setFuncionAndIntialpoint(self, function, xi, xii):
        super(secantMethod, self).setFuncionAndIntialpoint(function, xi)
        self.secondInitial = xii
        return

    def calculateRoot(self):
        self.list.append(0)
        self.errors.append(None)
        xi = self.initialPoint
        xii = self.secondInitial
        self.appRoots.append([float(xi), float(xii)])
        error = 100
        start = time.time()
        while self.iteration < self.maxIteration and error >= self.epsilon:
            try:
                print("xi = ", xi)
                print("xii = ", xii)
                xiii = xii - (self.fx(self.function, xii) * (xi - xii)) / (
                            self.fx(self.function, xi) - self.fx(self.function, xii))
                print("xiii = ", xiii)
            except:
                raise ZeroDivisionError
                break

            self.appRoots.append(float(xiii))
            try:
                error = abs((xiii - xii) / xiii * 100)
            except:
                self.errors.append(None)
                print("error of relative error because xiii = ", xiii)
                break
            self.errors.append(float(error))
            xi = xii
            xii = xiii
            self.iteration = self.iteration + 1
        end = time.time()
        self.executionTime = end - start
        return self.appRoots[len(self.appRoots) - 1]



    def graph(self, counter):
        if counter > len(self.appRoots)-2:
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
        # for x in self.appRoots:
        #     f.append(self.fx(self.function, x))
        f.append(self.appRoots[0][0])
        f.append(self.appRoots[0][1])
        for i in range(len(self.appRoots)):
            f.append(self.appRoots[i])
        del f[2]
        # now f contains the appRoots with the two initial points
        # f2 is the value of f(x) for all roots in f
        f2 = []
        for x in f:
            f2.append(self.fx(self.function, x))
        # matching the 2 intial points and indicate the new point
        for i in range(counter):
            plt.plot([f[i], f[i+1]], [f2[i], f2[i+1]], 'ro-')
            plt.plot([f[i+1], f[i+2]], [f2[i+1], 0], 'ro-')
            # a vertical line showing the new root
            plt.vlines(f[i+2], ymin=self.fx(self.function,f[i+2]), ymax=0, color='g')
        plt.grid()
        plt.show()