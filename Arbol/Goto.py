from .Instruccion import Instruccion
from .Mensaje import *

class Goto(Instruccion) :

    def __init__(self, etiqueta, linea, columna) :
        self.etiqueta = etiqueta
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        etiqueta = ts.getEtiqueta(self.etiqueta)
        ts.setEtActual(etiqueta.identificador)

        for instruccion in etiqueta.instrucciones:
            res = instruccion.ejecutar(ts,mensajes)
            if res:
                break
    
        return True

    def getAST_Ascendente(self) :
        print('ast')
    
    def getAST_Descendente(self) :
        print('ast')
    
    def getRepGramatical(self) :
        print('gramatical')
