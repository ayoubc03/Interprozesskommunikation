import os
import time
import signal
import sys

fifo_path1 = '/tmp/myfifo1'
dateiname = 'messwerte.txt'

def signal_handler(sig, frame):
    sys.exit(0)
    
def messwert_in_datei(fifo_path, dateiname):
    try:    
        if not os.path.exists(fifo_path):
            os.mkfifo(fifo_path)
    except Exception as e:
        print(f"Fehler")  
        sys.exit(1)
             
    
    while True:
        try:
            with open(fifo_path, 'r') as fifo:
                messwert = fifo.readline().strip()
        
            if messwert:
                with open(dateiname, 'a') as datei:
                   datei.write(messwert + '\n')
        except Exception as e:
            print(f"Fehler")
            
        
        time.sleep(2)

if __name__ == '__main__':
   signal.signal(signal.SIGINT, signal_handler)
messwert_in_datei(fifo_path1, dateiname)