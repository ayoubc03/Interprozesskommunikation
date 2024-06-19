import os
import time

fifo_path1 = '/tmp/myfifo1'
dateiname = 'messwerte.txt'

def messwert_in_datei(fifo_path, dateiname):
    if not os.path.exists(fifo_path):
        os.mkfifo(fifo_path)
    
    while True:
        with open(fifo_path, 'r') as fifo:
            messwert = fifo.readline().strip()
        
        if messwert:
            with open(dateiname, 'a') as datei:
                datei.write(messwert + '\n')
                print(f"Messwert {messwert} wurde in die Datei '{dateiname}' geschrieben.")
        
        time.sleep(1)

if __name__ == '__main__':
    messwert_in_datei(fifo_path1, dateiname)
