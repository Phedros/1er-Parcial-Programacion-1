from Estadisticas import Estadisticas

class Jugador:
    def __init__(self,nombre=0,posicion=0,logros=0,estadisticas=0):
        self.__nombre = nombre
        self.__posicion = posicion
        self.__logros = logros
        self.__estadisticas = estadisticas

    # Getters y setters nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    # Getters y setters posicion

    @property
    def posicion(self):
        return self.__posicion

    @posicion.setter
    def posicion(self, posicion):
        self.__posicion = posicion

    # Getters y setters logros

    @property
    def logros(self):
        return self.__logros

    @logros.setter
    def logros(self, logros):
        self.__logros = logros

    # Getters y setters estadisticas

    @property
    def estadisticas(self):
        return self.__estadisticas

    @estadisticas.setter
    def estadisticas(self, estadisticas):
        self.__estadisticas = estadisticas

    def mostrar_logros(self):
        print(f'Los logros {self.nombre} son los siguientes: ')
        for logro in self.logros:
            print('\t' + logro)
        

