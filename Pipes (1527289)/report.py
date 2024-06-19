import os
import time

fifo_path3 = '/tmp/myfifo3'

def ausgabe_ergebnisse(fifo_path):
    if not os.path.exists(fifo_path):
        os.mkfifo(fifo_path)
    
    while True:
        # Lesen der Ergebnisse aus der benannten Pipe
        with open(fifo_path, 'r') as fifo:
            ergebnisse = fifo.read().strip()
        
        print(f"Ergebnisse:\n{ergebnisse} \n -----------------")
        
        # Pause
        time.sleep(1) 

if __name__ == '__main__':
    while True:
        ausgabe_ergebnisse(fifo_path3)
       # Pause
        time.sleep(1)  
