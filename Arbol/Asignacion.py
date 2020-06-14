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

        if not isinstance(self.expresion,dict):
            temporal = self.expresion.ejecutar(ts,mensajes)

            if temporal is None:
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La expresión para el identificador '+self.identificador+' es inválida.',self.linea,self.columna))
                return
        else:
            temporal = {}

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
        
        elif isinstance(temporal,dict):
            tipo_dato = TIPO_DATO.ARREGLO
        
        #validar arreglo, tipos de datos y ambitos
        ts.addSimbolo(Simbolo(self.identificador,tipo_dato,dimension,temporal,self.linea,self.columna,ts.getEtActual()))
    
    def getAST_Ascendente(self) :
        arbol = '\"'+str(self)+'\"' + '[label=\"asig_inst\"] ;\n'
        
        arbol += '\"id_'+str(self)+'\"' + '[label=\"identificador\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"id_'+str(self)+'\"\n'
        
        arbol += '\"asig_'+str(self)+'\"' + '[label=\"=\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"asig_'+str(self)+'\"\n'

        arbol += '\"'+str(self.expresion)+'\"' + '[label=\"expresion\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"'+str(self.expresion)+'\"\n'
        arbol += self.expresion.getAST_Ascendente()

        return arbol
        
    def getAST_Descendente(self) :
        print('ast')