import os
import sys
import signal
import time


def signal_handler(sig, frame): # Funktion für den signal handler um einen KeyBoard Interrupt anzuzeigen
    print("\nBeende...")
    sys.exit(0)
    


signal.signal(signal.SIGINT, signal_handler) # Der Signal Handler wird hier eingerichtet SIGINT steht für SignalInterrupt (STRG + C)
script_dir = os.path.dirname(os.path.abspath(__file__)) # Returned den Pfad in dem sich das aktuelle Skript befindet
programmes = ["log.py", "stats.py", "report.py", "conv.py"] # Alle Skripte in einem Array
programme_pfade = [os.path.join(script_dir, programme) for programme in programmes] # Fügt den absoluten Pfad den einzelnen Skripten hinzu. Dies klappt, da alle Skripte im selben Ordner sind


