class Node():
    def __init__(self, valore):
        self.valore = valore
        self.sinistro = None
        self.destro = None
        
    def inserisci(self, valore):
        if self.valore is not None:    
            if valore < self.valore:
                if self.sinistro is None:
                    self.sinistro = Node(valore)
                else:
                    self.sinistro.inserisci(valore)
            elif valore > self.valore:
                if self.destro is None:
                    self.destro = Node(valore)
                else:
                    self.destro.inserisci(valore)
        else:
            self.valore = valore
        
    
    def printTree(self):
        if self.valore is not None:
            if self.sinistro is not None:
                self.sinistro.printTree()
            print(self.valore)
            if self.destro is not None:
                self.destro.printTree()
            
    def find(self, valore):
        if self.valore is not None:
            if valore == self.valore:
                return True
            elif valore < self.valore and self.sinistro is not None:
                return self.sinistro.find(valore)
            elif valore > self.valore and self.destro is not None:
                return self.destro.find(valore)
        return False
    
    def contaNodi(self, n_nodi):
        if self.valore is not None:
            if self.sinistro is not None:
                self.sinistro.contaNodi(n_nodi)
            n_nodi+=1
            if self.destro is not None:
                self.destro.contaNodi(n_nodi)
        return n_nodi
    
    def calcolaAltezza(self):
        if self is None:
            return 0
        else:
            altezza_sinistro = 0
            altezza_destro = 0
            if self.sinistro is not None:
                altezza_sinistro = self.sinistro.calcolaAltezza()
            if self.destro is not None:
                altezza_destro = self.destro.calcolaAltezza()
            return max(altezza_sinistro, altezza_destro) + 1

    def bilanciato(self):
        #sapere n nodi e altezza
        n_nodi = self.contaNodi(0)
        altezza = self.calcolaAltezza()

            
        
def caricamentoLista(lista, n):
    centro = len(lista) // 2
    n.inserisci(lista[centro])
    if centro!=0:
        listaSx = lista[0:centro]
        listaDx = lista[centro+1:]
        if len(listaSx)>0:
            caricamentoLista(listaSx, n)
        if len(listaDx)>0:
            caricamentoLista(listaDx, n)
    else:
        return None    
        
def main():
    n = Node(5)
    n.inserisci(2)
    n.inserisci(10)
    n.inserisci(1)
    n.inserisci(7)
    n.printTree()
    print(n.find(7))
    lista_nodi = [5,6,2,20,28,16]
    lista_nodi.sort()
    n_2 = Node(None)
    caricamentoLista(lista_nodi,n_2)
    n_2.printTree()
    
    
if __name__ == '__main__':
    main()
