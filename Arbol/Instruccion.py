import abc 
class Instruccion(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def ejecutar(self,ts,mensajes) :
        pass
    
    @abc.abstractmethod
    def getAST_Ascendente(self) :
        pass
    
    @abc.abstractmethod
    def getAST_Descendente(self) :
        pass