from .Instruccion import Instruccion
from .Mensaje import *
from enum import Enum

class TIPO_UNARIO(Enum) :
    CADENA = 1,
    ENTERO = 2,
    DECIMAL = 3,
    IDENTIFICADOR = 4,
    NEGATIVO = 5

class Unaria(Instruccion) :

    def __init__(self, valor, tipo, linea, columna) :
        self.valor = valor
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :

        if self.tipo == TIPO_UNARIO.CADENA:
            return self.valor;
        
        if self.tipo == TIPO_UNARIO.ENTERO:
            return int(self.valor)
        
        if self.tipo == TIPO_UNARIO.DECIMAL:
            return float(self.valor)
        
        if self.tipo == TIPO_UNARIO.IDENTIFICADOR:
            simbolo = ts.getSimbolo(self.valor)

            if not simbolo:
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'El identificador '+self.valor+' no se ha encontrado.',self.linea,self.columna))
                return None
            
            return simbolo.valor;
        
        if self.tipo == TIPO_UNARIO.NEGATIVO:
            temporal = self.valor.ejecutar(ts,mensajes)

            if not temporal:
                return None
            
            if isinstance(temporal,str):
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede aplicar el operador - a una cadena.',self.linea,self.columna))
                return None
            
            return (-1)*temporal

    def getAST_Ascendente(self) :
        if self.tipo == TIPO_UNARIO.CADENA:
            arbol = '\"exp_'+str(self)+'\"' + '[label=\"CADENA\"] ;\n'
            arbol += '\"'+str(self)+'\" -> '+'\"exp_'+str(self)+'\"'
        
        elif self.tipo == TIPO_UNARIO.ENTERO:
            arbol = '\"exp_'+str(self)+'\"' + '[label=\"ENTERO\"] ;\n'
            arbol += '\"'+str(self)+'\" -> '+'\"exp_'+str(self)+'\"'
        
        elif self.tipo == TIPO_UNARIO.DECIMAL:
            arbol = '\"exp_'+str(self)+'\"' + '[label=\"DECIMAL\"] ;\n'
            arbol += '\"'+str(self)+'\" -> '+'\"exp_'+str(self)+'\"'
        
        elif self.tipo == TIPO_UNARIO.IDENTIFICADOR:
            arbol = '\"exp_'+str(self)+'\"' + '[label=\"IDENTIFICADOR\"] ;\n'
            arbol += '\"'+str(self)+'\" -> '+'\"exp_'+str(self)+'\"'
        
        elif self.tipo == TIPO_UNARIO.NEGATIVO:
            arbol = '\"exp_neg_'+str(self)+'\"' + '[label=\"-\"] ;\n'
            arbol += '\"'+str(self)+'\" -> '+'\"exp_neg_'+str(self)+'\"\n'
            arbol += '\"'+str(self.valor)+'\"' + '[label=\"expresion\"] ;\n'
            arbol += '\"'+str(self)+'\" -> '+'\"'+str(self.valor)+'\"\n'
            arbol += self.valor.getAST_Ascendente()
        
        return arbol
    
    def getAST_Descendente(self) :
        print('ast')