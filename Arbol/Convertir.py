from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Convertir(Instruccion) :

    def __init__(self, identificador, expresion, tipo, linea, columna) :
        self.identificador = identificador
        self.expresion = expresion
        self.tipo = tipo;
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        temporal = self.expresion.ejecutar(ts,mensajes)

        if temporal is None:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La expresión para el identificador '+self.identificador+' es inválida.',self.linea,self.columna))
            return
        
        if self.tipo == 'float':
            if isinstance(temporal,int):
                temporal = float(temporal)
            
            elif isinstance(temporal,str):
                temporal = ord(temporal[0:1])

            #validar si es arreglo
        
        elif self.tipo == 'int':
            if isinstance(temporal,float):
                temporal = int(temporal)
            
            elif isinstance(temporal,str):
                temporal = float(ord(temporal[0:1]))
            
            #validar si es arreglo
        
        elif self.tipo == 'char':
            if isinstance(temporal,float):
                temporal = int(temporal)

            elif isinstance(temporal,int):
                if temporal >= 0 and temporal<=255:
                    temporal = chr(temporal)
                
                elif temporal > 255:
                    temporal = temporal % 256
                    temporal = chr(temporal)
                
                else:
                    mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede realizar la conversión de un número negativo a char.',self.linea,self.columna))
                    return None
            
            elif isinstance(temporal,str):
                temporal = temporal[0:1]
            
            #validar arreglos

        #validar arreglo, tipos de datos y ambitos
        ts.addSimbolo(Simbolo(self.identificador,TIPO_DATO.ENTERO,0,temporal,self.linea,self.columna,ts.getEtActual()))
    
    def getAST_Ascendente(self) :
        print('ast')
    
    def getAST_Descendente(self) :
        print('ast')
    
    def getRepGramatical(self) :
        print('gramatical')
