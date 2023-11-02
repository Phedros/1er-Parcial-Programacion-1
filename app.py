from biblioteca import *

def main_app():
    '''
    Ejecuta todo el programa.
    '''
    while True:
        
        opcion_elegida = imprimir_menu()
        match opcion_elegida:
            case 1:
                mostrar_lista_jugadores_dreamteam()
            case 2:
                estadisticas_de_jugador_dreamteam()
            case 3:
                validar_nombre_mostrar_logros()
            case 4:
                lista_promedio_puntos_por_partido_dreamteam()
            case 5:
                validar_jugador_salon_de_la_fama()
            case 6:
                calcular_jugador_mayor_rebotes_totales()
            case 7:
                ordenar_listado_asistencias_totales_descendente()
            case 8:
                ordenar_jugadores_segun_robos_y_bloqueos()
            case 9:
                crear_tabla_posiciones_cargar_lista()
            case 10:
                print('Gracias por participar')
                break
            case _:
                print('Opcion incorrecta. Elija entre 1 y 9')