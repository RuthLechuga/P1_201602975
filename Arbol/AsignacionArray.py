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
            try:
                diccionario = temporal.valor;
                dimension = len(self.accesos)
                
                for i in range(len(self.accesos)-1):
                    exp_acceso = self.accesos[i].ejecutar(ts,mensajes)

                    if exp_acceso is None:
                        mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La expresión en el acceso del arreglo es inválda.',self.linea,self.columna))
                        return
                    
                    diccionario[exp_acceso] = diccionario.get(exp_acceso,{})
                    dic_anterior = diccionario
                    acceso_anterior = exp_acceso
                    diccionario = diccionario[exp_acceso]
                
                exp_acceso = self.accesos[len(self.accesos)-1].ejecutar(ts,mensajes)
                if exp_acceso is None:
                        mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La expresión en el acceso del arreglo es inválda.',self.linea,self.columna))
                        return
                
                if isinstance(diccionario,str):
                    if exp_acceso < len(diccionario):
                        t = ""
                        for c in range(len(diccionario)):
                            if exp_acceso == c:
                                t += valor
                            else:
                                t += diccionario[c]
                        diccionario = t
                    else:
                        for i in range(len(diccionario),exp_acceso):
                            diccionario+= " "
                        diccionario += valor
                    
                    dic_anterior[acceso_anterior] = diccionario
                
                else:
                    diccionario[exp_acceso] = valor
                
                ts.addSimbolo(Simbolo(temporal.identificador,temporal.tipo,dimension,temporal.valor,temporal.linea,temporal.columna,temporal.ambito))
            except:
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se ha podido realizar la asignación en la posición específicada del arreglo.',self.linea,self.columna))
                return     
        
        if temporal.tipo == TIPO_DATO.CADENA:
            try:
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
            except:
                mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se ha podido realizar la asignación en la posición específicada del arreglo.',self.linea,self.columna))
                return

    def getAST_Ascendente(self) :
        arbol = '\"'+str(self)+'\"' + '[label=\"asig_array_inst\"] ;\n'
        
        arbol += '\"id_'+str(self)+'\"' + '[label=\"identificador\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"id_'+str(self)+'\"\n'

        arbol += '\"accesos_'+str(self)+'\"' + '[label=\"accesos\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"accesos_'+str(self)+'\"\n'

        for acceso in self.accesos:
            arbol += '\"'+str(acceso)+'\"' + '[label=\"acceso\"] ;\n'
            arbol += '\"accesos_'+str(self)+'\" -> \"'+str(acceso)+"\"\n"
            arbol += acceso.getAST_Ascendente()
        
        arbol += '\"asig_'+str(self)+'\"' + '[label=\"=\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"asig_'+str(self)+'\"\n'

        arbol += '\"'+str(self.expresion)+'\"' + '[label=\"expresion\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"'+str(self.expresion)+'\"\n'
        arbol += self.expresion.getAST_Ascendente()

        return arbol

    def getAST_Descendente(self) :
        print('ast')
