from .Instruccion import Instruccion
from .Mensaje import *
from .Simbolo import *

class Convertir(Instruccion) :

    def __init__(self, identificador, expresion, tipo, linea, columna) :
        self.identificador = identificador
        self.expresion = expresion
        self.tipo = tipo;
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self,ts,mensajes) :
        temporal = self.expresion.ejecutar(ts,mensajes)

        if temporal is None:
            mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'La expresión para el identificador '+self.identificador+' es inválida.',self.linea,self.columna))
            return
        
        if self.tipo == 'float':
            if isinstance(temporal,int):
                temporal = float(temporal)
            
            elif isinstance(temporal,str):
                temporal = ord(temporal[0:1])

            #validar si es arreglo
        
        elif self.tipo == 'int':
            if isinstance(temporal,float):
                temporal = int(temporal)
            
            elif isinstance(temporal,str):
                temporal = float(ord(temporal[0:1]))
            
            #validar si es arreglo
        
        elif self.tipo == 'char':
            if isinstance(temporal,float):
                temporal = int(temporal)

            elif isinstance(temporal,int):
                if temporal >= 0 and temporal<=255:
                    temporal = chr(temporal)
                
                elif temporal > 255:
                    temporal = temporal % 256
                    temporal = chr(temporal)
                
                else:
                    mensajes.append(Mensaje(TIPO_MENSAJE.SEMANTICO,'No se puede realizar la conversión de un número negativo a char.',self.linea,self.columna))
                    return None
            
            elif isinstance(temporal,str):
                temporal = temporal[0:1]
            
            #validar arreglos

        #validar arreglo, tipos de datos y ambitos
        ts.addSimbolo(Simbolo(self.identificador,TIPO_DATO.ENTERO,0,temporal,self.linea,self.columna,ts.getEtActual()))
    
    def getAST_Ascendente(self) :
        arbol = self.getEncabezado()
        arbol += self.expresion.getAST_Ascendente()
        return arbol
    
    def getAST_Descendente(self) :
        arbol = self.getEncabezado()
        arbol += self.expresion.getAST_Descendente()
        return arbol
    
    def getEncabezado(self):
        arbol = '\"'+str(self)+'\"' + '[label=\"asig_inst\"] ;\n'
        
        arbol += '\"id_'+str(self)+'\"' + '[label=\"identificador\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"id_'+str(self)+'\"\n'

        arbol += '\"as_'+str(self)+'\"' + '[label=\"=\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"as_'+str(self)+'\"\n'

        arbol += '\"PIZQ_'+str(self)+'\"' + '[label=\"(\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"PIZQ_'+str(self)+'\"\n'
        
        arbol += '\"tipo_'+str(self)+'\"' + '[label=\"'+self.tipo+'\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"tipo_'+str(self)+'\"\n'

        arbol += '\"PDER_'+str(self)+'\"' + '[label=\")\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"PDER_'+str(self)+'\"\n'

        arbol += '\"'+str(self.expresion)+'\"' + '[label=\"expresion\"] ;\n'
        arbol += '\"'+str(self)+'\"'+' -> '+ '\"'+str(self.expresion)+'\"\n'
        return arbol