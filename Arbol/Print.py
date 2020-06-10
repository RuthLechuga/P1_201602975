from .Instruccion import Instruccion

class Print(Instruccion) :

    def __init__(self,  cad) :
        self.cad = cad
    
    def ejecutar(self,ts,mensajes) :
        print(self.cad)
    
    def getAST(self) :
        print('ast')
    
    def getRepGramatical(self) :
        print('gramatical')
