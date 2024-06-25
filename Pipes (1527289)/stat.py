import os
import time
import signal
import sys

fifo_path2 = '/tmp/myfifo2'
fifo_path3 = '/tmp/myfifo3'

def signal_handler(sig, frame):
    sys.exit(0)

def berechne_summe_und_mittelwert():
    try:
        if not os.path.exists(fifo_path2):
            os.mkfifo(fifo_path2)
        if not os.path.exists(fifo_path3):
             os.mkfifo(fifo_path3)
    except Exception as e:
        print(f"Fehler")
        sys.exit(1)
        
    
    summe = 0
    anzahl = 0 
    
    while True:
        try:
        # Lesen der Messwerte von der benannten Pipe
             with open(fifo_path2, 'r') as fifo2:
                 messwerte = fifo2.readlines()
        
             for messwert in messwerte:
                 messwert = messwert.strip()
                 if messwert:
                  messwert = int(messwert)
                  summe += messwert 
                  anzahl += 1
                  mittelwert = summe / anzahl 
             with open(fifo_path3, 'w') as fifo:
                fifo.write(f"Summe: {summe}\n")
                fifo.write(f"Mittelwert: {mittelwert}\n")
        except Exception as e:
             print(f"Fehler")
             
        time.sleep(1)
        # Pause zwischen den Berechnungen
            
        
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    berechne_summe_und_mittelwert()
