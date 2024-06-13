import time
from multiprocessing import Queue

def log_process(conv_queue):
    while True:
        try:
            werte = conv_queue.get()  # Empfange den Messwert aus der Conv-Queue
            with open("log.txt", "a") as logfile:
                logfile.write(str(werte) + "\n")  # Schreibe den Messwert in die Log-Datei
            print(f"Log: Messwert {werte} in die Datei geschrieben.")
            time.sleep(2)  # Warte für 2 Sekunden
        except Exception as e:
            print("Ein Fehler ist aufgetreten: ", e)

if __name__ == "__main__":
    pass  # Hauptprozess benötigt keine weitere Implementierung





