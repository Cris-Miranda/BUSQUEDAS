class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = None
        self.padre = None
        self.coste = None
        self.set_hijos(hijos)
        
    def set_hijos(self, hijos):
        self.hijos=hijos
        if self.hijos != None:
            for h in self.hijos:
                h.padre = self
                
