from .Instruccion import Instruccion
from .Mensaje import *

class Unset(Instruccion) :

    def __init__(self, temporal, linea, columna) :
        self.temporal = temporal
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        return True

    def getAST_Ascendente(self) :
        print('ast')
    
    def getAST_Descendente(self) :
        print('ast')
    
    def getRepGramatical(self) :
        print('gramatical')
