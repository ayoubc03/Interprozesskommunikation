import posix_ipc
import mmap
import os
import signal

# Signal-Handler für sauberes Beenden
def sigint_handler(signum, frame):
    print("Log-Prozess beendet.")
    os._exit(0)

signal.signal(signal.SIGINT, sigint_handler)

# Namen des Shared Memory und Semaphoren
LOG_SHM_NAME = "/shm_log"
LOG_SEM_NAME = "/sem_log"

# Erstellen oder Öffnen von Shared Memory und Semaphoren
log_shm = posix_ipc.SharedMemory(LOG_SHM_NAME)
log_sem = posix_ipc.Semaphore(LOG_SEM_NAME)

# Erstellen von Memory Maps
log_speicher = mmap.mmap(log_shm.fd, log_shm.size)

# Schließen des Dateideskriptors
log_shm.close_fd()

# Endlosschleife zum Schreiben in die Datei
with open("log.txt", "w", encoding="utf-8") as logfile:
    while True:
        log_sem.acquire()
        log_speicher.seek(0)
        daten = log_speicher.read(1024).decode('utf-8').strip()
        logfile.write(daten + "\n")
        logfile.flush()
