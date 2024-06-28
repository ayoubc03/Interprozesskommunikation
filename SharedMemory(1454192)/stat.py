import posix_ipc
import mmap
import os
import signal

# Signal-Handler für sauberes Beenden
def sigint_handler(signum, frame):
    print("Statistikprozess beendet.")
    os._exit(0)

signal.signal(signal.SIGINT, sigint_handler)

# Namen des Shared Memory und Semaphoren
STAT_SHM_NAME = "/shm_stat"
STAT_SEM_NAME = "/sem_stat"
STAT_RESULT_SHM_NAME = "/shm_stat_result"
STAT_RESULT_SEM_NAME = "/sem_stat_result"