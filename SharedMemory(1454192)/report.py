import posix_ipc
import mmap
import os
import signal
import time

# Signal-Handler für sauberes Beenden
def sigint_handler(signum, frame):
    print("Reportprozess beendet.")
    os._exit(0)

signal.signal(signal.SIGINT, sigint_handler)

# Namen des Shared Memory und Semaphoren
STAT_RESULT_SHM_NAME = "/shm_stat_result"
STAT_RESULT_SEM_NAME = "/sem_stat_result"

# Warten, bis das Shared Memory verfügbar ist
while True:
    try:
        stat_result_shm = posix_ipc.SharedMemory(STAT_RESULT_SHM_NAME)
        break
    except posix_ipc.ExistentialError:
        time.sleep(1)

stat_result_sem = posix_ipc.Semaphore(STAT_RESULT_SEM_NAME)

# Erstellen von Memory Maps
stat_result_speicher = mmap.mmap(stat_result_shm.fd, stat_result_shm.size)

# Schließen der Dateideskriptoren
stat_result_shm.close_fd()

# Endlosschleife zur Ausgabe der Daten
while True:
    stat_result_sem.acquire()
    stat_result_speicher.seek(0)
    result_daten = stat_result_speicher.read(1024).decode('utf-8').strip()
    print(result_daten)