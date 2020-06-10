class TablaDeSimbolos() :

    def __init__(self, etiquetas= {}, simbolos = {}) :
        self.simbolos = simbolos
        self.etiquetas = etiquetas

    def addSimbolo(self, simbolo):
        self.simbolos[simbolo.identificador] = simbolo
    
    def getSimbolo(self, identificador):
        if not identificador in self.simbolos:
            return None

        return self.simbolos[identificador]
    
    def addEtiqueta(self, etiqueta):
        if not etiqueta.identificador in self.etiquetas:
            self.etiquetas[etiqueta.identificador] = etiqueta
            return True
                 
        return False
    
    def getEtiqueta(self, identificador):
        if not identificador in self.etiquetas:
            return None

        return self.etiquetas[identificador]
    

    