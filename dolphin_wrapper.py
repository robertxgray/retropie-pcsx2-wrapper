import os
import time
import psutil
from subprocess import Popen

# Process to look for to kill
procName1 = '/opt/retropie/emulators/dolphin/bin/dolphin-emu-nogui'

# Dolphin log file
logfile = os.environ["HOME"] + '/.dolphin-emu/Logs/dolphin.log'

# Find the HOTRESET signal in logs
try:
    os.remove(logfile)
except:
    pass
file = open(logfile, 'w')
file.close()
file = open(logfile, 'r')
while True:
    line = file.readline()
    if not line:
        time.sleep(3)
    elif line.split()[-1] == 'IOCTL_STM_HOTRESET':
        print('IOCTL_STM_HOTRESET')
        for process in psutil.process_iter():
            #print(process.cmdline())
            if procName1 in process.cmdline():
                print('Process found. Terminating it.')
                file.close()
                process.terminate()
                exit()
                break

