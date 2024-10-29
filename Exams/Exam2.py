class Vehiculo:
    def __init__(self, marca, modelo) -> None:
        self.__marca = marca
        self.__modelo = modelo
        
    def get_marca(self) -> str: 
        return self.__marca
    def get_tipo(self) -> str: 
        return self.__modelo
    def encender(self) -> None: 
        print("Encendiendo vehículo")
    def detener(self) -> None:
        print("Deteniendo vehículo")  
        
class Clase1(Vehiculo):
    def __init__(self,marca, modelo, puertas) -> None:
        super().__init__(marca, modelo)
        self.puertas = puertas
    def get_puertas(self) -> int: 
        return self.puertas    
    
    def encender(self) -> None: 
        print("Encendiendo clase1")
    def detener(self) -> None:
        print("Deteniendo clase1")  
       
    
class Clase2(Vehiculo):
    def __init__(self, marca, modelo, amortiguacion) -> None:
        super().__init__(marca, modelo) 
        self.amortiguacion = amortiguacion
        
    def encender(self) -> None: 
        print("Encendiendo Clase2")
    def detener(self) -> None:
        print("Deteniendo Clase2")  