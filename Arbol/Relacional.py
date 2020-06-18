from .Instruccion import Instruccion
from .Mensaje import *
from enum import Enum

class TIPO_RELACIONAL(Enum) :
    IGUAL_QUE = 1,
    DISTINTO_QUE = 2,
    MAYOR_IGUAL_QUE = 3,
    MENOR_IGUAL_QUE = 4,
    MENOR_QUE = 5,
    MAYOR_QUE = 6

class Relacional(Instruccion) :

    def __init__(self, izquierda, derecha, tipo, linea, columna) :
        self.izquierda = izquierda
        self.derecha = derecha
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        izq = None if not self.izquierda else self.izquierda.ejecutar(ts,mensajes)
        der = None if not self.derecha else self.derecha.ejecutar(ts,mensajes)

        if izq is None and der is None:
            return None
        
        if self.tipo == TIPO_RELACIONAL.IGUAL_QUE:
            if izq == der:
                return 1
            return 0
        
        if self.tipo == TIPO_RELACIONAL.DISTINTO_QUE:
            if izq != der:
                return 1
            return 0
        
        if self.tipo == TIPO_RELACIONAL.MAYOR_IGUAL_QUE:
            if izq >= der:
                return 1
            return 0
        
        if self.tipo == TIPO_RELACIONAL.MENOR_IGUAL_QUE:
            if izq <= der:
                return 1
            return 0
        
        if self.tipo == TIPO_RELACIONAL.MAYOR_QUE:
            if izq > der:
                return 1
            return 0
        
        if self.tipo == TIPO_RELACIONAL.MENOR_QUE:
            if izq < der:
                return 1
            return 0
         
    def getAST_Ascendente(self) :
        arbol = '\"'+str(self.izquierda)+'\"' + '[label=\"expresion\"] ;\n'
        arbol +='\"'+str(self)+'\" -> \"'+str(self.izquierda)+'\"\n'
        arbol += self.izquierda.getAST_Ascendente()
        
        arbol += '\"sig_'+str(self)+'\"' + '[label=\"'+self.tipo.name+'\"] ;\n'
        arbol +='\"'+str(self)+'\" -> \"sig_'+str(self)+'\"\n'
            
        arbol += '\"'+str(self.derecha)+'\"' + '[label=\"expresion\"] ;\n'
        arbol +='\"'+str(self)+'\" -> \"'+str(self.derecha)+'\"\n'
        arbol += self.derecha.getAST_Ascendente()

        return arbol

    def getAST_Descendente(self) :
        arbol = '\"'+str(self.izquierda)+'\"' + '[label=\"expresion\"] ;\n'
        arbol +='\"'+str(self)+'\" -> \"'+str(self.izquierda)+'\"\n'
        arbol += self.izquierda.getAST_Ascendente()
        
        arbol += '\"exp_der_'+str(self.izquierda)+'\"' + '[label=\"expresion\'\"] ;\n'
        arbol +='\"'+str(self)+'\" -> \"exp_der_'+str(self.izquierda)+'\"\n'
            
        arbol += '\"sig_'+str(self)+'\"' + '[label=\"'+self.tipo.name+'\"] ;\n'
        arbol += '\"exp_der_'+str(self.izquierda)+'\" -> \"sig_'+str(self)+'\"\n'
            
        arbol += '\"'+str(self.derecha)+'\"' + '[label=\"expresion\"] ;\n'
        arbol += '\"exp_der_'+str(self.izquierda)+'\" -> \"'+str(self.derecha)+'\"\n'
        arbol += self.derecha.getAST_Ascendente()

        return arbol
