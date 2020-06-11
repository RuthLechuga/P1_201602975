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

        tipo_dato = None
        dimension = 1

        if isinstance(temporal,int):
            tipo_dato = TIPO_DATO.ENTERO
        
        elif isinstance(temporal,float):
            tipo_dato = TIPO_DATO.DECIMAL
        
        elif isinstance(temporal,str) and len(temporal)==1:
            tipo_dato = TIPO_DATO.CARACTER
        
        elif isinstance(temporal,str):
            tipo_dato = TIPO_DATO.CADENA
        
        #validar arreglo, tipos de datos y ambitos
        ts.addSimbolo(Simbolo(self.identificador,tipo_dato,dimension,temporal,self.linea,self.columna,ts.getEtActual()))
    
    def getAST_Ascendente(self) :
        print('ast')
    
    def getAST_Descendente(self) :
        print('ast')
    
    def getRepGramatical(self) :
        print('gramatical')
