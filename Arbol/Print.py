from .Instruccion import Instruccion
from .Mensaje import *

class Print(Instruccion) :

    def __init__(self, expresion, linea, columna) :
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        valor = self.expresion.ejecutar(ts,mensajes)

        if valor is None:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se ha podido procesar la información del print.'+self.temporal+'.',self.linea,self.columna))           
            return
        
        mensajes.append(Mensaje(TIPO_MENSAJE.LOG,valor,self.linea,self.columna))
        
    def getAST_Ascendente(self) :
        print('ast')
    
    def getAST_Descendente(self) :
        print('ast')
    
    def getRepGramatical(self) :
        print('gramatical')
