from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Asignacion(Instruccion) :

    def __init__(self, identificador, expresion, linea, columna) :
        self.identificador = identificador
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        temporal = self.expresion.ejecutar(ts,mensajes)

        if temporal is None:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La expresión para el identificador '+self.identificador+' es inválida.',self.linea,self.columna))
            return
        
        #validar arreglo, tipos de datos y ambitos
        ts.addSimbolo(Simbolo(self.identificador,TIPO_DATO.ENTERO,0,temporal,self.linea,self.columna,ts.getEtActual()))
    
    def getAST_Ascendente(self) :
        print('ast')
    
    def getAST_Descendente(self) :
        print('ast')
    
    def getRepGramatical(self) :
        print('gramatical')
