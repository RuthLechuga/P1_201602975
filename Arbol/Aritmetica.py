from .Instruccion import Instruccion
from .Mensaje import *
from enum import Enum

class TIPO_ARITMETICA(Enum) :
    SUMA = 1,
    RESTA = 2,
    MULTIPLICACION = 3,
    DIVISION = 4,
    RESIDUO = 5,
    ABSOLUTO = 6

class Aritmetica(Instruccion) :

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
        
        if der is None:
            if self.tipo == TIPO_ARITMETICA.ABSOLUTO:
                if isinstance(izq,int) or isinstance(izq,float):
                    return abs(izq)
                
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede obtener el valor absoluto de una cadena.',self.linea,self.columna))
                return None
            return None
        
        if self.tipo == TIPO_ARITMETICA.SUMA:
            if (isinstance(izq,int) or isinstance(izq,float)) and (isinstance(der,int) or isinstance(der,float)):
                return izq+der
            
            if isinstance(izq,str) and isinstance(der,str):
                return izq+der
            
            if isinstance(izq,str) and (isinstance(der,int) or isinstance(der,float)):
                return izq+str(der)
            
            if isinstance(der,str) and (isinstance(izq,int) or isinstance(izq,float)):
                return der+str(izq)
        
        if self.tipo == TIPO_ARITMETICA.RESTA:
            if (isinstance(izq,int) or isinstance(izq,float)) and (isinstance(der,int) or isinstance(der,float)):
                return izq-der
            
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede restar una cadena.',self.linea,self.columna))
            return None
        
        if self.tipo == TIPO_ARITMETICA.MULTIPLICACION:
            if (isinstance(izq,int) or isinstance(izq,float)) and (isinstance(der,int) or isinstance(der,float)):
                return izq*der
            
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede multiplicar una cadena.',self.linea,self.columna))
            return None
        
        if self.tipo == TIPO_ARITMETICA.DIVISION:
            if isinstance(izq,int) and isinstance(der,int):
                return izq//der

            if (isinstance(izq,int) or isinstance(izq,float)) and (isinstance(der,int) or isinstance(der,float)):
                return izq/der
            
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede dividir una cadena.',self.linea,self.columna))
            return None
        
        if self.tipo == TIPO_ARITMETICA.RESIDUO:
            if (isinstance(izq,int) or isinstance(izq,float)) and (isinstance(der,int) or isinstance(der,float)):
                return izq%der
            
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede obtener el residuo de una cadena.',self.linea,self.columna))
            return None

    def getAST_Ascendente(self) :
        arbol = ""
        if self.derecha is None:
            arbol += '\"abs_'+str(self)+'\"' + '[label=\"abs\"] ;\n'
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
        print('ast')