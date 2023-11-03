import json

class Estadisticas:
    def __init__(self, estadistica_dict):
        self.__temporadas_jugadas = estadistica_dict['temporadas']
        self.__puntos_totales = estadistica_dict['puntos_totales']
        self.__promedio_puntos_por_partido = estadistica_dict['promedio_puntos_por_partido']
        self.__rebotes_totales = estadistica_dict['rebotes_totales']
        self.__promedio_rebotes_por_partido = estadistica_dict['promedio_rebotes_por_partido']
        self.__asistencias_totales = estadistica_dict['asistencias_totales']
        self.__promedio_asistencias_por_partido = estadistica_dict['promedio_asistencias_por_partido']
        self.__robos_totales = estadistica_dict['robos_totales']
        self.__bloqueos_totales = estadistica_dict['bloqueos_totales']
        self.__porcentaje_tiros_de_campo = estadistica_dict['porcentaje_tiros_de_campo']
        self.__porcentaje_tiros_libres = estadistica_dict['porcentaje_tiros_libres']
        self.__porcentaje_tiros_triples = estadistica_dict['porcentaje_tiros_triples']



    #Getters y setters temporadas_jugadas

    @property
    def temporadas_jugadas(self):
        return self.__temporadas_jugadas
    
    @temporadas_jugadas.setter
    def set_temporada_jugada(self, temporada):
        self.__temporadas_jugadas = temporada

    #Getters y setters puntos_totales

    @property
    def puntos_totales(self):
        return self.__puntos_totales
    
    @puntos_totales.setter
    def set_puntos_totales(self, puntos):
        self.__puntos_totales = puntos


    #Getters y setters promedio_puntos_por_partido

    @property
    def promedio_puntos_por_partido(self):
        return self.__promedio_puntos_por_partido
    
    @promedio_puntos_por_partido.setter
    def set_promedio_puntos_por_partido(self, puntos):
        self.__promedio_puntos_por_partido = puntos

    #Getters y setters rebotes_totales

    @property
    def rebotes_totales(self):
        return self.__rebotes_totales
    
    @rebotes_totales.setter
    def set_rebotes_totales(self, rebotes):
        self.__rebotes_totales = rebotes

    #Getters y setters promedio_rebotes_por_partido

    @property
    def promedio_rebotes_por_partido(self):
        return self.__promedio_rebotes_por_partido
    
    @promedio_rebotes_por_partido.setter
    def set_promedio_rebotes_por_partido(self, rebotes):
        self.__promedio_rebotes_por_partido = rebotes

    #Getters y setters asistencias_totales

    @property
    def asistencias_totales(self):
        return self.__asistencias_totales

    @asistencias_totales.setter
    def set_asistencias_totales(self, asistencias):
        self.__asistencias_totales = asistencias

    #Getters y setters promedio_asistencias_por_partido

    @property
    def promedio_asistencias_por_partido(self):
        return self.__promedio_asistencias_por_partido
    
    @promedio_asistencias_por_partido.setter
    def set_promedio_asistencias_por_partido(self, asistencias):
        self.__promedio_asistencias_por_partido = asistencias

    #Getters y setters robos_totales

    @property
    def robos_totales(self):
        return self.__robos_totales
    
    @robos_totales.setter
    def set_robos_totales(self, robos):
        self.__robos_totales = robos

    #Getters y setters bloqueos_totales

    @property
    def bloqueos_totales(self):
        return self.__bloqueos_totales
    
    @bloqueos_totales.setter
    def set_bloqueos_totales(self, bloqueos):
        self.__bloqueos_totales = bloqueos

    #Getters y setters porcentaje_tiros_de_campo

    @property
    def porcentaje_tiros_de_campo(self):
        return self.__porcentaje_tiros_de_campo
    
    @porcentaje_tiros_de_campo.setter
    def set_porcentaje_tiros_de_campo(self, porcentaje):
        self.__porcentaje_tiros_de_campo = porcentaje

    #Getters y setters porcentaje_tiros_libres

    @property
    def porcentaje_tiros_libres(self):
        return self.__porcentaje_tiros_libres
    
    @porcentaje_tiros_libres.setter
    def set_porcentaje_tiros_libres(self, porcentaje):
        self.__porcentaje_tiros_libres = porcentaje

    #Getters y setters porcentaje_tiros_triples

    @property
    def porcentaje_tiros_triples(self):
        return self.__porcentaje_tiros_triples
    
    @porcentaje_tiros_triples.setter
    def set_porcentaje_tiros_triples(self, porcentaje):
        self.__porcentaje_tiros_triples = porcentaje

    def lista_estadisticas(self):
        estadisticas = [
            self.__temporadas_jugadas,
            self.__puntos_totales,
            self.__promedio_puntos_por_partido,
            self.__rebotes_totales,
            self.__promedio_rebotes_por_partido,
            self.__asistencias_totales,
            self.__promedio_asistencias_por_partido,
            self.__robos_totales,
            self.__bloqueos_totales,
            self.__porcentaje_tiros_de_campo,
            self.__porcentaje_tiros_libres,
            self.__porcentaje_tiros_triples
        ]
        return estadisticas
    
    
    lista_tipo_estadisticas = ['temporadas','puntos_totales','promedio_puntos_por_partido','rebotes_totales','promedio_rebotes_por_partido','asistencias_totales','promedio_asistencias_por_partido','robos_totales','bloqueos_totales','porcentaje_tiros_de_campo','porcentaje_tiros_libres','porcentaje_tiros_triples']

    def suma_robos_bloqueos(self):
        '''
        Suma los robos y los bloqueos
        '''
        suma = self.robos_totales + self.bloqueos_totales
        return suma