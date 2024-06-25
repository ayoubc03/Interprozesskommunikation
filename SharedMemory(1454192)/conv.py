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



