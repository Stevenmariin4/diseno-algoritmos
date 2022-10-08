
import numbers
from tokenize import Name
from unicodedata import name
import numpy as np
from Imagen import Image
class Operators:
    _matrizNearby= []
    _matrizFor= []
    def __init__(self) -> None:        
        self.image = Image()
        self._matriz = np.array([[0,0,1,1,1],[0,1,1,0,1],[0,0,1,0,1]])
        #self._matriz = self.image.returnImage(True)
        self._matrizFor = []
        #self.image.printShowImage(self._matriz)
        pass

    # Calcultate is divisible
    def divisible(self,x):
        "This Method Calculate if number is par or impar"
        if x & 1 == 0:
            return True
        else:
            return False
    
    def calculate(self):
        "Method Calculate moduler number in matriz"
        n = self._matriz.shape[0]
        m = self._matriz.shape[1]
        for i in range(n):
            self._matrizNearby.append([])
            for j in range(m):
                up = (i - 1) % n
                down = (i + 1) % n
                left = (j - 1) % m
                rigth = (j + 1) % m
                
                modular = up + down + left + rigth % 2
                self._matrizNearby[i].append(0 if self.divisible(modular) else 1) 
        pass                         

    def calculateCorners(self):
        try:
            n = self._matriz.shape[0]
            m = self._matriz.shape[1]
            for i in range(n):
                    self._matrizNearby.append([])
                    for j in range(m):
                        up = (i - 1) % n
                        down = (i + 1) % n
                        left = (j - 1) % m
                        rigth = (j + 1) % m                            
                        modular = up + down + left + rigth % 2
                        self._matrizNearby[i].append(0 if self.divisible(modular) else 1) 
        except Exception as name:
            print("has ocurred error calculatecorners", name)    
            pass
        
    def converImageBlackWhite(self):
        try:
            self._matrizNearby = self.image.converImageBlackWhite(self._matriz)
        except NameError as name:
            print("has ocurred error in program", name)
                
    def forImagesAndPrint(self,numberIteration:numbers): 
        "This Method for iterations and print image"  
        try:            
            for i in range(numberIteration):
                self._matrizFor = self._matrizNearby
                self.image.printShowImage(self._matrizNearby)      
        except NameError as name:
            print("Has ocurred error in for print image", name)
            pass
    
program = Operators() 
program.calculateCorners()
# program.converImageBlackWhite()
# program.forImagesAndPrint(1)

