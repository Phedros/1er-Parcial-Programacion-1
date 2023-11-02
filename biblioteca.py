from Equipo import Equipo
import re
import json
import sqlite3


def cargar_equipo_dreamteam():
    '''
    crea una variable
    se le asigna un objeto Equipo() con un equipo cargado
    '''
    direccion = "dream_team.json"
    mi_equipo = Equipo()
    mi_equipo.cargar_equipo_json(direccion)
    return mi_equipo


def ordenar_ascendente(lista: list):
    '''
    ordena una lista de forma ascendente
    '''
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    menor = [x for x in lista[:] if x < pivot]
    igual = [x for x in lista if x == pivot]
    mayor = [x for x in lista[:] if x > pivot]
    return ordenar_ascendente(menor) + igual + ordenar_ascendente(mayor)


def ordenar_descendente(lista: list):
    '''
    ordena una lista de forma descendente
    '''
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    menor = [x for x in lista[:] if x < pivot]
    igual = [x for x in lista if x == pivot]
    mayor = [x for x in lista[:] if x > pivot]
    return ordenar_descendente(mayor) + igual + ordenar_descendente(menor)

def validar_nombre(nombre:str):
    '''
    ingresa un nombre tipo string y lo valida
    devuelve True si esta validado correctamente
    '''
    patron_validacion_nombre = '(^[A-Za-z ]+$)'
    if re.match(patron_validacion_nombre, nombre):
        return True
    else:
        print(f'{nombre} es un nombre incorrecto')

def imprime_lista_jugadores():
    '''
    imprime una lista de jugadores del equipo Dream Team
    '''
    mi_equipo = cargar_equipo_dreamteam()
    texto = ''
    contador = 1
    for jugador in mi_equipo.lista_jugadores:
        texto += f'{str(contador)} - {jugador.nombre}\n'
        contador += 1
    print(texto)

def traer_jugador(nombre:str):
    '''
    ingresa un nombre de un jugador en formato String
    devuelve un objeto de tipo Jugador
    '''
    try:
        if validar_nombre(nombre):
            equipo_dreamteam = cargar_equipo_dreamteam()
            for jugador in equipo_dreamteam.lista_jugadores:
                if nombre.lower() == jugador.nombre.lower():
                    indice = equipo_dreamteam.lista_jugadores.index(jugador)
            return equipo_dreamteam.lista_jugadores[indice]
    except:
        print('error, nombre ingresado incorrecto')

'''
***********************************************************************************
1) Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
Nombre Jugador - Posición. Ejemplo:
Michael Jordan - Escolta
***********************************************************************************
'''
def mostrar_lista_jugadores_dreamteam():
    '''
    muestra lista de jugadores del equipo Dream Team
    '''
    equipo_dreamteam = cargar_equipo_dreamteam()
    equipo_dreamteam.mostrar_lista_jugadores()

'''
***********************************************************************************
2) Permitir al usuario seleccionar un jugador por su índice (validar con regex) y mostrar
sus estadísticas completas, incluyendo temporadas jugadas, puntos totales,
promedio de puntos por partido, rebotes totales, promedio de rebotes por partido,
asistencias totales, promedio de asistencias por partido, robos totales, bloqueos
totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros
triples.
***********************************************************************************
'''
def estadisticas_de_jugador_dreamteam():
    '''
    Consulta el indice de un jugador para que el usuario ingrese un indice
    imprime las estadisticas del jugador
    '''
    imprime_lista_jugadores()
    indice = input('Ingrese indice del jugador: ')
    indice = int(indice)
    indice -= 1
    equipo_dreamteam = cargar_equipo_dreamteam()
    estadisticas = equipo_dreamteam.estadisticas_jugador_segun_indice(indice)
    lista_tipo_estadistica = estadisticas.lista_tipo_estadisticas
    jugador = equipo_dreamteam.lista_jugadores[indice]

    contador = 0
    print(f'Estadisticas de {jugador.nombre}: \n')
    for estadiscica in estadisticas.lista_estadisticas():
        print(f'\t{lista_tipo_estadistica[contador]}: {estadiscica}')
        contador +=1

    respuesta = input('Desea guardar archivo CVS? (s/n): ')
    if respuesta == 's' or respuesta == 'S':
        equipo_dreamteam.guardar_estadisticas_en_csv(indice)



