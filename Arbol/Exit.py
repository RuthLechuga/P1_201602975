from .Instruccion import Instruccion
from .Mensaje import *

class Exit(Instruccion) :

    def __init__(self, linea, columna) :
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        return None
        
    def getAST_Ascendente(self) :
        print('ast')
    
    def getAST_Descendente(self) :
        print('ast')
    
    def getRepGramatical(self) :
        print('gramatical')
