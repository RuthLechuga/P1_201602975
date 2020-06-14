from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class AsignacionArray(Instruccion) :

    def __init__(self, identificador, accesos, expresion, linea, columna) :
        self.identificador = identificador
        self.accesos = accesos
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        temporal = ts.getSimbolo(self.identificador)
        valor = self.expresion.ejecutar(ts,mensajes)
            
        if valor is None:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La expresion para la asignacion a: '+self.identificador+' es inválida.',self.linea,self.columna))
            return

        if temporal is None:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'El identificador '+self.identificador+' no ha sido declarado.',self.linea,self.columna))
            return
        
        if temporal.tipo == TIPO_DATO.ARREGLO:
            diccionario = temporal.valor;
            dimension = len(self.accesos)
            for i in range(len(self.accesos)-1):
                exp_acceso = self.accesos[i].ejecutar(ts,mensajes)

                if exp_acceso is None:
                    mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La expresión en el acceso del arreglo es inválda.',self.linea,self.columna))
                    return
                
                diccionario[exp_acceso] = diccionario.get(exp_acceso,{})
                diccionario = diccionario[exp_acceso]
            
            exp_acceso = self.accesos[len(self.accesos)-1].ejecutar(ts,mensajes)
            if exp_acceso is None:
                    mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La expresión en el acceso del arreglo es inválda.',self.linea,self.columna))
                    return
                
            diccionario[exp_acceso] = valor
            ts.addSimbolo(Simbolo(temporal.identificador,temporal.tipo,dimension,temporal.valor,temporal.linea,temporal.columna,temporal.ambito))
    
        if temporal.tipo == TIPO_DATO.CADENA:
            exp_acceso = self.accesos[0].ejecutar(ts,mensajes)
            if exp_acceso < len(temporal.valor):
                t = ""
                for c in range(len(temporal.valor)):
                    if exp_acceso == c:
                        t += valor
                    else:
                        t += temporal.valor[c]
                temporal.valor = t
            else:
                for i in range(len(temporal.valor),exp_acceso):
                    temporal.valor+= " "
                temporal.valor += valor
            ts.addSimbolo(Simbolo(temporal.identificador,temporal.tipo,temporal.dimension,temporal.valor,temporal.linea,temporal.columna,temporal.ambito))
    
    def getAST_Ascendente(self) :
        print('ast')
    
    def getAST_Descendente(self) :
        print('ast')
    
    def getRepGramatical(self) :
        print('gramatical')
