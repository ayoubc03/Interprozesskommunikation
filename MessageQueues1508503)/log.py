import time
import posix_ipc
import sys
import signal

def log_process():
    # Erstellen oder Öffnen der Message Queue mit dem Namen "/conv_queue"
    conv_queue = posix_ipc.MessageQueue("/conv_queue", posix_ipc.O_CREAT)

    # Signalhandler-Funktion definieren, um den Prozess sicher zu beenden
    def signal_handler(sig, frame):
        print('Log-Prozess beendet.')
        conv_queue.close()  # Schließen der Message Queue
        sys.exit(0)  # Beenden des Programms

    # Verbinden des SIGINT-Signals (Ctrl-C) mit dem Signalhandler
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            # Empfang der Daten aus der Message Queue
            wert, _ = conv_queue.receive()
            wert = wert.decode()  # Dekodieren der Daten von Bytes zu String
            
            # Öffnen der Log-Datei im Anhangsmodus und Schreiben der empfangenen Daten
            with open("log.txt", "a") as logfile:
                logfile.write(f"{wert}\n")
            print(f"Log: Messwert {wert} in die Datei geschrieben.")
            
            time.sleep(2)  # Warten für 2 Sekunden
        except Exception as e:
            print("Ein Fehler ist aufgetreten: ", e)
