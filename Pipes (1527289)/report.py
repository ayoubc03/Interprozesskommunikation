import os
import time
import signal
import sys

# Pfad zur benannten Pipe
fifo_path3 = '/tmp/myfifo3'

# Signalhandler für ein sauberes Beenden des Programms
def signal_handler(sig, frame):
    sys.exit(0)

# Funktion zur Ausgabe der Ergebnisse
def ausgabe_ergebnisse():
    try:
        if not os.path.exists(fifo_path3):
            os.mkfifo(fifo_path3)
    except Exception as e:
        print(f"Error creating FIFO: {e}")
        sys.exit(1)
    
    while True:
        try:
            # Lesen der Ergebnisse aus der dritten Pipe
            with open(fifo_path3, 'r') as fifo:
                ergebnisse = fifo.read().strip()
                if ergebnisse:
                    # Ausgabe der Ergebnisse auf dem Bildschirm
                    print(f"Ergebnisse:\n{ergebnisse}\n-----------------")
        except Exception as e:
            print(f"Error reading from FIFO: {e}")
        
        # Warten von einer Sekunde vor der nächsten Wiederholung
        time.sleep(1)

if __name__ == '__main__':
    # Registrieren des Signalhandlers für SIGINT
    signal.signal(signal.SIGINT, signal_handler)
    # Starten der Funktion
    ausgabe_ergebnisse()