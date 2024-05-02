import threading

class ContoBancario:
    def __init__(self, saldo=0, numero_conto=""):
        self.saldo = saldo
        self.numero_conto = numero_conto
        self.lock = threading.Lock()

    def deposito(self, importo):
        with self.lock:
            self.saldo += importo
            print(f"Deposito di {importo} effettuato. Nuovo saldo: {self.saldo}")

    def prelievo(self, importo):
        with self.lock:
            if self.saldo >= importo:
                self.saldo -= importo
                print(f"Prelievo di {importo} effettuato. Nuovo saldo: {self.saldo}")
            else:
                print("Fondi insufficienti.")

class ContoCorrente(ContoBancario):
    def __init__(self, saldo=0, numero_conto=""):
        super().__init__(saldo, numero_conto)

class ContoRisparmio(ContoBancario):
    def __init__(self, saldo=0, numero_conto=""):
        super().__init__(saldo, numero_conto)

def simulazione(cliente, conto, operazioni):
    for operazione in operazioni:
        if operazione[0] == 'D':
            conto.deposito(operazione[1])
        elif operazione[0] == 'P':
            conto.prelievo(operazione[1])

conto_corrente = ContoCorrente(saldo=1000, numero_conto="CC123")
conto_risparmio = ContoRisparmio(saldo=2000, numero_conto="CR456")

operazioni_cliente1 = [('D', 500), ('P', 300)]
operazioni_cliente2 = [('D', 1000), ('P', 700)]

thread_cliente1 = threading.Thread(target=simulazione, args=("Cliente1", conto_corrente, operazioni_cliente1))
thread_cliente2 = threading.Thread(target=simulazione, args=("Cliente2", conto_risparmio, operazioni_cliente2))

thread_cliente1.start()
thread_cliente2.start()

thread_cliente1.join()
thread_cliente2.join()
