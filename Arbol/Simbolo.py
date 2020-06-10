from enum import Enum

class TIPO_DATO(Enum) :
    ENTERO = 1
    DECIMAL = 2
    CADENA = 3
    CARACTER = 4

class Simbolo() :
    def __init__(self, identificador, tipo, dimension, valor, linea, columna, ambito) :
        self.identificador = identificador
        self.tipo = tipo
        self.dimension = dimension
        self.valor = valor
        self.linea = linea
        self.columna = columna
        self.ambito = ambito
