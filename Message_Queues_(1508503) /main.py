from multiprocessing import Queue, Process
from conv import conv
from log import log_process
from stat_process import stat_process
from report import report_process

if __name__ == "__main__":
    # Erstelle die Queues für die Interprozesskommunikation
    conv_queue = Queue()    # Queue für Conv -> Log
    stat_queue = Queue()    # Queue für Conv -> Stat
    report_queue = Queue()  # Queue für Stat -> Report

    # Starte den Log-Prozess
    log_proc = Process(target=log_process, args=(conv_queue,))
    log_proc.start()

    # Starte den Stat-Prozess
    stat_proc = Process(target=stat_process, args=(stat_queue, report_queue))
    stat_proc.start()

    # Starte den Report-Prozess
    report_proc = Process(target=report_process, args=(report_queue,))
    report_proc.start()

    # Starte den Conv-Prozess
    conv(conv_queue, stat_queue)

    # Warte auf das Ende der Prozesse
    log_proc.join()
    stat_proc.join()
    report_proc.join()
