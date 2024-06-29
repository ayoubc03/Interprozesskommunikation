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

# Erstellen von Shared Memory und Semaphoren
stat_shm = posix_ipc.SharedMemory(STAT_SHM_NAME)
stat_sem = posix_ipc.Semaphore(STAT_SEM_NAME)
stat_result_shm = posix_ipc.SharedMemory(STAT_RESULT_SHM_NAME, posix_ipc.O_CREAT, size=1024)
stat_result_sem = posix_ipc.Semaphore(STAT_RESULT_SEM_NAME, posix_ipc.O_CREAT, initial_value=0)

# Erstellen von Memory Maps
stat_speicher = mmap.mmap(stat_shm.fd, stat_shm.size)
stat_result_speicher = mmap.mmap(stat_result_shm.fd, stat_result_shm.size)

# Schließen der Dateideskriptoren
stat_shm.close_fd()
stat_result_shm.close_fd()

# Endlosschleife zur Berechnung der Werte
werte = []
while True:
    stat_sem.acquire()
    stat_speicher.seek(0)
    daten = stat_speicher.read(1024).decode('utf-8').strip()
    
    # Wert aus dem Speicher lesen
    try:
        wert = int(daten.split()[0])
    except (ValueError, IndexError):
        continue
    
    werte.append(wert)
    
    mittelwert = sum(werte) / len(werte)
    summe = sum(werte)
    
    result_daten = f"Mittelwert: {mittelwert}, Summe: {summe}\n"
    
    # Schreiben in das Shared-Memory
    stat_result_speicher.seek(0)
    stat_result_speicher.write(b'\x00' * 1024)  # Speicher mit Nullen überschreiben
    stat_result_speicher.seek(0)
    stat_result_speicher.write(result_daten.encode('utf-8'))
    stat_result_speicher.flush()
    stat_result_sem.release()
