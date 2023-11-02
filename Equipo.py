import json
import re
from Jugador import Jugador
from Estadisticas import Estadisticas


class Equipo:
    def __init__(self, nombre_equipo=None, lista_de_jugadores=None):
        self.__nombre_equipo = nombre_equipo
        self.__lista_de_jugadores = lista_de_jugadores
    
    #Getters y setters nombre_equipo

    @property
    def nombre_equipo(self):
        return self.__nombre_equipo
    
    @nombre_equipo.setter
    def nombre_equipo(self, nombre_equipo):
        self.__nombre_equipo = nombre_equipo

    #Getters y setters lista_jugadores

    @property
    def lista_jugadores(self):
        return self.__lista_de_jugadores
    
    @lista_jugadores.setter
    def lista_jugadores(self, lista_jugadores):
        self.__lista_de_jugadores = lista_jugadores

    def cargar_equipo_json(self, direccion_archivo: str) -> list[dict]:
        '''
        Lee un archivo json y devuelve una lista de jugadores
        '''
        lista_jugadores_archivo = []
        lista_jugadores = []
        nombre_equipo = ''
        try:
            with open(direccion_archivo, "r", encoding='utf-8') as archivo_json:
                json_jugadores_archivo = json.load(archivo_json)
                lista_jugadores_archivo = json_jugadores_archivo['jugadores']
                nombre_equipo_ingresado = json_jugadores_archivo['equipo']
        except:
            print("error")
    
        self.nombre_equipo = nombre_equipo_ingresado

        for jugador in lista_jugadores_archivo:
            nombre = jugador['nombre']
            posicion = jugador['posicion']
            logros = jugador['logros']
            estadisticas = Estadisticas(jugador['estadisticas'])
            jugador_objeto = Jugador(nombre,posicion,logros,estadisticas)
            lista_jugadores.append(jugador_objeto)
        self.lista_jugadores = lista_jugadores
        

    def mostrar_lista_jugadores(self):
        '''
        Muestra lista de jugadores
        Imprime en formato 'Nombre - posicion'
        '''
        for jugador in self.__lista_de_jugadores:
            print('{0} - {1}'.format(jugador.nombre,jugador.posicion))
    
    def estadisticas_jugador_segun_indice(self, indice: int):
        '''
        Ingresa el indice de una lista de jugadores
        imprime las estadisticas del jugador
        '''
        patron_indice = '(^[0-9]+$)'
        indice = str(indice)
        if re.match(patron_indice, indice):
            try:
                lista = self.lista_jugadores
                jugador = lista[int(indice)]
                return jugador.estadisticas
            except:
                print('error')
        else:
            print('Debe ingresar un indice valido')

    def guardar_estadisticas_en_csv(self, indice: int):
        '''
        Ingresa el indice de un jugador
        guarda las estadisticas en un archivo CSV
        '''
        texto = ''

        nombre = f'{self.__lista_de_jugadores[indice].nombre}'
        posicion = f'{self.__lista_de_jugadores[indice].posicion}'
        texto += f'{nombre},{posicion}'

        estadisticas = self.estadisticas_jugador_segun_indice(indice)
        estadistica_lista = estadisticas.lista_estadisticas()
        for estadistica in estadistica_lista:
            texto += f',{estadistica}'
        texto += '\n'

        nombre_archivo = 'estadisticas.csv'

        try:
            with open(nombre_archivo, 'r'):
                existe_archivo = True
        except FileNotFoundError:
            existe_archivo = False

        if existe_archivo:
            with open(nombre_archivo, 'a') as file:
                file.write(texto)
        else:
            texto_nuevo = 'Jugador,Posicion,Temporadas,Puntos totales,Promedio puntos por partido,Rebotes totales,Promedio rebotes por partido,Asistencias totales,Promedio asistencias por partido,Robos totales,Bloqueos totales,Porcentaje tiros de campo,Porcentaje tiros libres,Porcentaje tiros triples\n'
            texto_nuevo += texto
            print(texto)
            with open(nombre_archivo, 'w') as file:
                file.write(texto_nuevo)

    def dict_jugadores_robos_mas_bloqueos(self):
        dict_jugadores = {}
        for jugador in self.lista_jugadores:
            dict_jugadores[jugador.nombre] = jugador.estadisticas.suma_robos_bloqueos()
        return dict_jugadores


