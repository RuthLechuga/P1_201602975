from .Instruccion import Instruccion
from .Mensaje import *

class Print(Instruccion) :

    def __init__(self, expresion, linea, columna) :
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        valor = self.expresion.ejecutar(ts,mensajes)

        if valor is None:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se ha podido procesar la información del print.',self.linea,self.columna))           
            return
        
        if isinstance(valor,dict):
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede imprimir un arreglo.',self.linea,self.columna))           
            return

        mensajes.append(Mensaje(TIPO_MENSAJE.LOG,valor,self.linea,self.columna))
        
    def getAST_Ascendente(self) :
        arbol = '\"'+str(self)+'\"' + '[label=\"print_inst\"] ;\n'
        
        arbol += '\"print_'+str(self)+'\"' + '[label=\"print\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"print_'+str(self)+'\"\n'
        
        arbol += '\"PIZQ_'+str(self)+'\"' + '[label=\"(\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"PIZQ_'+str(self)+'\"\n'
        
        arbol += '\"'+str(self.expresion)+'\"' + '[label=\"expresion\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"'+str(self.expresion)+'\"\n'

        arbol += '\"PDER_'+str(self)+'\"' + '[label=\")\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"PDER_'+str(self)+'\"\n'

        arbol += self.expresion.getAST_Ascendente()    
        return arbol
    
    def getAST_Descendente(self) :
        print('ast')