'''
***********************************************************************************
3) Después de mostrar las estadísticas de un jugador seleccionado por el usuario,
permite al usuario guardar las estadísticas de ese jugador en un archivo CSV. El
archivo CSV debe contener los siguientes campos: nombre, posición, temporadas,
puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes
por partido, asistencias totales, promedio de asistencias por partido, robos totales,
bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y
porcentaje de tiros triples.
***********************************************************************************
'''
# Agregado al metodo -> estadisticas_de_jugador_dreamteam()
'''
***********************************************************************************
4) Permitir al usuario buscar un jugador por su nombre (validar con regex) y mostrar
sus logros, como campeonatos de la NBA, participaciones en el All-Star y
pertenencia al Salón de la Fama del Baloncesto, etc.
***********************************************************************************
'''

def validar_nombre_mostrar_logros():
    '''
    solicita al usuario que ingrese un nombre
    lo valida y muestra los logros del jugador
    '''
    try:
        nombre = input('Ingrese nombre del jugador: ')
        validar_nombre(nombre)

        jugador = traer_jugador(nombre)
        logros = jugador.logros
        print(f'Logros de {nombre}:\n')
        for logro in logros:
            print('\t' + logro)
    except:
        print('error')

'''
***********************************************************************************
5) Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream
Team, ordenado por nombre de manera ascendente
***********************************************************************************
'''

def lista_promedio_puntos_por_partido_dreamteam():
    '''
    imprime una lista del promedio de los puntos por partido de los jugadores de Dream Team
    '''
    lista_promedios_puntos = []
    mi_equipo = cargar_equipo_dreamteam()
    for jugador in mi_equipo.lista_jugadores:
        lista_promedios_puntos.append(jugador.estadisticas.promedio_puntos_por_partido)
    
    lista_promedios_ordenada = ordenar_ascendente(lista_promedios_puntos)
    lista_jugadores_ordenada = []
    for valor in lista_promedios_ordenada:
        for jugador in mi_equipo.lista_jugadores:
            if valor == jugador.estadisticas.promedio_puntos_por_partido:
                lista_jugadores_ordenada.append(jugador.nombre)
    contador = 0
    print('\nEl promedio de puntos por partido de todo el equipo del DreamTeam, ordenado por nombre de manera ascendente es la siguiente: \n')
    for _ in range(len(lista_jugadores_ordenada)):
        print(f'\t{lista_jugadores_ordenada[contador]}: {lista_promedios_ordenada[contador]}')
        contador += 1

'''
***********************************************************************************
6) Permitir al usuario ingresar el nombre de un jugador (validar con regex) y mostrar si
ese jugador es miembro del Salón de la Fama del Baloncesto.
***********************************************************************************
'''

def validar_jugador_salon_de_la_fama():
    '''
    solicita al usuario ingresar nombre
    lo valida
    imprime si esta en el salon de la fama
    '''

    nombre = input('Ingrese un nombre: ')

    mi_equipo = cargar_equipo_dreamteam()
    if validar_nombre(nombre):
        for jugador in mi_equipo.lista_jugadores:
            try:
                if jugador.logros.index('Miembro del Salon de la Fama del Baloncesto'):
                    if jugador.nombre.lower() == nombre.lower():
                        print(f'{nombre} pertenece al Salon de la Fama')
                        break
            except:
                print(f'{nombre} no pertenece al salon de la fama')
                break

'''
***********************************************************************************
7) Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
***********************************************************************************
'''

def calcular_jugador_mayor_rebotes_totales():
    '''
    imprime el jugador con mayor rebotes totales
    '''
    mayor_jugador = ''
    mayor_valor = ''
    bandera = True
    mi_equipo = cargar_equipo_dreamteam()
    lista_jugadores = mi_equipo.lista_jugadores
    for jugador in lista_jugadores:
        if bandera:
            mayor_jugador = jugador.nombre
            mayor_valor = jugador.estadisticas.rebotes_totales
            bandera = False
        else:
            if jugador.estadisticas.rebotes_totales > mayor_valor:
                mayor_jugador = jugador.nombre
                mayor_valor = jugador.estadisticas.rebotes_totales 
    print(f'El jugador con mayor cantidad de rebotes es: {mayor_jugador}')      

'''
***********************************************************************************
8) Según su último número del DNI, usar el campo que corresponda para
realizar los siguientes puntos
    A) Ordenar el listado de manera descendente(el mayor arriba) y mostrar el
    listado.
    B) Permitir guardar este listado ordenado en un archivo CSV con su
    apellido.csv
    C) Permitir guardar este listado ordenado en un archivo JSON y permitir al
    usuario ingresar el nombre del archivo a guardar (validar con regex)
        5- "asistencias_totales"
***********************************************************************************
'''


