from .Instruccion import Instruccion
from .Mensaje import *

class If(Instruccion) :

    def __init__(self, condicion, instruccion, linea, columna) :
        self.condicion = condicion
        self.instruccion = instruccion
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        try:
            res = self.condicion.ejecutar(ts,mensajes)

            if(int(res)==1):
               return self.instruccion.ejecutar(ts,mensajes)
        
        except:   
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No pudo procesarse el If.',self.linea,self.columna))
            return None 

    def getAST_Ascendente(self) :
        print('ast')
    
    def getAST_Descendente(self) :
        print('ast')
    
    def getRepGramatical(self) :
        print('gramatical')
