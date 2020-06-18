from .Instruccion import Instruccion
from .Mensaje import *
from enum import Enum

class TIPO_LOGICA(Enum) :
    NOT = 1,
    AND = 2,
    OR = 3,
    XOR = 4

class Logica(Instruccion) :

    def __init__(self, izquierda, derecha, tipo, linea, columna) :
        self.izquierda = izquierda
        self.derecha = derecha
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        izq = None if not self.izquierda else self.izquierda.ejecutar(ts,mensajes)
        der = None if not self.derecha else self.derecha.ejecutar(ts,mensajes)

        try:
            if izq is None and der is None:
                return None
        
            if der is None:
                if self.tipo == TIPO_LOGICA.NOT:
                    if izq:
                        return 0
                    return 1
                return None
        
            if self.tipo == TIPO_LOGICA.AND:
                if izq and der:
                    return 1
                return 0
        
            if self.tipo == TIPO_LOGICA.OR:
                if izq or der:
                    return 1
                return 0
        
            if self.tipo == TIPO_LOGICA.XOR:
                if (izq and not der) or (not izq and der):
                    return 1
                return 0
        
        except:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se ha podido realizar la operación lógica.',self.linea,self.columna))
            return None

    def getAST_Ascendente(self) :
        arbol = ""
        if self.derecha is None:
            arbol += '\"not_'+str(self)+'\"' + '[label=\"not\"] ;\n'
            arbol +='\"'+str(self)+'\" -> \"abs_'+str(self)+'\"\n'

            arbol += '\"PIZQ_'+str(self)+'\"' + '[label=\"(\"] ;\n'
            arbol +='\"'+str(self)+'\" -> \"PIZQ_'+str(self)+'\"\n'

            arbol += '\"'+str(self.izquierda)+'\"' + '[label=\"expresion\"] ;\n'
            arbol +='\"'+str(self)+'\" -> \"'+str(self.izquierda)+'\"\n'
            arbol += self.izquierda.getAST_Ascendente()

            arbol += '\"PDER_'+str(self)+'\"' + '[label=\")\"] ;\n'
            arbol +='\"'+str(self)+'\" -> \"PDER_'+str(self)+'\"\n'
                
        else:
            arbol += '\"'+str(self.izquierda)+'\"' + '[label=\"expresion\"] ;\n'
            arbol +='\"'+str(self)+'\" -> \"'+str(self.izquierda)+'\"\n'
            arbol += self.izquierda.getAST_Ascendente()
            
            arbol += '\"sig_'+str(self)+'\"' + '[label=\"'+self.tipo.name+'\"] ;\n'
            arbol +='\"'+str(self)+'\" -> \"sig_'+str(self)+'\"\n'
            
            arbol += '\"'+str(self.derecha)+'\"' + '[label=\"expresion\"] ;\n'
            arbol +='\"'+str(self)+'\" -> \"'+str(self.derecha)+'\"\n'
            arbol += self.derecha.getAST_Ascendente()
        
        return arbol

    def getAST_Descendente(self) :
        arbol = ""
        if self.derecha is None:
            arbol += '\"not_'+str(self)+'\"' + '[label=\"not\"] ;\n'
            arbol +='\"'+str(self)+'\" -> \"abs_'+str(self)+'\"\n'

            arbol += '\"PIZQ_'+str(self)+'\"' + '[label=\"(\"] ;\n'
            arbol +='\"'+str(self)+'\" -> \"PIZQ_'+str(self)+'\"\n'

            arbol += '\"'+str(self.izquierda)+'\"' + '[label=\"expresion\"] ;\n'
            arbol +='\"'+str(self)+'\" -> \"'+str(self.izquierda)+'\"\n'
            arbol += self.izquierda.getAST_Descendente()

            arbol += '\"PDER_'+str(self)+'\"' + '[label=\")\"] ;\n'
            arbol +='\"'+str(self)+'\" -> \"PDER_'+str(self)+'\"\n'
                
        else:
            arbol += '\"'+str(self.izquierda)+'\"' + '[label=\"expresion\"] ;\n'
            arbol +='\"'+str(self)+'\" -> \"'+str(self.izquierda)+'\"\n'
            arbol += self.izquierda.getAST_Descendente()

            arbol += '\"exp_der_'+str(self.izquierda)+'\"' + '[label=\"expresion\'\"] ;\n'
            arbol +='\"'+str(self)+'\" -> \"exp_der_'+str(self.izquierda)+'\"\n'
            
            arbol += '\"sig_'+str(self)+'\"' + '[label=\"'+self.tipo.name+'\"] ;\n'
            arbol += '\"exp_der_'+str(self.izquierda)+'\" -> \"sig_'+str(self)+'\"\n'
            
            arbol += '\"'+str(self.derecha)+'\"' + '[label=\"expresion\"] ;\n'
            arbol += '\"exp_der_'+str(self.izquierda)+'\" -> \"'+str(self.derecha)+'\"\n'
            arbol += self.derecha.getAST_Descendente()
        
        return arbol
