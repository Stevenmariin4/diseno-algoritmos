import numpy as np
class CopyArray:
    
    def __init__(self) -> None:
        self.a =  np.array([5,2,3])
        self.b =  np.array([1,4,7])
        self.matriz =  np.array([[1,2,4],[4,5,6],[7,8,9]])
        pass
    
    
    def copyArray(self,array):
        try:
            c = np.zeros(len(array))
            for i in range(len(array)):
                c[i] = array[i]                
            return c    
                
        except NameError as name:
            print(name)    
            pass
        
    def copyMatriz(self,matriz):
        try:
            self.newMatriz = []
            for i in range(matriz.shape[0]):
                for j in range(matriz.shape[1]):
                    if j == 0:
                        self.newMatriz.append([matriz[i][j]])
                    else:
                        self.newMatriz[i].append(j)
            return self.newMatriz                            
        except NameError as name:
            print(name)    
            pass
        
    def initProgram(self):
        self.x = self.copyMatriz(self.matriz)
        print(self.x)
        # self.b = self.copyArray(self.a)
        # self.b[0] = 10
        # self.b[1] = 10
        # self.b[2] = 10
        
        # print(self.a)
        # print(self.b)
        
        
        
program = CopyArray()      
program.initProgram()