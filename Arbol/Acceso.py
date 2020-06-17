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
                else:
                    return None

                if diccionario is None:
                    return None
                    
            return diccionario       

    def getAST_Ascendente(self) :
        arbol = '\"id_'+str(self)+'\"' + '[label=\"identificador\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"id_'+str(self)+'\"\n'

        arbol += '\"accesos_'+str(self)+'\"' + '[label=\"accesos\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"accesos_'+str(self)+'\"\n'

        for acceso in self.accesos:
            arbol += '\"'+str(acceso)+'\"' + '[label=\"acceso\"] ;\n'
            arbol += '\"accesos_'+str(self)+'\" -> \"'+str(acceso)+"\"\n"
            arbol += acceso.getAST_Ascendente()

        return arbol
    
    def getAST_Descendente(self) :
        print('ast')
    
