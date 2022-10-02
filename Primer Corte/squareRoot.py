import math


class SquareRoot:
    def __init__(self) -> None:
        pass
    
    def calculateSquareRoot(self):
        try:
            print("Digite un numero")
            number = input()
            number = int(number)
            print("Raiz cuadrada es:", math.sqrt(number))
        except NameError as error: 
            print("Ha ocurrido una excepicion",error)    
        finally:
            print("Ciclo Terminado")   
        pass