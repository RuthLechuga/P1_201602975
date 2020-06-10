from .Instruccion import Instruccion
from .Mensaje import *

class Print(Instruccion) :

    def __init__(self, temporal, linea, columna) :
        self.temporal = temporal
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        simbolo = ts.getSimbolo(self.temporal)

        if not simbolo:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se ha encontrado el identificador '+self.temporal+'.',self.linea,self.columna))           
            return
        
        mensajes.append(Mensaje(TIPO_MENSAJE.LOG,simbolo.valor,self.linea,self.columna))
        print("",simbolo.valor)
         
    def getAST_Ascendente(self) :
        print('ast')
    
    def getAST_Descendente(self) :
        print('ast')
    
    def getRepGramatical(self) :
        print('gramatical')
