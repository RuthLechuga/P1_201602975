from .Instruccion import Instruccion
from .Mensaje import Mensaje
from enum import Enum

class TIPO_RELACIONAL(Enum) :
    IGUAL_QUE = 1,
    DISTINTO_QUE = 2,
    MAYOR_IGUAL_QUE = 3,
    MENOR_IGUAL_QUE = 4,
    MENOR_QUE = 5,
    MAYOR_QUE = 6

class Relacional(Instruccion) :

    def __init__(self, izquierda, derecha, tipo, linea, columna) :
        self.izquierda = izquierda
        self.derecha = derecha
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        izq = None if not self.izquierda else self.izquierda.ejecutar(ts,mensajes)
        der = None if not self.derecha else self.derecha.ejecutar(ts,mensajes)

        if izq is None and der is None:
            return None
        
        if self.tipo == TIPO_RELACIONAL.IGUAL_QUE:
            if izq == der:
                return 1
            return 0
        
        if self.tipo == TIPO_RELACIONAL.DISTINTO_QUE:
            if izq != der:
                return 1
            return 0
        
        if self.tipo == TIPO_RELACIONAL.MAYOR_IGUAL_QUE:
            if izq >= der:
                return 1
            return 0
        
        if self.tipo == TIPO_RELACIONAL.MENOR_IGUAL_QUE:
            if izq <= der:
                return 1
            return 0
        
        if self.tipo == TIPO_RELACIONAL.MAYOR_QUE:
            if izq > der:
                return 1
            return 0
        
        if self.tipo == TIPO_RELACIONAL.MENOR_QUE:
            if izq < der:
                return 1
            return 0
         
    def getAST_Ascendente(self) :
        print('ast')
    
    def getAST_Descendente(self) :
        print('ast')
    
    def getRepGramatical(self) :
        print('gramatical')