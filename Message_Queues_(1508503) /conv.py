import random
import time
import signal
import sys

def conv(conv_queue, stat_queue):
    # Signalhandler-Funktion, um den Conv-Prozess zu beenden
    def signal_handler(sig, frame):
        print('Conv-Prozess beendet.')
        sys.exit(0)

    # Registriere den Signalhandler für SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            # Generiere eine Zufallszahl zwischen 1 und 100
            zufallszahl = random.randint(1, 100)
            # Füge die Zufallszahl in die Conv-Queue ein
            conv_queue.put(zufallszahl)
            # Füge die Zufallszahl in die Stat-Queue ein
            stat_queue.put(zufallszahl)
            # Ausgabe zur Bestätigung der eingefügten Zufallszahl
            print(f"Conv: Zufallszahl {zufallszahl} in die Queue eingefügt.")
            # Warte für 2 Sekunden
            time.sleep(2)
        except Exception as e:
            # Ausgabe einer Fehlermeldung, falls eine Exception auftritt
            print("Ein Fehler ist aufgetreten: ", e)
