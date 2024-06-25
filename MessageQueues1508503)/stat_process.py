import time
import posix_ipc
import sys
import signal

def stat_process():
    ## Öffnen der Message Queues
    stat_queue = posix_ipc.MessageQueue("/stat_queue", posix_ipc.O_CREAT)
    report_queue = posix_ipc.MessageQueue("/report_queue", posix_ipc.O_CREAT)
    
    summe = 0  
    anzahl = 0  

    
    def signal_handler(sig, frame):
        print('Stat-Prozess beendet.')  
        stat_queue.close()  # Schließen der stat_queue
        report_queue.close()  # Schließen der report_queue
        sys.exit(0)  # Prozess beenden

    
    signal.signal(signal.SIGINT, signal_handler)
    
    while True:
        try:
            # Empfangen der Daten von der stat_queue
            wert, _ = stat_queue.receive()
            wert = int(wert.decode())  # Nachricht decodieren und in eine Ganzzahl umwandeln
            print(f"Stat: Empfangener Wert {wert}")  # Den empfangenen Wert ausgeben
            
            
            summe += wert
            anzahl += 1
            
            # Den Mittelwert berechnen
            mittelwert = summe / anzahl
            
            # Summe und Mittelwert an die report_queue senden
            report_queue.send(f"{summe},{mittelwert}")
            
           
            time.sleep(2)
        except Exception as e:
           
            print("Ein Fehler ist aufgetreten: ", e)
