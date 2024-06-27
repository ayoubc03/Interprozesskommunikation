import posix_ipc
import mmap
import os
import time
import random
import signal

# Signal-Handler für sauberes Beenden
def sigint_handler(signum, frame):
    print("Konverterprozess beendet.")
    os._exit(0)

signal.signal(signal.SIGINT, sigint_handler)

# Namen des Shared Memory und Semaphoren
STAT_SHM_NAME = "/shm_stat"
STAT_SEM_NAME = "/sem_stat"
LOG_SHM_NAME = "/shm_log"
LOG_SEM_NAME = "/sem_log"

# Erstellen oder Öffnen von Shared Memory und Semaphoren
stat_shm = posix_ipc.SharedMemory(STAT_SHM_NAME, posix_ipc.O_CREAT, size=1024)
stat_sem = posix_ipc.Semaphore(STAT_SEM_NAME, posix_ipc.O_CREAT, initial_value=0)
log_shm = posix_ipc.SharedMemory(LOG_SHM_NAME, posix_ipc.O_CREAT, size=1024)
log_sem = posix_ipc.Semaphore(LOG_SEM_NAME, posix_ipc.O_CREAT, initial_value=0)

# Erstellen von Memory Maps
stat_speicher = mmap.mmap(stat_shm.fd, stat_shm.size)
log_speicher = mmap.mmap(log_shm.fd, log_shm.size)

# Schließen der Dateideskriptoren
stat_shm.close_fd()
log_shm.close_fd()

# Endlosschleife zur Generierung von Daten
while True:
    wert = random.randint(0, 100)
    daten = f"{wert}\n"

    # Schreiben in das Log-Shared-Memory
    log_speicher.seek(0)
    log_speicher.write(daten.encode('utf-8'))
    log_speicher.flush()
    log_sem.release()

    # Schreiben in das Stat-Shared-Memory
    stat_speicher.seek(0)
    stat_speicher.write(daten.encode('utf-8'))
    stat_speicher.flush()
    stat_sem.release()

    time.sleep(1)

