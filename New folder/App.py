# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:42:10 2019

@author: esabn
"""
import sys
import datetime
from matplotlib import pyplot as plt

from Ui_MainWindow import Ui_MainWindow
from Ui_Result import Ui_DialogResult
from Ui_Result_2 import Ui_DialogResultSeidel
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, \
     QTreeWidgetItem , QTableWidgetItem , QSizePolicy, QPushButton, QFileDialog
from PyQt5 import QtGui, QtCore
from BracketMethods import BracketMethods
from BisectionClass import Bisection
from FalsePosition import FalsePosition
from fixedPointIteration import FixedPointIterationMethod
from newtonRaphason import NewtonRaphasonMethod
from secent import secantMethod
from birgeVieta import birgeVietaMethod
from allMethods import allMethods
from guassElimination import gaussEliminationClass
from Checker import ParserAndChecker
from LU import LUClass
from gaussJordan import gaussJordanClass
from GaussSeidelClass import GaussSeidel

app = QApplication(sys.argv)
app.setStyle('Fusion')

#MainWindow = QMainWindow()
#ui = Ui_MainWindow()
#ui.setupUi(MainWindow)

class Handler_MainWindow:
    
    x_lower = 0
    x_upper = 4
    max_itr = 50
    epsilon = 0.00001
    selected = "Root Finder"
    xl_bisection = 0
    xu_bisection = 0
    xl_falsePosition = 0
    xu_falsePosition = 0
    xi_fixedPoint = 0
    xi_newtonRaphson = 0
    x1_secant = 0
    x2_secant = 0
    xi_biergeVieta = 0
    resultDialog = None
    list_methods = ["Bisection", "False-Position", "Fixed Point", \
                            "Newton-Raphson", "Secant", "Bierge-Vieta"]
    
    def __init__(self):
        self.MainWindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        #self.ui.resultTable.hide()
        #sizePolicy = self.ui.contentWidget.sizePolicy()
        #sizePolicy.setRetainSizeWhenHidden(True)
        #self.ui.contentWidget.setSizePolicy(sizePolicy)
        self.ui.btnGaussSeidel.hide()
        self.ui.btnSingleStep.hide()
        self.ui.contentWidget_1.hide()
        self.ui.contentWidget_2.hide()
        self.ui.btnResult.clicked.connect(self.btnResultClicked)
        self.ui.btnResult_2.clicked.connect(self.btnResultClicked_2)
        self.ui.btnSingleStep.clicked.connect(self.openSingleStep)
        self.ui.btnGaussSeidel.clicked.connect(self.openSeidelDetails)
        
        self.ui.treeSelection.currentItemChanged.connect(self.getSelected)
        self.ui.treeSelection.currentItemChanged.connect(self.setScene)
        self.ui.treeSelection.currentItemChanged.connect(self.setInputWidgets)
        self.ui.actionExit.triggered.connect(app.quit)
        self.method = None
        self.all_methods = list()
        self.method_2 = None
        self.all_methods_2 = list()
    def setScene(self):
        if self.selected == "Root Finder":
            return
        elif self.selected == "System of Equations Solver":
            return
        elif self.selected in ["Bisection", "False-Position", "Fixed Point",\
                               "Newton-Raphson", "Secant", "Bierge-Vieta", "All Methods"]:
            self.ui.contentWidget_0.hide()
            self.ui.contentWidget_1.show()
            self.ui.contentWidget_2.hide()
        else:
            self.ui.contentWidget_0.hide()
            self.ui.contentWidget_1.hide()
            self.ui.contentWidget_2.show()
    
    def setInputWidgets(self):
        if self.selected in ["Bisection", "False-Position", "Fixed Point",\
                               "Newton-Raphson", "Secant", "Bierge-Vieta", "All Methods"]:
            self.setInputsWidgets()
        elif self.selected in ["Gaussian-elimination", "LU decomposition", "Gaussian-Jordan", \
                            "Gauss-Seidel", "All"]:
            self.setInputsWidgets_2()
    def autoSave(self):
        if self.selected == "All Methods":
            for i in range(6):
                method = self.all_methods[i]
                filename = self.list_methods[i] + "_" + \
                (str(datetime.datetime.now()).split())[1].replace(":", "") + ".csv"
                method.save(method.solution, filename)
        else:
            filename = self.selected + "_" + \
            (str(datetime.datetime.now()).split())[1].replace(":", "") + ".csv"
            self.method.save(self.method.solution, filename)
            
    def autoSave_2(self):
        if self.selected == "All":
            filename = "Gauss-Seidel_" + (str(datetime.datetime.now()).split())[1].replace(":", "") + ".csv"
            self.all_methods_2[3].save(filename)
        elif self.selected == "Gauss-Seidel":
            filename = "Gauss-Seidel_" + (str(datetime.datetime.now()).split())[1].replace(":", "") + ".csv"
            self.method_2.save(filename)
    def btnResultClicked_2(self):
        self.readInputs_2()
        self.methodFactory_2()
        self.run_2()
        if self.ui.actionAuto_Save.isChecked():
            self.autoSave_2()
        self.populateResultTable_2()
        self.ui.btnGaussSeidel.setEnabled(True)
    def btnResultClicked(self):
        self.readInputs()
        self.methodFactory()
        self.run()
        
        if self.ui.actionAuto_Save.isChecked():
            self.autoSave()
        self.populateResultTable()
        self.ui.btnSingleStep.setEnabled(True)
    
    def readInputs(self):
        self.function = self.ui.txtFunction.text()
        self.max_itr = int(self.ui.txtMaxItr.text())
        self.epsilon = float(self.ui.txtEpsilon.text())
        
        if self.selected == "All Methods":
            self.xl_bisection = float(self.ui.txtXlBisection.text())
            self.xu_bisection = float(self.ui.txtXuBisection.text())
            self.xl_falsePosition = float(self.ui.txtXlFalsePosition.text())
            self.xu_falsePosition = float(self.ui.txtXuFalsePosition.text())
            self.xi_fixedPoint = float(self.ui.txtXiFixedPoint.text())
            self.xi_newtonRaphson = float(self.ui.txtXiNewtonRaphson.text())
            self.x1_secant = float(self.ui.txtX1Secant.text())
            self.x2_secant = float(self.ui.txtX2Secant.text())
            self.xi_biergeVieta = float(self.ui.txtXiBiergeVieta.text())
        else:
            self.x_lower = float(self.ui.txtXl.text())
            if not self.ui.txtXu.isHidden(): 
                self.x_upper = float(self.ui.txtXu.text())
        
        
    def readInputs_2(self):
        self.equations = self.ui.txtEditEquations.toPlainText().split("\n")
        if (self.selected == "All") | (self.selected == "Gauss-Seidel"):
            self.initial = [float(i) for i in self.ui.txtEditInitial.toPlainText().split("\n")]
            self.max_itr = self.ui.txtMaxItr_2.text()
            self.epsilon = self.ui.txtEpsilon_2.text()
            
    def openSeidelDetails(self):
        #self.btnResultClicked_2()
        self.resultDialog = Handler_DialogResultSeidel(self)
    
    def populateResultTable_2(self):
        self.ui.resultTable.clear()
        (self.ui.resultTable.setVerticalHeaderItem(i, QTableWidgetItem()) for i in range(self.ui.resultTable.rowCount()))
        if self.selected == "All":
            self.ui.resultTable.setColumnCount(self.all_methods_2[0].parser.numOfVariables)
            self.ui.resultTable.setHorizontalHeaderLabels(self.all_methods_2[0].parser.variables)
            self.ui.resultTable.setRowCount(3) #will be incremented by 1
            list_methods = ["Gaussian-elimination", "Gaussian-Jordan", \
                            "Gauss-Seidel"] #, "LU decomposition"
            self.ui.resultTable.setVerticalHeaderLabels(list_methods)
            for i in range(len(self.all_methods_2)):
                method = self.all_methods_2[i]
                for j in range(len(method.parser.variables)):
                    item = QTableWidgetItem()
                    item.setText(str(method.solution[j]))
                    self.ui.resultTable.setItem(i, j, item)            
        else:
            self.ui.resultTable.setColumnCount(self.method_2.parser.numOfVariables)
            self.ui.resultTable.setHorizontalHeaderLabels(self.method_2.parser.variables)
            self.ui.resultTable.setRowCount(1)
            self.ui.resultTable.setVerticalHeaderLabels([self.selected])
            for j in range(len(self.method_2.parser.variables)):
                item = QTableWidgetItem()
                item.setText(str(self.method_2.solution[j]))
                self.ui.resultTable.setItem(0, j, item)
            
    def openSingleStep(self):
        #self.btnResultClicked()
        self.resultDialog = Handler_DialogResult(self)
    def populateResultTable(self):
        
        self.ui.resultTable.clear()
        self.ui.resultTable.setColumnCount(5)
        self.ui.resultTable.setHorizontalHeaderLabels(["Number of Iterations" \
        , "Execution Time", "Approximate Root", "Precision", "Graph"])
        (self.ui.resultTable.setVerticalHeaderItem(i, QTableWidgetItem()) for i in range(self.ui.resultTable.rowCount()))
        if self.selected == "All Methods":
            self.ui.resultTable.setRowCount(6)
            self.ui.resultTable.setVerticalHeaderLabels(self.list_methods)
            for i in range(len(self.all_methods)):
                self.addToTable(self.ui.resultTable, self.all_methods[i], i)
        else:
            self.ui.resultTable.setRowCount(1)
            (self.ui.resultTable.setVerticalHeaderItem(i, QTableWidgetItem()) for i in range(self.ui.resultTable.rowCount()))
            self.ui.resultTable.setVerticalHeaderLabels([self.selected])
            self.addToTable(self.ui.resultTable, self.method, 0)
        
    def methodFactory_2(self):
        self.all_methods_2 = []
        self.method_2 = None
        parser = None
        parser = ParserAndChecker(self.equations.copy())
        
        if self.selected == "Gaussian-elimination":
            self.method_2 = gaussEliminationClass(parser)
        elif self.selected == "LU decomposition":
            self.method_2 = LUClass(parser)
        elif self.selected == "Gaussian-Jordan":
            self.method_2 = gaussJordanClass(parser)
        elif self.selected == "Gauss-Seidel":
            self.method_2 = GaussSeidel(parser)
        elif self.selected == "All":
            self.all_methods_2.append(gaussEliminationClass(ParserAndChecker(self.equations)))
            #self.all_methods_2.append(LUClass(ParserAndChecker(self.equations)))
            self.all_methods_2.append(gaussJordanClass(ParserAndChecker(self.equations)))
            self.all_methods_2.append(GaussSeidel(ParserAndChecker(self.equations)))
            
    def methodFactory(self):
        self.all_methods = []
        self.method = None
        if self.selected == "Bisection":
            self.method = Bisection(self.function, self.x_lower, self.x_upper, self.epsilon, self.max_itr)
        elif self.selected == "False-Position":
            self.method = FalsePosition(self.function, self.x_lower, self.x_upper, self.epsilon, self.max_itr)
        elif self.selected == "Fixed Point":
            self.method = FixedPointIterationMethod()
            self.method.setFuncionAndIntialpoint(self.function, self.x_lower)
            self.method.setMaxIteration(self.max_itr)
            self.method.setEpsilon(self.epsilon)
        elif self.selected == "Newton-Raphson":
            self.method = NewtonRaphasonMethod()
            self.method.setFuncionAndIntialpoint(self.function, self.x_lower)
            self.method.setMaxIteration(self.max_itr)
            self.method.setEpsilon(self.epsilon)
        elif self.selected == "Secant":
            self.method = secantMethod()
            self.method.setFuncionAndIntialpoint(self.function, self.x_lower, self.x_upper)
            self.method.setMaxIteration(self.max_itr)
            self.method.setEpsilon(self.epsilon)
        elif self.selected == "Bierge-Vieta":
            self.method = birgeVietaMethod()
            self.method.setFuncionAndIntialpoint(self.function, self.x_lower)
            self.method.setMaxIteration(self.max_itr)
            self.method.setEpsilon(self.epsilon)
        elif self.selected == "All Methods":
            self.all_methods.append(Bisection(self.function, self.xl_bisection, self.xu_bisection, self.epsilon, self.max_itr))
            self.all_methods.append(FalsePosition(self.function, self.xl_falsePosition, self.xu_falsePosition, self.epsilon, self.max_itr))
            method = FixedPointIterationMethod()
            method.setFuncionAndIntialpoint(self.function, self.xi_fixedPoint)
            method.setMaxIteration(self.max_itr)
            method.setEpsilon(self.epsilon)
            self.all_methods.append(method)
            method = NewtonRaphasonMethod()
            method.setFuncionAndIntialpoint(self.function, self.xi_newtonRaphson)
            method.setMaxIteration(self.max_itr)
            method.setEpsilon(self.epsilon)
            self.all_methods.append(method)
            method = secantMethod()
            method.setFuncionAndIntialpoint(self.function, self.x1_secant, self.x2_secant)
            method.setMaxIteration(self.max_itr)
            method.setEpsilon(self.epsilon)
            self.all_methods.append(method)
            method = birgeVietaMethod()
            method.setFuncionAndIntialpoint(self.function, self.xi_biergeVieta)
            method.setMaxIteration(self.max_itr)
            method.setEpsilon(self.epsilon)
            self.all_methods.append(method)
    
    def run_2(self):
        if self.selected == "All":
            for method in self.all_methods_2:
                method.solve()
        else :
            self.method_2.solve()
    
    def run(self):
        if self.selected == "All Methods":
            for method in self.all_methods:
                method.runMethod()
        else :
            self.method.runMethod()
        
    def setInputsWidgets_2(self):
        self.ui.contentWidget_1.hide()
        self.ui.contentWidget_2.show()
        self.ui.btnSingleStep.hide()
        if (self.selected == "Gauss-Seidel") | (self.selected =="All"):
            self.ui.txtEpsilon_2.show()
            self.ui.txtMaxItr_2.show()
            self.ui.lblEpsilon_2.show()
            self.ui.lblMaxItr_2.show()
            self.ui.txtEditInitial.show()
            self.ui.btnGaussSeidel.show()
        else:
            self.ui.txtEpsilon_2.hide()
            self.ui.txtMaxItr_2.hide()
            self.ui.lblEpsilon_2.hide()
            self.ui.lblMaxItr_2.hide()
            self.ui.txtEditInitial.hide()
            self.ui.btnGaussSeidel.hide()

            


        
    def setInputsWidgets(self):
        self.ui.contentWidget_2.hide()
        self.ui.contentWidget_1.show()
        self.ui.btnGaussSeidel.hide()
        self.ui.btnSingleStep.show()
        if self.selected == "Bisection":
            self.ui.tabAllMethods.hide()
            self.ui.lblXl.setText("Xl:")
            self.ui.lblXl.show()
            self.ui.txtXl.show()
            self.ui.lblXu.setText("Xu:")
            self.ui.lblXu.show()
            self.ui.txtXu.show()
        elif self.selected == "False-Position":
            self.ui.tabAllMethods.hide()
            self.ui.lblXl.setText("Xl:")
            self.ui.txtXl.show()
            self.ui.lblXl.show()
            self.ui.lblXu.setText("Xu:")
            self.ui.lblXu.show()
            self.ui.txtXu.show()
        elif self.selected == "Fixed Point":
            self.ui.tabAllMethods.hide()
            self.ui.lblXl.setText("Xi:")
            self.ui.lblXl.show()
            self.ui.txtXl.show()
            self.ui.lblXu.setText("Xu:")
            self.ui.txtXu.hide()
            self.ui.lblXu.hide()
        elif self.selected == "Newton-Raphson":
            self.ui.tabAllMethods.hide()
            self.ui.lblXl.setText("Xi:")
            self.ui.lblXl.show()
            self.ui.txtXl.show()
            self.ui.lblXu.setText("Xu:")
            self.ui.lblXu.hide()
            self.ui.txtXu.hide()
        elif self.selected == "Secant":
            self.ui.tabAllMethods.hide()
            self.ui.lblXl.setText("X1:")
            self.ui.lblXl.show()
            self.ui.txtXl.show()
            self.ui.lblXu.setText("X2:")
            self.ui.lblXu.show()
            self.ui.txtXu.show()
        elif self.selected == "Bierge-Vieta":
            self.ui.tabAllMethods.hide()
            self.ui.lblXl.setText("Xi:")
            self.ui.lblXl.show()
            self.ui.txtXl.show()
            self.ui.lblXu.setText("Xu:")
            self.ui.lblXu.hide()
            self.ui.txtXu.hide()
        elif self.selected == "All Methods":
            self.ui.lblXl.hide()
            self.ui.txtXl.hide()
            self.ui.lblXu.hide()
            self.ui.txtXu.hide()
            self.ui.tabAllMethods.show()

    def getSelected(self):
        if not self.resultDialog == None:
            return
        selected = mainWindow.ui.treeSelection.currentItem().text(0)
        if selected == "Root Finder":
            return
        elif selected == "System of Equations Solver":
            return
        self.method = None
        self.all_methods = None
        self.method_2 = None
        self.all_methods_2 = None
        self.ui.btnGaussSeidel.setDisabled(True)
        self.ui.btnSingleStep.setDisabled(True)
        self.selected = selected
        
        
    def addToTable(self, tableWidget, method, row):
    
        item_itrNum = QTableWidgetItem()
        item_itrNum.setText(str(method.getNumOfIteration()))
        tableWidget.setItem(row, 0, item_itrNum)
        item_executionTime = QTableWidgetItem()
        item_executionTime.setText(str(method.executionTime))
        tableWidget.setItem(row, 1, item_executionTime)
        item_root = QTableWidgetItem()
        item_root.setText(str(method.getRoot()))
        tableWidget.setItem(row, 2, item_root)
        item_precision = QTableWidgetItem()
        item_precision.setText(str(method.getPrecision()))
        tableWidget.setItem(row, 3, item_precision)
        item_graph = QTableWidgetItem()
        tableWidget.setItem(row, 4, item_graph)
        if type(method) is birgeVietaMethod:
            item_graph.setText("-")
            return
        button = QPushButton("show..")
        button.setFlat(True)
        font = button.font()
        font.setUnderline(True)
        button.setFont(font)
        button.clicked.connect(lambda: self.btnGraphClicked(method, method.getNumOfIteration()))
        tableWidget.setCellWidget(row, 4, button)
        
    def btnGraphClicked(self, method, itr_num):
        plt.close()
        method.graph(itr_num)
    
   # def addGraphButtons(self, tableWidget, method):
    #    if type(method) is list:
     #       for i in range(tableWidget.rowCount()):
      #          button = QPushButton("show..")
       #         button.setFlat(True)
        #        font = button.font()
         #       font.setUnderline(True)
          #      button.setFont(font)
           #     item = QTableWidgetItem()
            #    tableWidget.setItem(i, 4, item)
             #   button.clicked.connect(f)

class Handler_DialogResultSeidel:
    DialogResultSeidel = QDialog()
    ui = Ui_DialogResultSeidel()
    ui.setupUi(DialogResultSeidel)
    
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.setScene()
        self.ui.btnShowGraph.clicked.connect(self.btnGraphClicked)
        self.DialogResultSeidel.accepted.connect(self.manualSave)
        self.DialogResultSeidel.rejected.connect(self.dialogRejected)
        self.DialogResultSeidel.show()
    
    def dialogRejected(self):
        self.mainWindow.resultDialog = None
    def btnGraphClicked(self):
        if self.mainWindow.selected == "All":    
            plt.close()
            self.mainWindow.all_methods_2[3].graph()
        else:
            plt.close()
            self.mainWindow.method_2.graph()
    def populateTreeWidget(self, treeWidget, dic):
        
        treeWidget.setHeaderItem(QTreeWidgetItem())
        keys = self.listKeys(dic)
        treeWidget.setColumnCount(len(keys))
        treeWidget.setHeaderLabels(keys)
        for i in range(len(dic[keys[0]])):
            item = QTreeWidgetItem(treeWidget)
            for j in range(len(keys)):
                item.setText(j, str((dic[keys[j]])[i]))
                
    def setScene(self):
        
        self.ui.treeResult
        self.ui.treeResult.clear()
        if self.mainWindow.selected == "All":
            self.populateTreeWidget(self.ui.treeResult, self.mainWindow.all_methods_2[2].steps_dict) # will be incremented
        else:
            self.populateTreeWidget(self.ui.treeResult, self.mainWindow.method_2.steps_dict)
    def listKeys(self, dic):
        return list(dic.keys())
    
    def manualSave(self):
        filename, _ = QFileDialog.getSaveFileName(self.DialogResultSeidel, "Save file",\
            "Untitled", "comma-separated values (*.csv)")
        if filename:
            if self.mainWindow.selected == "All":     
                self.mainWindow.all_methods_2.save(filename)
            else:
                self.mainWindow.method_2.save(filename)
    
    
class Handler_DialogResult:
    DialogResult = QDialog()
    ui = Ui_DialogResult()
    ui.setupUi(DialogResult)
    
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.setScene()
        self.ui.btnShowGraph.clicked.connect(self.btnGraphClicked)
        self.ui.btnAllMethodsGraph1.clicked.connect(self.btnAllMethodsGraph1Clicked)
        self.ui.btnAllMethodsGraph2.clicked.connect(self.btnAllMethodsGraph2Clicked)
        self.DialogResult.accepted.connect(self.manualSave)
        self.DialogResult.rejected.connect(self.dialogRejected)
        if not (self.ui.treeResult.isHidden()):
            self.ui.treeResult.setFocus()
        else:
            self.ui.treeResultBisecition.setFocus()
        self.DialogResult.show()

     

    def dialogRejected(self):
        self.mainWindow.resultDialog = None
    
    def manualSave(self):
        if self.mainWindow.selected == "All Methods":
            folder = QFileDialog.getExistingDirectory(self.DialogResult, "Choose a Folder", "")
            if folder:       
                for i in range(6):
                    method = self.mainWindow.all_methods[i]
                    filename = folder + "/" + self.mainWindow.list_methods[i] + ".csv"
                    method.save(method.solution, filename)
            else:
                pass
        else:
            filename, _ = QFileDialog.getSaveFileName(self.DialogResult, "Save file",\
            "Untitled", "comma-separated values (*.csv)")
            if filename:
                self.mainWindow.method.save(self.mainWindow.method.solution, filename)
            else:
                pass
    
    def btnAllMethodsGraph1Clicked(self):
        plt.close()
        self.allMethodsObj.graph_roots()
    def btnAllMethodsGraph2Clicked(self):
        plt.close()
        self.allMethodsObj.graph_errors()
    def populateTreeWidget(self, treeWidget, dic):
        
        treeWidget.setHeaderItem(QTreeWidgetItem())
        keys = self.listKeys(dic)
        treeWidget.setColumnCount(len(keys))
        treeWidget.setHeaderLabels(keys)
        for i in range(len(dic[keys[0]])):
            item = QTreeWidgetItem(treeWidget)
            for j in range(len(keys)):
                item.setText(j, str((dic[keys[j]])[i]))
        
        
    def listKeys(self, dic):
        return list(dic.keys())
    
    def setScene(self):
        
        if self.mainWindow.selected == "All Methods":
            self.allMethodsObj = allMethods(self.mainWindow.all_methods)
            self.ui.btnAllMethodsGraph1.show()
            self.ui.btnAllMethodsGraph2.show()
            self.ui.treeResult.hide()
            self.ui.tabAllMethods.show()
            self.list_treeResults = [self.ui.treeResultBisecition,self.ui.treeResultFalsePosition\
            , self.ui.treeResultFixedPoint, self.ui.treeResultNewtonRaphson\
            , self.ui.treeResultSecant, self.ui.treeResultBiergeVieta]
            for i in range(len(self.list_treeResults)):
                self.list_treeResults[i].clear()
                self.populateTreeWidget(self.list_treeResults[i], self.mainWindow.all_methods[i].solution)
            
      #      for i in self.list_treeResults:
       #         i.currentItemChanged.connect(self.f)
        else:
            self.ui.btnAllMethodsGraph1.hide()
            self.ui.btnAllMethodsGraph2.hide()
            self.ui.tabAllMethods.hide()
            self.ui.treeResult.show()
            self.ui.treeResult.clear()
            self.populateTreeWidget(self.ui.treeResult, self.mainWindow.method.solution)
         #   self.ui.treeResult.currentItemChanged.connect(self.getSelected)
    
    
    def btnGraphClicked(self):
        itr_num = self.getCurrentItr()
        print(itr_num)
        method = self.getCurrentMethod()
        if not type(method) is birgeVietaMethod:
            plt.close()
            method.graph(itr_num)
        
    def getCurrentMethod(self):
        if (self.mainWindow.selected == "All Methods"):
            return self.mainWindow.all_methods[self.ui.tabAllMethods.currentIndex()]
        else:
            return self.mainWindow.method
    def getCurrentItr(self):
        if (self.mainWindow.selected == "All Methods"):    
            return int(self.list_treeResults[self.ui.tabAllMethods.currentIndex()].currentItem().text(0))
        else:
            return int(self.ui.treeResult.currentItem().text(0))

mainWindow = Handler_MainWindow()

mainWindow.MainWindow.show()
sys.exit(app.exec_())