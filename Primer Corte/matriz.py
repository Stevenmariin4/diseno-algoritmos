class Matriz:
    # Var private 
    __numberColumn= 0
    __numberRows = 0
    __matriz= []
    __numberMax = 0
    __numberMin = 0
    # Constructor 
    def __init__(self) -> None:
        pass
    
    # Method poblate matriz whit data digit for user
    def poblateMatriz(self):
        for i in range(self.__numberColumn):
            for j in range(self.__numberRows):
                print("digite el valor de la matriz en el valor de la columna", i)
                print("digite el valor de la matriz en el valor de la fila", j)
                row = int(input())
                if(len(self.__matriz)== 0):
                    self.__matriz = [[row]]
                elif(len(self.__matriz) == i):
                    self.__matriz.append([row])  
                else:
                    self.__matriz[i].append(row)     
        print("La matriz completa es")
        print(self.__matriz)        
        pass
    
    # Method calculate what is max number in matriz
    def calculateNumberMax(self):
        self.__numberMax = self.__matriz[0][0]
        for i in range(self.__numberColumn):
            for j in range(self.__numberRows):
                if(self.__matriz[i][j] > self.__numberMax):
                    self.__numberMax = self.__matriz[i][j]
        print("El numero maximo es ", self.__numberMax)
        pass
    
    # Method calculate what is min number in matriz
    def calculateNumberMin(self):
        self.__numberMin = self.__matriz[0][0]
        for i in range(self.__numberColumn):
            for j in range(self.__numberRows):
                if(self.__matriz[i][j] < self.__numberMax):
                    self.__numberMax = self.__matriz[i][j]        
        print("El numero minimmo es ", self.__numberMin)
        pass
    
    # Method init program
    def initProgram(self):
        self.captureData()
        self.poblateMatriz()  
        self.calculateNumberMax()    
        self.calculateNumberMin()
        pass
    
    # Method Capture data digit for user
    def captureData(self):
        print("ingrese el numero de columnas de la filas")
        self.__numberRows = int(input())
        print("ingrese el numero de columnas de la matriz")
        self.__numberColumn = int(input())
        pass
