import random
import os
import time

fifo_path1 = '/tmp/myfifo1'
fifo_path2 = '/tmp/myfifo2'

def generiere_messwerte():
    if not os.path.exists(fifo_path1):
        os.mkfifo(fifo_path1)
        
    
    while True:
        # Erzeugung der Zufallszahlen (Messwerte)
        messwert = random.randint(1, 1000) 

        # Messwerte in die Pipe schreiben
        with open(fifo_path1, 'w') as fifo:
                fifo.write(f"{messwert}\n")
                
        
        with open(fifo_path2, 'w') as fifo:
                fifo.write(f"{messwert}\n")
        
        print(f"Messwerte wurden in die benannte Pipe geschrieben.")
        
        time.sleep(1)  # Pause zwischen den Messungen

if __name__ == '__main__':
    generiere_messwerte()
