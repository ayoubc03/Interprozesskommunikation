import os
import time
import signal
import sys

fifo_path3 = '/tmp/myfifo3'

def signal_handler(sig, frame):
    sys.exit(0)

def ausgabe_ergebnisse():
    try:
        if not os.path.exists(fifo_path3):
            os.mkfifo(fifo_path3)
    except Exception as e:
        print(f"Error creating FIFO: {e}")
        sys.exit(1)
    
    while True:
        try:
            with open(fifo_path3, 'r') as fifo:
                ergebnisse = fifo.read().strip()
                if ergebnisse:
                    print(f"Ergebnisse:\n{ergebnisse}\n-----------------")
        except Exception as e:
            print(f"Error reading from FIFO: {e}")
        
        time.sleep(1)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    ausgabe_ergebnisse()