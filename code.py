class Coda:
    def __init__(self):
        self.lista = []
        
    def is_empty(self):
        if(len(self.lista)==0):
            return True
        else:
            return False
        
    def enqueue(self,x):
        self.lista.append(x)
            
    def dequeue(self):
        if(self.is_empty()):
            print("Lista vuota impossibile rimuovere")
            return None
        else:
            return self.lista.pop(0)
        
    def stampa(self):
        print(self.lista)

def main():
    coda = Coda()
    coda.dequeue()
    coda.enqueue(10)
    coda.enqueue(5)
    coda.stampa()
    print(f"elemento rimosso: {coda.dequeue()}")
    print(f"elemento rimosso: {coda.dequeue()}")
    print(f"elemento rimosso: {coda.dequeue()}")
    coda.enqueue(39)
    coda.stampa()
    

if __name__ == "__main__":
    main()