from .Instruccion import Instruccion
from .Mensaje import *

class If(Instruccion) :

    def __init__(self, condicion, instruccion, linea, columna) :
        self.condicion = condicion
        self.instruccion = instruccion
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        try:
            res = self.condicion.ejecutar(ts,mensajes)

            if(int(res)==1):
               return self.instruccion.ejecutar(ts,mensajes)
        
        except:   
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No pudo procesarse el If.',self.linea,self.columna))
            return None 

    def getAST_Ascendente(self) :
        arbol = '\"'+str(self)+'\"' + '[label=\"if_inst\"] ;\n'
        
        arbol += '\"if_'+str(self)+'\"' + '[label=\"if\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"if_'+str(self)+'\"\n'
        
        arbol += '\"PIZQ_'+str(self)+'\"' + '[label=\"(\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"PIZQ_'+str(self)+'\"\n'

        arbol += '\"'+str(self.condicion)+'\"' + '[label=\"condicion\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"'+str(self.condicion)+'\"\n'
        arbol += self.condicion.getAST_Ascendente()
        
        arbol += '\"PDER_'+str(self)+'\"' + '[label=\")\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"PDER_'+str(self)+'\"\n'
        
        arbol += '\"ins_'+str(self)+'\"' + '[label=\"instruccion\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"ins_'+str(self)+'\"\n'

        arbol += '\"ins_'+str(self)+'\"'+' -> '+ '\"'+str(self.instruccion)+'\"\n'
        arbol += self.instruccion.getAST_Ascendente()
        
        return arbol
    
    def getAST_Descendente(self) :
        arbol = '\"'+str(self)+'\"' + '[label=\"if_inst\"] ;\n'
        
        arbol += '\"if_'+str(self)+'\"' + '[label=\"if\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"if_'+str(self)+'\"\n'
        
        arbol += '\"PIZQ_'+str(self)+'\"' + '[label=\"(\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"PIZQ_'+str(self)+'\"\n'

        arbol += '\"'+str(self.condicion)+'\"' + '[label=\"condicion\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"'+str(self.condicion)+'\"\n'
        arbol += self.condicion.getAST_Descendente()
        
        arbol += '\"PDER_'+str(self)+'\"' + '[label=\")\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"PDER_'+str(self)+'\"\n'
        
        arbol += '\"ins_'+str(self)+'\"' + '[label=\"instruccion\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"ins_'+str(self)+'\"\n'

        arbol += '\"ins_'+str(self)+'\"'+' -> '+ '\"'+str(self.instruccion)+'\"\n'
        arbol += self.instruccion.getAST_Descendente()
        
        return arbol
    