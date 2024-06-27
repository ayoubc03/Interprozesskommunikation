import os
import time
import signal
import sys



#Liste der zu startenden Prozesse
prozesse = ['report.py', 'log.py', 'stat.py', 'conv.py']

def runscript(scriptname):
    os.system(f'python3 {scriptname}')
    
def signal_handler(sig, frame):
    for pid in kprozessids:
        os.kill(pid, signal.SIGINT)
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        # Durchlaufen der Prozesse und Erstellen der Kindprozesse
        kprozessids = []
        for script in prozesse:
            kprozessid = os.fork()
            if kprozessid == 0:
                runscript(script)
                os._exit(0)
            else:
                kprozessids.append(kprozessid)

        # Warten auf Abschluss der Kindprozesse
        for kind in kprozessids:
            os.wait()

        # Kurze Pause
        time.sleep(1)