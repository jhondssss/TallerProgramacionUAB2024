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
        
# REFACTORIZAR Una clase Hija o SubClase, debe implementar una nueva función que utilice un nuevo arreglo/lista con valores (2020, 2021, 2022, 2023, 2024) para los distintos años Permitidos De Circulación.
# - Esta función debe recibir un parámetro correspondiente al año de fabricación de un coche, así como crear el arreglo mencionado arriba.
# - Si el valor ingresado de las puertas está entre 2-5, continuar con la validación del año, si no, mostrar un mensaje de error como “Revise nuevamente el número de puertas ingresado ya que un automovil/coche no existe uno que tenga [puertas] (valor de puertas, ejemplo: 9)
# - Validar que el año proporcionado está presente en el arreglo, se debe mostrar el mensaje: "El coche con año de fabricación [año] tiene permitido circular." (Donde "[año]" es el valor introducido por el usuario). Si el año NO está en el arreglo, se debe mostrar: "El coche con año de fabricación [año] NO puede circular en Bolivia.”
class Coche(Vehiculo):
    def __init__(self,marca, modelo, puertas) -> None:
        super().__init__(marca, modelo)
        self.puertas = puertas
    def get_puertas(self) -> int: 
        return self.puertas    
    def encender(self) -> None: 
        print("Encendiendo Coche")
    def detener(self) -> None:
        print("Deteniendo Coche")  
       
    
class Clase2(Vehiculo):
    def __init__(self, marca, modelo, amortiguacion) -> None:
        super().__init__(marca, modelo) 
        self.amortiguacion = amortiguacion
        
    def encender(self) -> None: 
        print("Encendiendo Clase2")
    def detener(self) -> None:
        print("Deteniendo Clase2")  