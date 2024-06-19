import time

def stat_process(stat_queue, report_queue):
    summe = 0
    anzahl = 0
    while True:
        try:
            wert = stat_queue.get()  # Empfange den Messwert aus der Stat-Queue
            print(f"Stat: Empfangener Wert {wert}")
            summe += wert
            anzahl += 1
            mittelwert = summe / anzahl
            report_queue.put((summe, mittelwert))  # Übermittle Summe und Mittelwert an die Report-Queue
            time.sleep(2)  # Warte für 2 Sekunden
        except Exception as e:
            print("Ein Fehler ist aufgetreten: ", e)
