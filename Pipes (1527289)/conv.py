import random
import os
import time
import signal
import sys

# Pfade zu den benannten Pipes
fifo_path1 = '/tmp/myfifo1'
fifo_path2 = '/tmp/myfifo2'

# Funktion zum Löschen der Pipes
def schliessen():
    if os.path.exists(fifo_path1):
        os.remove(fifo_path1)
    if os.path.exists(fifo_path2):
        os.remove(fifo_path2)
  
 # Signalhandler zum sauberen Beenden des Programms       
def signal_handler(sig, frame):
    schliessen()
    sys.exit(0)
            
    
    
# Funktion zur Generierung von Messwerten und Schreiben in die Pipes
def generiere_messwerte():
    try:
        # Erstellen der Pipes, falls diese noch nicht existieren
        if not os.path.exists(fifo_path1):
          os.mkfifo(fifo_path1)
        if not os.path.exists(fifo_path2):
          os.mkfifo(fifo_path2)
    except Exception as e:
        print(f"Fehler")
        sys.exit(1)
        
    while True:
        # Generieren eines zufälligen Messwertes zwischen 1 und 1000
        messwert = random.randint(1, 1000)
        
        try:
            # Schreiben des Messwertes in die erste Pipe
            with open(fifo_path1, 'w') as fifo1:
              fifo1.write(f"{messwert}\n")
              # Schreiben des Messwertes in die zweite Pipe
            with open(fifo_path2, 'w') as fifo:
              fifo.write(f"{messwert}\n")
        except Exception as e:
         
         # Warten von 2 Sekunden vor der nächsten Wiederholung
         time.sleep(2)

if __name__ == '__main__':
    # Registrieren des Signalhandlers für SIGINT
    signal.signal(signal.SIGINT, signal_handler)
   # Starten der Funktion
    generiere_messwerte()