def ordenar_listado_asistencias_totales_descendente():
    '''
    Ordenar el listado de asistenciastotales manera descendente
    Permitir guardar este listado ordenado en un archivo CSV con nombre 'serra.csv'
    Permitir guardar este listado ordenado en un archivo JSON
    '''
    lista_asistencias_totales = []
    mi_equipo = cargar_equipo_dreamteam()
    for jugador in mi_equipo.lista_jugadores:
        lista_asistencias_totales.append(jugador.estadisticas.asistencias_totales)
    
    lista_asistencias_ordenada = ordenar_descendente(lista_asistencias_totales)
    lista_jugadores_ordenada = []
    for valor in lista_asistencias_ordenada:
        for jugador in mi_equipo.lista_jugadores:
            if valor == jugador.estadisticas.asistencias_totales:
                lista_jugadores_ordenada.append(jugador.nombre)
    contador = 0
    mensaje = ''
    bandera = True
    print('\nEl listado de asistencias totales, ordenado por nombre de manera descendente es la siguiente: \n')
    for _ in range(len(lista_jugadores_ordenada)):
        print(f'\t{lista_jugadores_ordenada[contador]}: {lista_asistencias_ordenada[contador]}')
        if bandera:
            mensaje += f'{lista_jugadores_ordenada[contador]}'
            bandera = False
        else:
            mensaje += f',{lista_jugadores_ordenada[contador]}'
        contador += 1
    mensaje += '\n'
    bandera = True
    contador2 = 0
    for _ in range(len(lista_jugadores_ordenada)):
        if bandera:
            mensaje += f'{lista_asistencias_ordenada[contador2]}'
            bandera = False
        else:
            mensaje += f',{lista_asistencias_ordenada[contador2]}'
        contador2 += 1
    
    respuesta = input('\nDesea guardar archivo CVS? (s/n): ')
    if respuesta == 's' or respuesta == 'S':
        apellido = 'serra.csv'
        with open(apellido, 'w') as file:
            file.write(mensaje)
    
    respuesta2 = input('\nDesea guardar archivo json? (s/n): ')
    if respuesta2 == 's' or respuesta == 'S':
        data = {}
        data['asistencias_totales'] = []
        contador_json = 0
        for _ in range(len(lista_jugadores_ordenada)):
            jugador_a_ingresar = lista_jugadores_ordenada[contador_json]
            asistencias_a_ingresar = lista_asistencias_ordenada[contador_json]
            dict_a_ingresar = {'jugador' : f'{jugador_a_ingresar}', 'asistencias' : f'{asistencias_a_ingresar}'}
            data['asistencias_totales'].append(dict_a_ingresar)
            contador_json += 1
        respuesta3 = input('Ingrese nombre de archivo a guardar')
        with open(f'{respuesta3}.json', 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


def imprimir_menu():
    print(
    """
    1  - Mostrar la lista de todos los jugadores del Dream Team
    2  - Mostrar sus estadísticas completas de un jugador
    3  - Mostrar logros de jugador
    4  - Calcular y mostrar el promedio de puntos por partido de forma ascendente
    5  - Consultar si un jugador es miembro del Salón de la Fama del Baloncesto.
    6  - Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
    7  - Ordenar asistencias totales de manera descendente
    8  - Ver porcentajes de robos y bloqueos totales de manera ascendente
    9  - Crear tabla de posiciones en base de datos
    10 - Salir
    """)
    respuesta = input('Ingrese una opcion: ')
    respuesta = int(respuesta)
    return respuesta


'''
***********************************************************************************
9)(para todos) ordenar los datos por el jugador que sumando los robos totales más
los bloqueos totales ("robos_totales" + "bloqueos_totales").
    A) ordenar los jugadores por el valor sumado.
    B)listar todos los jugadores ordenados y mostrar el porcentaje de este valor
    sumado tomando como 100% el valor máximo
    por ej: si el máximo valor es 500 , ese es el 100% y el que suma 450 tiene un
    90% .
    C) crear un filtro que permita ingresar un valor y que solo muestre esa
    cantidad de jugadores ordenados por la suma de los dos campos.
***********************************************************************************
'''

def calcular_porcentaje(numero:float, valor_max:float):
    '''
    Ingresa un numero (float) y un valor maximo (float)
    calcula el porcentaje del numero en base al valor maximo
    '''
    resultado = numero * 100 / valor_max
    mensaje = f'{resultado:.2f}%'
    return mensaje

def ordenar_jugadores_segun_robos_y_bloqueos():
    '''
    Ordena los jugadores del equipo Dream Team en base a la suma de los robos y los bloqueos
    Calcula el porcentaje de ese total en base al mayor valor

    '''
    # A) ordenar los jugadores por el valor sumado.
    lista_robos_y_bloqueos_valores = []
    lista_robos_y_bloqueos_valores_ordenada = []
    lista_robos_y_bloqueos_jugadores_ordenado = []
    dict_robos_y_bloqueos_jugadores_ordenado = {}

    mi_equipo = cargar_equipo_dreamteam()
    dict_jugadores = mi_equipo.dict_jugadores_robos_mas_bloqueos()
    for v in dict_jugadores.values():
        lista_robos_y_bloqueos_valores.append(v)
    
    lista_robos_y_bloqueos_valores_ordenada = ordenar_ascendente(lista_robos_y_bloqueos_valores)

    for valor_ordenado in lista_robos_y_bloqueos_valores_ordenada:
        for k,v in dict_jugadores.items():
            if v == valor_ordenado:
                lista_robos_y_bloqueos_jugadores_ordenado.append(k)
                dict_robos_y_bloqueos_jugadores_ordenado[k] = v

    # listar todos los jugadores ordenados y mostrar el porcentaje de este valor
    # sumado tomando como 100% el valor máximo
    # por ej: si el máximo valor es 500 , ese es el 100% y el que suma 450 tiene un
    # 90% .
    mensaje = '\nLista de porcentajes de bloqueos y robos totales:\n'

    dict_robos_y_bloqueos_porcentajes_ordenado = {}
    valor_max = lista_robos_y_bloqueos_valores_ordenada[0]
    for valor in lista_robos_y_bloqueos_valores_ordenada:
        if valor > valor_max:
            valor_max = valor
    
    for jugador,valor in dict_robos_y_bloqueos_jugadores_ordenado.items():
        dict_robos_y_bloqueos_porcentajes_ordenado[jugador] = calcular_porcentaje(valor, valor_max)
    
    lista_mensajes = []
    for jugador,valor in dict_robos_y_bloqueos_porcentajes_ordenado.items():
        mensaje_jugador = f'\t{jugador}: {valor}\n'
        lista_mensajes.append(mensaje_jugador)
    
    cantidad_jugadores = input(f'Que cantidad de jugadores desea visualizar? 1-{len(lista_mensajes)}: ')
    cantidad_jugadores = int(cantidad_jugadores)
    while cantidad_jugadores > len(lista_mensajes) or cantidad_jugadores < 0:
        cantidad_jugadores = input(f'Dato incorrecto. Debe ingresar un numero entre 1 y {len(lista_mensajes)}: ')
    
    contador = 0
    for _ in range(cantidad_jugadores):
        mensaje += lista_mensajes[contador]
        contador += 1

    print(mensaje)
    
    
    return dict_robos_y_bloqueos_jugadores_ordenado
    

def crear_tabla_posiciones_cargar_lista():
    mi_equipo = cargar_equipo_dreamteam()
    lista_jugadores = mi_equipo.lista_jugadores
    lista_posiciones = []
    for jugador in lista_jugadores:
            posicion = jugador.posicion
            lista_posiciones.append(posicion)
    with sqlite3.connect('bd_btf.bd') as conexion:
        try:    
            sentencia = ''' create  table posicion_jugadores 
                        (
                            id integer primary key autoincrement,
                            posiciones text
                        )
                    '''
            conexion.execute(sentencia)
            print("Se creo la tabla posiciones")                       
        except sqlite3.OperationalError:
            print("La tabla personajes ya existe")
    
    lista_valores_unicos = []
    for posicion in lista_posiciones:
        if posicion not in lista_valores_unicos:
            lista_valores_unicos.append(posicion)
    print(lista_valores_unicos)

    with sqlite3.connect("bd_btf.bd") as conexion:
        for posicion in lista_valores_unicos:
            try:
                conexion.execute("insert into posicion_jugadores(posiciones) values (?)", (f"{posicion}",)) 
            except:
                print("Error")
        conexion.commit()
