import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

class GeometricMatriz:
    array = 0
    def __init__(self) -> None:
        self.array = np.zeros((10,10))
        pass
    # Method print circle
    def printCircle(self):
        self.array[0,3] = 1
        self.array[0,4] = 1
        self.array[0,5] = 1
        self.array[0,6] = 1
        self.array[0,7] = 1
        self.array[1,2] = 1
        self.array[1,8] = 1
        self.array[2,2] = 1
        self.array[2,8] = 1
        self.array[3,2] = 1
        self.array[3,8] = 1
        self.array[4,2] = 1
        self.array[4,8] = 1
        self.array[5,8] = 1
        self.array[5,2] = 1
        self.array[6,8] = 1
        self.array[6,2] = 1
        self.array[7,8] = 1
        self.array[7,2] = 1
        self.array[8,8] = 1
        self.array[8,2] = 1        
        self.array[9,3] = 1
        self.array[9,4] = 1
        self.array[9,5] = 1
        self.array[9,6] = 1
        self.array[9,7] = 1
        print(self.array)
        plt.title("This is circle")
        plt.imshow(self.array,cmap=cm.gray)
        plt.show()

    def printTringule(self):
        self.array[9,0] = 1
        self.array[9,1] = 1
        self.array[9,2] = 1
        self.array[9,3] = 1
        self.array[9,4] = 1
        self.array[9,5] = 1
        self.array[9,6] = 1
        self.array[9,7] = 1
        self.array[9,8] = 1
        self.array[9,9] = 1
        self.array[8,8] = 1
        self.array[8,1] = 1
        self.array[7,7] = 1
        self.array[7,2] = 1
        self.array[6,6] = 1
        self.array[6,3] = 1
        self.array[5,5] = 1
        self.array[5,4] = 1
        print(self.array)
        plt.title("This is tringule")
        plt.imshow(self.array,cmap=cm.gray)
        plt.show()
        pass
    
program = GeometricMatriz()

program.printTringule()