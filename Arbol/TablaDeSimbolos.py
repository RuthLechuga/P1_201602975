class TablaDeSimbolos() :

    def __init__(self, etiquetas= {}, simbolos = {}, et_actual = 'main') :
        self.simbolos = simbolos
        self.etiquetas = etiquetas
        self.et_actual = et_actual

    def addSimbolo(self, simbolo):
        self.simbolos[simbolo.identificador] = simbolo
    
    def getSimbolo(self, identificador):
        if not identificador in self.simbolos:
            return None

        return self.simbolos[identificador]
    
    def deleteSimbolo(self, identificador):
        if not identificador in self.simbolos:
            return False

        del self.simbolos[identificador]
        return True
    
    def addEtiqueta(self, etiqueta):
        if not etiqueta.identificador in self.etiquetas:
            self.etiquetas[etiqueta.identificador] = etiqueta
            return True
                 
        return False
    
    def getEtiqueta(self, identificador):
        if not identificador in self.etiquetas:
            return None

        return self.etiquetas[identificador]
    
    def getEtiquetas(self):
        return self.etiquetas
    
    def setEtActual(self, etiqueta):
        self.et_actual = etiqueta
    
    def getEtActual(self):
        return self.et_actual
    

    