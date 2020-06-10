import abc 
class Instruccion(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def ejecutar(self,ts,mensajes) :
        pass
    
    @abc.abstractmethod
    def getAST(self) :
        pass
    
    @abc.abstractmethod
    def getRepGramatical(self) :
        pass