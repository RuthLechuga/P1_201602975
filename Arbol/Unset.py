from .Instruccion import Instruccion
from .Mensaje import *

class Unset(Instruccion) :

    def __init__(self, temporal, linea, columna) :
        self.temporal = temporal
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        band = ts.deleteSimbolo(self.temporal)

        if not band:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede eliminar la temporal porque no existe.',self.linea,self.columna))
            
    def getAST_Ascendente(self) :
        arbol = '\"'+str(self)+'\"' + '[label=\"unset_inst\"] ;\n'
        
        arbol += '\"unset_'+str(self)+'\"' + '[label=\"unset\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"unset_'+str(self)+'\"\n'

        arbol += '\"PIZQ_'+str(self)+'\"' + '[label=\"(\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"PIZQ_'+str(self)+'\"\n'

        arbol += '\"id_'+str(self)+'\"' + '[label=\"identificador\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"id_'+str(self)+'\"\n'
        
        arbol += '\"PDER_'+str(self)+'\"' + '[label=\")\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"PDER_'+str(self)+'\"\n'
        
        return arbol
    
    def getAST_Descendente(self) :
        print('ast')