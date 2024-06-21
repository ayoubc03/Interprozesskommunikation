import time
import posix_ipc
import sys
import signal

def stat_process():
    stat_queue = posix_ipc.MessageQueue("/stat_queue", posix_ipc.O_CREAT)
    report_queue = posix_ipc.MessageQueue("/report_queue", posix_ipc.O_CREAT)
    summe = 0
    anzahl = 0

    def signal_handler(sig, frame):
        print('Stat-Prozess beendet.')
        stat_queue.close()
        report_queue.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    while True:
        try:
            wert, _ = stat_queue.receive()
            wert = int(wert.decode())
            print(f"Stat: Empfangener Wert {wert}")
            summe += wert
            anzahl += 1
            mittelwert = summe / anzahl
            report_queue.send(f"{summe},{mittelwert}")
            time.sleep(2)
        except Exception as e:
            print("Ein Fehler ist aufgetreten: ", e)