import os

import signal
import time


script_dir = os.path.dirname(os.path.abspath(__file__)) # Returned den Pfad in dem sich das aktuelle Skript befindet
programmes = ["log.py", "report.py", "stat.py", "conv.py"] # Alle Skripte in einer Liste
programme_pfade = [os.path.join(script_dir, programme) for programme in programmes] # Fügt den absoluten Pfad den einzelnen Skripten hinzu. Dies klappt, da alle Skripte im selben Ordner sind


# Prozesse forken
try:
    for i, programme_pfad in enumerate(programme_pfade):
        pid = os.fork()
        if pid == 0:
            # Kindprozess: Ersetzen durch neues Skript
            os.execlp("python3", "python3", programme_pfad)
        # Sehr wichtig! Serverprozessen Zeit geben zu starten, bevor die Clientprozesse gestartet werden
        if i < 3:
            time.sleep(1)
    
    # Warten auf alle Kindprozesse
    for _ in range(len(programmes)):
        os.waitpid(-1, 0)
    
    print("Alle Prozesse sind beendet.")
except OSError as e:
    print("Fork fehlgeschlagen:", e)
    sys.exit(1)
