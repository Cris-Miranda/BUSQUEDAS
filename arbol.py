class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = None
        self.padre = None
        self.coste = None
        self.set_hijos(hijos)
        
    def set_hijos(self, hijos): #Establece los nodos hijos para el nodo actual
        self.hijos=hijos
        if self.hijos != None:
            for h in self.hijos:
                h.padre = self
                
    def get_hijos(self):  #Devuelve la lista de hijos del nodo
        return self.hijos
    
    def get_padre(self):  #Devuelve el nodo padre del nodo actual
        return self.padre
    
    def set_padre(self, padre):  #Establece el nodo padre del nodo actual
        self.padre = padre
    
    def set_datos(self, datos):  #Establece el valor a datos del nodo
        self.datos = datos
        
    def get_datos(self): #Devuelve los datos del nodo
        return self.datos  
        
    def set_coste(self, coste):  #Establece el coste asociado al nodo
        self.coste = coste
        
    def get_coste(self): #Devuelve el coste del nodo
        return self.coste
        
    def igual(self, nodo):  #Compara los datos actuales con los anteriores
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False
        
    def en_lista(self, lista_nodos): #Comprueba si el nodo actual esta en la lista de nodos
        en_la_lista=False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista=True
        return en_la_lista
    
    def __str__(self):
        return str(self.get_datos())  #sobre escribe la representacion en forma de cadena