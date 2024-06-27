import os

import signal
import time


script_dir = os.path.dirname(os.path.abspath(__file__)) # Returned den Pfad in dem sich das aktuelle Skript befindet
programmes = ["log.py", "report.py", "stat.py", "conv.py"] # Alle Skripte in einer Liste
programme_pfade = [os.path.join(script_dir, programme) for programme in programmes] # Fügt den absoluten Pfad den einzelnen Skripten hinzu. Dies klappt, da alle Skripte im selben Ordner sind


# Prozesse forken
try:
    for programme_pfad in programme_pfade:
        pid = os.fork()
        if pid == 0:
            # Kindprozess: Ersetzen durch neues Skript
            os.execlp("python3", "python3", programme_pfad)
       
    
    # Warten auf alle Kindprozesse
    for _ in range(len(programmes)):
        os.waitpid(-1, 0)
    
    print("Alle Prozesse sind beendet.")
except OSError as e:
    print("Fork fehlgeschlagen:", e)
    sys.exit(1)