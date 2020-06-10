from enum import Enum

class TIPO_ESTRUCTURA(Enum) :
    PROCEDIMIENTO = 1
    FUNCION = 2
    CONTROL = 3

class Etiqueta() :
    def __init__(self, identificador, tipo_estructura, linea, columna, instrucciones = {}):
        self.identificador = identificador
        self.instrucciones = instrucciones
        self.tipo_estructura = tipo_estructura
        self.linea = linea
        self.columna = columna
    
    def updateTipoEstructura(tipo) :
        self.tipo_estructura = tipo