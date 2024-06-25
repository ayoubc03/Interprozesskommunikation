import time
import posix_ipc
import sys
import signal

def report_process():
    # Erstellen oder Öffnen der Message Queue mit dem Namen "/report_queue"
    report_queue = posix_ipc.MessageQueue("/report_queue", posix_ipc.O_CREAT)

    # Signalhandler-Funktion definieren, um den Prozess sicher zu beenden
    def signal_handler(sig, frame):
        print('Report-Prozess beendet.')
        report_queue.close()  # Schließen der Message Queue
        sys.exit(0)  # Beenden des Programms

    # Verbinden des SIGINT-Signals (Ctrl-C) mit dem Signalhandler
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            # Empfang der Nachricht aus der Message Queue
            daten, _ = report_queue.receive()
            daten = daten.decode()  # Dekodieren der Nachricht von Bytes zu String
            summe, mittelwert = daten.split(',')  # Aufteilen der empfangenen Daten in Summe und Mittelwert
            
            # Ausgabe der empfangenen Daten auf der Konsole
            print(f"Report: Summe {summe}, Mittelwert {mittelwert}")
            
            time.sleep(2)  # Warten für 2 Sekunden
        except Exception as e:
            # Fehlermeldung ausgeben, falls ein Fehler auftritt
            print("Ein Fehler ist aufgetreten: ", e)
