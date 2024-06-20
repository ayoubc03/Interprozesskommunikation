import os
import time

# Aktuelles Vezeichnis für Start der Programme
working_directory = '/home/adam-ibrahimkhel/IPC neu/Interprozesskommunikation/Pipes (1527289)'
os.chdir(working_directory)


#Liste der zu startenden Prozesse
prozesse = ['report.py', 'log.py', 'stat.py', 'conv.py']

def runscript(scriptname):
    os.system(f'python3 {scriptname}')

if __name__ == '__main__':

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