from Divisble import CalcultateDivisible
from algorithmevler import Algorithm
from printGrapic import PrintGrapic
from squareRoot import SquareRoot


class Activites:
    def __init__(self) -> None:
        pass
  
  
    def optionValue(self,option):
        try:
            if option == 1:
                program = SquareRoot()
                program.calculateSquareRoot()
            elif option == 2:
                program = CalcultateDivisible()
                program.CalcultateDivisible()
            elif option == 3:
                program = PrintGrapic()
                program.printGrapic()
            elif option == 4:
                program = Algorithm()
                program.initProgram()       
            else:
                print("Opcion no valida")
        except NameError as error: 
            print("Ha ocurrido una excepicion",error)    
        finally:
            print("Proceso Terminado") 
    def initProgram(self):
        try:
            print("Digite la actividad que desea ejecutar")
            print("1 Calcular raiz cuadrada")
            print("2 Calcular numero divisibles")
            print("3 Imprimir Graficos")
            print("4 Calcular algoritmo de evler")
            number = input()
            number = int(number)
            self.optionValue(number)
        except NameError as error: 
            print("Ha ocurrido una excepicion",error)    
        finally:
            print("Ciclo Terminado")     
        pass


program = Activites()
program.initProgram()