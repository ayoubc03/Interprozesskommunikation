import random
import os
import time

fifo_path1 = '/tmp/myfifo1'
fifo_path2 = '/tmp/myfifo2'

def generiere_messwerte():
    if not os.path.exists(fifo_path1):
        os.mkfifo(fifo_path1)
    if not os.path.exists(fifo_path2):
        os.mkfifo(fifo_path2)
    
    while True:
        messwert = random.randint(1, 1000)
        
        # Schreibe Messwert in fifo_path1
        with open(fifo_path1, 'w') as fifo1:
            fifo1.write(f"{messwert}\n")
        
        # Schreibe Messwert in fifo_path2 für Stat-Prozess
        with open(fifo_path2, 'w') as fifo:
            fifo.write(f"{messwert}\n")
        
        time.sleep(2)

if __name__ == '__main__':
    generiere_messwerte()