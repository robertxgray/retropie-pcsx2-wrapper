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
    # Tested with Dolphin 5.0
    # You need to configure IOS_WC24 logs to be written to file
    elif line.split()[-1] == 'IOCTL_NWC24_REQUEST_SHUTDOWN':
        print('Exit to menu')
        for process in psutil.process_iter():
            #print(process.cmdline())
            if procName1 in process.cmdline():
                print('Process found. Terminating it.')
                process.terminate()
                file.close()
        exit()

