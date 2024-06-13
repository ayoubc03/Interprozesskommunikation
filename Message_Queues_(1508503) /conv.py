import random
import time
from multiprocessing import Queue
from log import log_process  # Importiere die log_process Funktion aus log.py

def conv(conv_queue):
    while True:
        try:
            # Generiere eine Zufallszahl und füge sie in die Queue ein
            zufallszahl = random.randint(0, 100)
            conv_queue.put(zufallszahl)
            print(f"Conv: Zufallszahl {zufallszahl} in die Queue eingefügt.")
            time.sleep(2)  # Warte für 2 Sekunden
        except Exception as e:
            print("Ein Fehler ist aufgetreten: ", e)

if __name__ == "__main__":
    conv_queue = Queue()  # Erstelle eine Queue für die Kommunikation
    # Starte den Log-Prozess als separaten Prozess
    from multiprocessing import Process
    log_proc = Process(target=log_process, args=(conv_queue,))
    log_proc.start()
    
    # Starte den Conv-Prozess
    conv(conv_queue)

