from .Instruccion import Instruccion
from .Mensaje import *

class Unset(Instruccion) :

    def __init__(self, temporal, linea, columna) :
        self.temporal = temporal
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        band = ts.deleteSimbolo(self.temporal)

        if not band:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede eliminar la temporal porque no existe.',self.linea,self.columna))
            
    def getAST_Ascendente(self) :
        print('ast')
    
    def getAST_Descendente(self) :
        print('ast')
    
    def getRepGramatical(self) :
        print('gramatical')
