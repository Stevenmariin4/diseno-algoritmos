
class CalcultateDivisible:
    # Constructor Application
    def __init__(self) -> None:
        pass
    # Method calculate divisible number
    def CalcultateDivisible(self):
        try:
            print("Digite un numero")
            number = input()
            number = int(number)
            array = list()
            for i in range(number):        
                number = number / 2
                if(number > 1):
                    array.append(number)
            print(array)
        except NameError as error: 
            print("Ha ocurrido una excepicion",error)    
        finally:
            print("Ciclo Terminado")   
        pass

 