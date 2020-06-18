from .Instruccion import Instruccion
from .Mensaje import *

class Goto(Instruccion) :

    def __init__(self, etiqueta, linea, columna) :
        self.etiqueta = etiqueta
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        return ts.getEtiqueta(self.etiqueta)

    def getAST_Ascendente(self) :
        arbol = '\"'+str(self)+'\"' + '[label=\"goto_inst\"] ;\n'
        
        arbol += '\"goto_'+str(self)+'\"' + '[label=\"goto\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"goto_'+str(self)+'\"\n'

        arbol += '\"et_'+str(self)+'\"' + '[label=\"etiqueta\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"et_'+str(self)+'\"\n'
        
        return arbol
    
    def getAST_Descendente(self) :
        return self.getAST_Ascendente()