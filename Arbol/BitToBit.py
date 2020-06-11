from .Instruccion import Instruccion
from .Mensaje import *
from enum import Enum

class TIPO_BIT_BIT(Enum) :
    NOT = 1,
    AND = 2,
    OR = 3,
    XOR = 4,
    IZQUIERDA = 5,
    DERECHA = 6

class BitToBit(Instruccion) :

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
            if self.tipo == TIPO_BIT_BIT.NOT:
                if isinstance(izq,int) or isinstance(izq,str):
                    temporal = str(izq)
                    resultado = ''

                    try:
                        for c in temporal:
                            if (not int(c)):
                                resultado += '1'
                            else:
                                resultado += '0'
                        return resultado
                    except:
                        mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede aplicar una operacion bit a bit sobre un dato no entero.',self.linea,self.columna))
                        return None
                else:
                    mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede aplicar una operacion bit a bit sobre un dato no entero.',self.linea,self.columna))
                    return None
            return None
            
        temporal_izq = str(izq)
        temporal_der = str(der)
        longitud = len(temporal_izq)
        resultado = ''

        if not(len(temporal_izq) == len(temporal_der)) and (self.tipo != TIPO_BIT_BIT.IZQUIERDA and self.tipo != TIPO_BIT_BIT.DERECHA):
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'Ambos operandos deben tener la misma longitud para aplicar una operación bit a bit.',self.linea,self.columna))
            return None
        
        if self.tipo == TIPO_BIT_BIT.AND:
            try:
                for i in range(longitud):
                    if int(temporal_izq[i]) and int(temporal_der[i]):
                        resultado += '1'
                    else:
                        resultado += '0'
                return resultado
            except:
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede aplicar una operacion bit a bit sobre un dato no entero.',self.linea,self.columna))
                return None

        if self.tipo == TIPO_BIT_BIT.OR:
            try:
                for i in range(longitud):
                    if int(temporal_izq[i]) or int(temporal_der[i]):
                        resultado += '1'
                    else:
                        resultado += '0'
                return resultado
            except:
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede aplicar una operacion bit a bit sobre un dato no entero.',self.linea,self.columna))
                return None

        if self.tipo == TIPO_BIT_BIT.XOR:
            try:
                for i in range(longitud):
                    if (int(temporal_izq[i]) and not int(temporal_der[i])) or (not int(temporal_izq[i]) and int(temporal_der[i])):
                        resultado += '1'
                    else:
                        resultado += '0'
                return resultado
            except:
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede aplicar una operacion bit a bit sobre un dato no entero.',self.linea,self.columna))
                return None
        
        if self.tipo == TIPO_BIT_BIT.IZQUIERDA:
            try:
                for i in range(int(temporal_der)):
                    resultado += '0'
                return temporal_izq[int(temporal_der):]+resultado
            except:
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede aplicar una operacion bit a bit sobre un dato no entero.',self.linea,self.columna))
                return None
        
        if self.tipo == TIPO_BIT_BIT.DERECHA:
            try:
                for i in range(int(temporal_der)):
                    resultado += '0'
                return resultado+temporal_izq[0:len(temporal_izq)-int(temporal_der)]
            except:
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede aplicar una operacion bit a bit sobre un dato no entero.',self.linea,self.columna))
                return None
        

    def getAST_Ascendente(self) :
        print('ast')
    
    def getAST_Descendente(self) :
        print('ast')
    
    def getRepGramatical(self) :
        print('gramatical')
