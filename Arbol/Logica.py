from .Instruccion import Instruccion
from .Mensaje import *
from enum import Enum

class TIPO_LOGICA(Enum) :
    NOT = 1,
    AND = 2,
    OR = 3,
    XOR = 4

class Logica(Instruccion) :

    def __init__(self, izquierda, derecha, tipo, linea, columna) :
        self.izquierda = izquierda
        self.derecha = derecha
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        izq = None if not self.izquierda else self.izquierda.ejecutar(ts,mensajes)
        der = None if not self.derecha else self.derecha.ejecutar(ts,mensajes)

        try:
            if izq is None and der is None:
                return None
        
            if der is None:
                if self.tipo == TIPO_LOGICA.NOT:
                    if izq:
                        return 0
                    return 1
                return None
        
            if self.tipo == TIPO_LOGICA.AND:
                if izq and der:
                    return 1
                return 0
        
            if self.tipo == TIPO_LOGICA.OR:
                if izq or der:
                    return 1
                return 0
        
            if self.tipo == TIPO_LOGICA.XOR:
                if (izq and not der) or (not izq and der):
                    return 1
                return 0
        
        except:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se ha podido realizar la operación lógica.',self.linea,self.columna))
            return None

    def getAST_Ascendente(self) :
        print('ast')
    
    def getAST_Descendente(self) :
        print('ast')
    
    def getRepGramatical(self) :
        print('gramatical')
