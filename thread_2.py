from threading import Thread
import time
class MioThread(Thread):
    def __init__(self,nome):
        super().__init__()
        self.nome = nome
        self.running = True
    def run(self):
        #codice del thread
        while self.running:
            print(f"Sono il thread {self.nome}")
            time.sleep(1)
    def kill(self):
        self.running = False
            
def main():
    lista_nomi = ["Brama :)","Sciolla :(","Bergia :("]
    lista_thread = [MioThread(nome) for nome in lista_nomi]
    '''
    thread1 = MioThread("Sciolla nel 1 turno") #una instanza di thread
    thread2 = MioThread("E non lo spostiamo")
    thread1.start()
    thread2.start()
    '''
    for t in lista_thread:
        t.start()
    for _ in range(4):
        print("Sono il main thread")
        time.sleep(1)
    for t in lista_thread:
        t.kill()
        t.join() #necessario
    print("Sono il main thread e ho chiuso gli altri")

if __name__ == "__main__":
    main()