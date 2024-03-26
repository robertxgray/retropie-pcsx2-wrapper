from evdev import InputDevice, categorize, ecodes
from subprocess import Popen
import psutil
import signal
import time

#creates object 'gamepad' to store the data
#you can call it whatever you like
# you will need to check /dev/input for your specific device name like eventXX
DEVICE = '/dev/input/event13'
print(f"Connecting to {DEVICE}")
while True:
    try:
        gamepad = InputDevice(DEVICE)
        break
    except:
        pass
print("Connected!")

#button code variables (change to suit your device)
# More information from https://core-electronics.com.au/tutorials/using-usb-and-bluetooth-controllers-with-python.html
button1 = 318
button2 = 315

# Processes to look for to kill when BOTH keys are pressed
proc_names = [
    'AppRun.wrapped', # pcsx2 AppImage
    'dolphin-emu-nogui',
    'rpcs3',
    'Cemu.exe',
    'yuzu',
    'Ryujinx'
]

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    # button 1 pressed
    if event.code == button1 and event.type == ecodes.EV_KEY and event.value == 1:
        for event2 in gamepad.read_loop():
            # button 1 released
            if event2.code == button1 and event2.type == ecodes.EV_KEY and event2.value == 0:
                break
            # button 2 pressed
            elif event2.code == button2 and event2.type == ecodes.EV_KEY and event2.value == 1:
                print("PS Button and Start Pressed")
                while True:
                    for process in psutil.process_iter():
                        for param in process.cmdline():
                            for name in proc_names:
                                if name in param:
                                    print(process.cmdline())
                                    print('Process found. Terminating it.')
                                    process.send_signal(signal.SIGTERM)
                                    time.sleep(1)
                                    process.send_signal(signal.SIGHUP)
                                    time.sleep(1)
                                    process.send_signal(signal.SIGKILL)
