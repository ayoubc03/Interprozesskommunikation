import random
import os
import time
import signal
import sys

fifo_path1 = '/tmp/myfifo1'
fifo_path2 = '/tmp/myfifo2'

def schliessen():
    if os.path.exists(fifo_path1):
        os.remove(fifo_path1)
    if os.path.exists(fifo_path2):
        os.remove(fifo_path2)
        
def signal_handler(sig, frame):
    schliessen()
    sys.exit(0)
            
    
    

def generiere_messwerte():
    try:
        if not os.path.exists(fifo_path1):
          os.mkfifo(fifo_path1)
        if not os.path.exists(fifo_path2):
          os.mkfifo(fifo_path2)
    except Exception as e:
        print(f"Fehler")
        sys.exit(1)
        
    while True:
        messwert = random.randint(1, 1000)
        
        try:
            with open(fifo_path1, 'w') as fifo1:
              fifo1.write(f"{messwert}\n")
            with open(fifo_path2, 'w') as fifo:
              fifo.write(f"{messwert}\n")
        except Exception as e:
         
         time.sleep(2)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    generiere_messwerte()