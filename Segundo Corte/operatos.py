
import numbers
import numpy as np
from Imagen import Image
class Operators:
    _matrizNearby= []
    def __init__(self) -> None:        
        self.image = Image()
        self._matriz = self.image.returnImage(True)
        self.image.printShowImage(self._matriz)
        pass

    # Calcultate is divisible
    def divisible(self,x):
        "This Method Calculate if number is par or impar"
        if x & 1 == 0:
            return True
        else:
            return False
    
    def calculate(self):
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
                
    def forImagesAndPrint(self,numberIteration:numbers): 
        "This Method for"  
        for i in range(numberIteration):
             self._matriz = self._matrizNearby
             self.image.printShowImage(self._matrizNearby)      
        pass     
    
program = Operators()    
program.calculate()
program.forImagesAndPrint(2)

