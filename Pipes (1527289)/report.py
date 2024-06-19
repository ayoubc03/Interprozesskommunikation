import os
import time

fifo_path3 = '/tmp/myfifo3'

def ausgabe_ergebnisse():
    if not os.path.exists(fifo_path3):
        os.mkfifo(fifo_path3)
    
    while True:
        # Öffne fifo_path3 zum Lesen der Ergebnisse
        with open(fifo_path3, 'r') as fifo:
            ergebnisse = fifo.read().strip()
            if ergebnisse:
                print(f"Ergebnisse:\n{ergebnisse}\n-----------------")
        
        # Kurze Pause, bevor erneut nach neuen Daten gesucht wird
        time.sleep(1)

if __name__ == '__main__':
    ausgabe_ergebnisse()
