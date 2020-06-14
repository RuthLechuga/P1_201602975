from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Read(Instruccion) :

    def __init__(self, identificador, linea, columna) :
        self.identificador = identificador
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        print("read")
        
    def getAST_Ascendente(self) :
        print('ast')
    
    def getAST_Descendente(self) :
        print('ast')
    
    def getRepGramatical(self) :
        print('gramatical')
