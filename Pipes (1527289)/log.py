import os
import time
import signal
import sys

# Pfad zur benannten Pipe
fifo_path1 = '/tmp/myfifo1'
# Name der Datei, in welche die Messwerte geschrieben werden
dateiname = 'messwerte.txt'

# Signalhandler zum sauberen Beenden des Programms
def signal_handler(sig, frame):
    sys.exit(0)
 
 # Funktion zum Lesen der Messwerte aus der Pipe und Schreiben in die Datei   
def messwert_in_datei(fifo_path, dateiname):
    try:    
        # Erstellen der Pipe, falls sie nicht existiert
        if not os.path.exists(fifo_path):
            os.mkfifo(fifo_path)
    except Exception as e:
        print(f"Fehler")  
        sys.exit(1)
             
    
    while True:
        try:
            # Lesen der Messwerte aus der Pipe
            with open(fifo_path, 'r') as fifo:
                messwert = fifo.readline().strip()
        
            if messwert:
                # Schreiben des Messwerts in die Datei
                with open(dateiname, 'a') as datei:
                   datei.write(messwert + '\n')
        except Exception as e:
            print(f"Fehler")
            
        # Warten von 2 Sekunden vor dem nächsten Durchlauf
        time.sleep(2)

# Registrieren des Signalhandlers für SIGINT
if __name__ == '__main__':
   signal.signal(signal.SIGINT, signal_handler)
   # Starten der Funktion
messwert_in_datei(fifo_path1, dateiname)