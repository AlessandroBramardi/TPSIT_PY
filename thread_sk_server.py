from threading import Thread
import time
import socket
MY_ADDRESS = ("127.0.0.1", 9000) #assegno ip e porta al processo
BUFFER_SIZE = 4096 #byte

class MioThread(Thread):
    def __init__(self,s):
        super().__init__()
        self.s = s 
        self.sender_address = None
    def run(self):
        #codice del thread
        while True:
            data, s_address = self.s.recvfrom(BUFFER_SIZE)
            self.sender_address = s_address
            stringa = data.decode()
            print(f"Ricevuto {stringa} da {s_address}")
            if stringa == "EXIT":
                break
    def kill(self):
        self.running = False
            
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(MY_ADDRESS)
    thread=MioThread(s)
    thread.start()
    while True:
        if thread.sender_address != None:
            string = input("-> ")
            binary_string = string.encode()
            s.sendto(binary_string, thread.sender_address)
if __name__ == "__main__":
    main()