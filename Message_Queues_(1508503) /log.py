import time
import signal
import sys

def log_process(conv_queue):

    def signal_handler(sig, frame):
        print('Log-Prozess beendet.')
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            # Empfange den Messwert aus der Conv-Queue
            wert = conv_queue.get()
            # Öffne die Log-Datei im Anhangsmodus ('a') und schreibe den Messwert hinein
            with open("log.txt", "a") as logfile:
                logfile.write(f"{wert}\n")  # Schreibe den Messwert in die Log-Datei
            # Ausgabe zur Bestätigung, dass der Messwert in die Datei geschrieben wurde
            print(f"Log: Messwert {wert} in die Datei geschrieben.")
            # Warte für 2 Sekunden
            time.sleep(2)
        except Exception as e:
            
            print("Ein Fehler ist aufgetreten: ", e)
