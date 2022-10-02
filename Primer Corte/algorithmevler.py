import matplotlib.pyplot as plt
import numpy as np
class Algorithm:
    # Var private for calculate algorithm
    __fsDeta = 0
    __ArrayS = []
    __ArrayT = []
    # Constructor Application
    def __init__(self) -> None:
            self.iterationNum = 0
            self.valueDelta =0
            self.valueS= 0
            self.valueT= 0
            self.fs = 0
            self.__fsDeta = 0
            self.__ArrayS =[]
            self.__ArrayT =[]
            pass

    # Method capture data of user
    def captureData(self):
        print("enter the interations")
        self.iterationNum = int(input())
        print("enter initial value of S")
        self.valueS = int(input())
        print("enter initial value of T")
        self.valueT = int(input())
        print("enter value of delta")
        self.valueDelta = float(input())
        pass
    
    # Method calculate new value of function delta
    def calculateValueFsDelta(self):
        x = self.valueDelta * -10
        self.__fsDeta = self.valueS + -x
        pass

    # Method Calcula of value iteration for number digited user
    def  calculationAlgorithm(self):
            self.calculateValueFsDelta()
            for i in range(int(self.iterationNum)):
                self.valueT = self.valueT + self.valueDelta
                self.__ArrayT.append(self.valueT)
                print("Value of fuction T + Delta in position: ", i, " is: ", self.valueT)
                self.valueS = self.valueS / self.__fsDeta
                self.__ArrayS.append(self.valueS)
                print("Value of fuction algoritmhe of evler in position: ",i ," is:", self.valueS)
            pass
    
    # Method print grapic
    def printGrapic(self):
        plt.title("Values T * S")
        plt.xlabel("Print S")
        plt.ylabel("Print T")
        plt.plot(self.__ArrayS,self.__ArrayT)
        plt.show()
        pass

    # Method init program and call other methods for calculate algorithm
    def initProgram(self):
        self.captureData()
        self.calculationAlgorithm()
        self.printGrapic()
        pass
