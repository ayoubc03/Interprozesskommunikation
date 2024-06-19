import os
import time

fifo_path3 = '/tmp/myfifo3'

def ausgabe_ergebnisse():
    if not os.path.exists(fifo_path3):
        os.mkfifo(fifo_path3)
    
    while True:
        # Lesen der Ergebnisse aus der benannten Pipe
        with open(fifo_path3, 'r') as fifo:
            ergebnisse = fifo.read().strip()
        
        print(f"Ergebnisse:\n{ergebnisse} \n -----------------")
        
        # Pause
        time.sleep(1) 

if __name__ == '__main__':
        ausgabe_ergebnisse()
       