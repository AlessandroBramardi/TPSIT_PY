from threading import Thread
import time
import socket
#messaggio = f"{messaggio}|{ipDest}" portaUDP=43211
#assegno ip e porta al processo
BUFFER_SIZE = 4096 #byte
SERVER_ADDRESS = ("192.168.1.125", 43211)
NICKNAME = "brama"
MY_ADDRESS = ("192.168.1.120",43211)

class MioThread(Thread):
    def __init__(self,s):
        super().__init__()
        self.s = s 
    def run(self):
        #codice del thread
        while True:
            data, sender_address = self.s.recvfrom(BUFFER_SIZE) #serve spazio di memoria in byte, ritorna dati + indirizzo
            stringa = data.decode() #devo castare data perchè arriva in binary
            print(f"Ricevuto {stringa} da {sender_address}")
            #if stringa == "EXIT":
             #   break
    def kill(self):
        self.running = False
            
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(MY_ADDRESS)
    thread=MioThread(s)
    partito = True
    while True:
        string = input("messaggio-> ")
        dest = input("inserire nick destinatario ->")
        #binary_string = string.encode()
        packet = f"{string}|{NICKNAME}|{dest}"
        s.sendto(packet.encode(), SERVER_ADDRESS)
        if partito:
            thread.start()
            partito = False
            
if __name__ == "__main__":
    main()