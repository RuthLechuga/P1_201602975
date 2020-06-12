class TablaDeSimbolos() :

    def __init__(self, etiquetas= {}, simbolos = {}, et_actual = 'main') :
        self.simbolos = simbolos
        self.etiquetas = etiquetas
        self.et_actual = et_actual
        self.num_et = 0

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
    
    def addEtiqueta(self, new_etiqueta):
        for etiqueta in self.etiquetas.values():
            if etiqueta.identificador == new_etiqueta.identificador:
                return False
        
        self.etiquetas[len(self.etiquetas)] = new_etiqueta
        return True
    
    def getEtiqueta(self, identificador):
        for id, etiqueta in self.etiquetas.items():
            if etiqueta.identificador == identificador:
                self.num_et = id
                self.et_actual = etiqueta
                return etiqueta

        return None
    
    def getEtiquetas(self):
        return self.etiquetas
    
    def getSiguiente(self):
        self.num_et +=1

        if self.num_et==len(self.etiquetas):
            return None
        
        self.et_actual = self.etiquetas[self.num_et].identificador
        return self.etiquetas[self.num_et]
       
    def getEtActual(self):
        return self.et_actual
    

    