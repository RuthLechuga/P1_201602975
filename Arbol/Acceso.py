from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Acceso(Instruccion) :

    def __init__(self, identificador, accesos) :
        self.identificador = identificador
        self.accesos = accesos
    
    def ejecutar(self,ts,mensajes) :
        temporal = ts.getSimbolo(self.identificador)

        if temporal is None:
            return None
        
        if temporal.tipo == TIPO_DATO.ARREGLO or temporal.tipo == TIPO_DATO.CADENA:
            diccionario = temporal.valor
            for acceso in self.accesos:
                indice = acceso.ejecutar(ts,mensajes)

                if indice is None:
                    return None
                
                if isinstance(diccionario,dict):
                    diccionario = diccionario.get(indice, None)          
                elif isinstance(diccionario,str):
                    diccionario = diccionario[indice]

                if diccionario is None:
                    return None
            
            return diccionario       

    def getAST_Ascendente(self) :
        print('ast')
    
    def getAST_Descendente(self) :
        print('ast')
    
    def getRepGramatical(self) :
        print('gramatical')
