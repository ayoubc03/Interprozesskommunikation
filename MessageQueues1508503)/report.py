import time
import posix_ipc
import sys
import signal

def report_process():
    report_queue = posix_ipc.MessageQueue("/report_queue", posix_ipc.O_CREAT)
    def signal_handler(sig, frame):
        print('Report-Prozess beendet.')
        report_queue.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            daten, _ = report_queue.receive()
            daten = daten.decode()
            summe, mittelwert = daten.split(',')
            print(f"Report: Summe {summe}, Mittelwert {mittelwert}")
            time.sleep(2)
        except Exception as e:
            print("Ein Fehler ist aufgetreten: ", e)