#password ha solo lettere minuscole italiane con n caratteri (n=3)

from threading import Thread
import time


password = "ansa"
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "z"]
trovato = False

class MioThread(Thread):
    def __init__(self,lettera):
        super().__init__()
        self.lettera = lettera
        #self.running = True
    def run(self):
        #codice del thread
        global trovato
        for l in alfabeto:
            for l2 in alfabeto:
                for l3 in alfabeto:
                    prova = self.lettera + l + l2 + l3
                    if prova == password:
                        print(f"password indovinata! prova: {prova} password: {password}")
                        trovato = True
                    if trovato:
                        return
        
    def kill(self):
        self.running = False

def main():
    lista_thread = [MioThread(l) for l in alfabeto]
    for t in lista_thread:
        t.start()
    for t in lista_thread:
        t.join()
if __name__ == "__main__":
    main()