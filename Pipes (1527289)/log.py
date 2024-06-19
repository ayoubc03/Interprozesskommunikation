import os
import time

fifo_path1 = '/tmp/myfifo1'
dateiname = 'messwerte.txt'

def messwert_in_datei(fifo_path, dateiname):
    while True:
        # Lesen des Messwerts von der benannten Pipe
        with open(fifo_path, 'r') as fifo:
            messwert = fifo.read().strip()
        
        # Messwert in die Datei schreiben
            with open(dateiname, 'a') as datei:
                datei.write(messwert + '\n')
                print(f"Die Datei '{dateiname}' wurde erstellt und der Messwert {messwert} wurde in die Datei geschrieben.")
            
            # Überprüfung, ob Messwert in die Datei geschrieben wurde
            if os.path.exists(dateiname):
                with open(dateiname, 'r') as datei:
                    gespeicherterMesswert = datei.read()
                   
            else:
                print('Die Datei/Der Messwert existiert nicht.')
        
        time.sleep(1)  # Pause zwischen den Operationen

if __name__ == '__main__':
    messwert_in_datei(fifo_path1, dateiname)