from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

import easygui

class Read(Instruccion) :

    def __init__(self, identificador, linea, columna) :
        self.identificador = identificador
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        valor = easygui.enterbox("Valor para: "+self.identificador)
        valor_tipado = ''
        tipo = TIPO_DATO.CADENA
        
        try:
            valor_tipado = int(valor)
            tipo = TIPO_DATO.ENTERO
        except:
            try:
                valor_tipado = float(valor)
                tipo = TIPO_DATO.DECIMAL
            except:
                valor_tipado = str(valor)
                tipo = TIPO_DATO.CADENA

        if not valor is None:
            ts.addSimbolo(Simbolo(self.identificador,tipo,1,valor_tipado,self.linea,self.columna,ts.getEtActual()))
        else:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La expresión para el identificador '+self.identificador+' es inválida.',self.linea,self.columna))
                
    def getAST_Ascendente(self) :
        arbol = '\"'+str(self)+'\"' + '[label=\"asig_inst\"] ;\n'
        
        arbol += '\"id_'+str(self)+'\"' + '[label=\"identificador\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"id_'+str(self)+'\"\n'

        arbol += '\"as_'+str(self)+'\"' + '[label=\"=\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"as_'+str(self)+'\"\n'
        
        arbol += '\"read_'+str(self)+'\"' + '[label=\"read\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"read_'+str(self)+'\"\n'

        arbol += '\"PIZQ_'+str(self)+'\"' + '[label=\"(\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"PIZQ_'+str(self)+'\"\n'
        
        arbol += '\"PDER_'+str(self)+'\"' + '[label=\")\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"PDER_'+str(self)+'\"\n'
        
        return arbol
    
    def getAST_Descendente(self) :
        return self.getAST_Ascendente()