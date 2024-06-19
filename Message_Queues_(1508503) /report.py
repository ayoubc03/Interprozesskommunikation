import time

def report_process(report_queue):
    while True:
        try:
            summe, mittelwert = report_queue.get()  # Empfange Summe und Mittelwert aus der Report-Queue
            print(f"Report: Summe {summe}, Mittelwert {mittelwert}")
            time.sleep(2)  # Warte für 2 Sekunden
        except Exception as e:
            print("Ein Fehler ist aufgetreten: ", e)
