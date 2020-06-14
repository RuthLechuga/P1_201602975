from .Instruccion import Instruccion
from .Mensaje import *

class Exit(Instruccion) :

    def __init__(self, linea, columna) :
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        return None
        
    def getAST_Ascendente(self) :
        arbol = '\"'+str(self)+'\"' + '[label=\"exit_inst\"] ;\n'
        
        arbol += '\"exit_'+str(self)+'\"' + '[label=\"exit\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"exit_'+str(self)+'\"\n'

        return arbol
    
    def getAST_Descendente(self) :
        print('ast')