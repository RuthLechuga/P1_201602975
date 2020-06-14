from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Read(Instruccion) :

    def __init__(self, identificador, linea, columna) :
        self.identificador = identificador
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        print("read")
        
    def getAST_Ascendente(self) :
        arbol = '\"'+str(self)+'\"' + '[label=\"asig_inst\"] ;\n'
        
        arbol += '\"id_'+str(self)+'\"' + '[label=\"identificador\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"id_'+str(self)+'\"\n'

        arbol += '\"as_'+str(self)+'\"' + '[label=\"=\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"as_'+str(self)+'\"\n'
        
        arbol += '\"read_'+str(self)+'\"' + '[label=\"read\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"read_'+str(self)+'\"\n'

        arbol += '\"PIZQ_'+str(self)+'\"' + '[label=\"(\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"PIZQ_'+str(self)+'\"\n'
        
        arbol += '\"PDER_'+str(self)+'\"' + '[label=\")\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"PDER_'+str(self)+'\"\n'
        
        return arbol
    
    def getAST_Descendente(self) :
        print('ast')