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