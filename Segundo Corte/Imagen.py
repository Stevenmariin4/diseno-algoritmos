from xmlrpc.client import Boolean
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import imageio as io

class Image:
    def __init__(self) -> None:
        self.image = None
        self.arrayPixel= np.array([0,0,0,0,0])
        pass
    # This Method return to image in scale gray dependency of var withGray type Bool
    def returnImage(self,withGray:Boolean):
        "This Method return to image in scale gray dependency of var withGray type Bool "
        returnGray = True if withGray else False
        self.withGray = returnGray
        image = io.imread(r'https://images.unsplash.com/photo-1474511320723-9a56873867b5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8&w=1000&q=80',as_gray=returnGray)
        return image

    def calculateDimen(self,withGray):
        try:
            print("Dimensiones de la imagen")
            newImage= self.returnImage(withGray)
            print(newImage.shape)
            print("imagen original RGB color tes canales")
            self.printShowImage(newImage)
        except NameError as name:
            print(name)    
            pass

    def printShowImage(self, newImage):
        "This method Show image"
        try:
            plt.imshow(newImage, cmap=cm.gray) if self.withGray else plt.imshow(newImage)  
            plt.show()        
        except NameError as name:
            print(name)    
            pass    

    def calculatePixeles(self):
        try:
            image= self.returnImage(True)
            for i in range(image.shape[0]):
                for j in range(image.shape[1]):
                    value = int(image[i][j])
                    if  value >= 0 and  value <= 50:
                        self.arrayPixel[0] = self.arrayPixel[0] + 1
                    if  value >=51 and  value <= 100:   
                        self.arrayPixel[1] = self.arrayPixel[1] + 1
                    if  value >=101 and  value <= 150:   
                        self.arrayPixel[2] = self.arrayPixel[2] + 1                
                    if  value >=151 and  value <= 200:   
                        self.arrayPixel[3] = self.arrayPixel[3] + 1                    
                    if  value >=201 and  value <= 255:   
                        self.arrayPixel[4] = self.arrayPixel[4] + 1                    
        except NameError as name:
            print(name)            
            pass
        pass  

    def printPixeles(self):
        print("Numero de pixeles de 0 a 50", self.arrayPixel[0])
        print("Numero de pixeles de 51 a 100", self.arrayPixel[1])
        print("Numero de pixeles de 101 a 150", self.arrayPixel[2])
        print("Numero de pixeles de 151 a 200", self.arrayPixel[3])
        print("Numero de pixeles de 201 a 250", self.arrayPixel[4])
        print("El valor de el arreglo es:")
        print(self.arrayPixel)
        print("Plot de el arreglo")
        data = {'0-50':self.arrayPixel[0],'51-100':self.arrayPixel[1],'101-150':self.arrayPixel[2],'151-200':self.arrayPixel[3],'201-255':self.arrayPixel[4]}
        pixel = list(data.keys())
        values = list(data.values())
        plt.bar(pixel, values, color ='blue',
            width = 0.4)
        plt.title("Range Pixel for value")
        plt.show()
        pass



