import time

def log_process(conv_queue):
    while True:
        try:
            wert = conv_queue.get()  # Empfange den Messwert aus der Conv-Queue
            with open("log.txt", "a") as logfile:
                logfile.write(f"{wert}\n")  # Schreibe den Messwert in die Log-Datei
            print(f"Log: Messwert {wert} in die Datei geschrieben.")
            time.sleep(2)  # Warte für 2 Sekunden
        except Exception as e:
            print("Ein Fehler ist aufgetreten: ", e)
