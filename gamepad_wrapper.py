from evdev import InputDevice, categorize, ecodes
import psutil
from subprocess import Popen

#creates object 'gamepad' to store the data
#you can call it whatever you like
# you will need to check /dev/input for your specific device name like eventXX
gamepad = InputDevice('/dev/input/event15')

#button code variables (change to suit your device)
# More information from https://core-electronics.com.au/tutorials/using-usb-and-bluetooth-controllers-with-python.html
button1 = 318
button2 = 315

# Process to look for to kill when BOTH keys are pressed
procName1 = '/usr/games/PCSX2'
procName2 = '/opt/retropie/emulators/dolphin/bin/dolphin-emu-nogui'
procName3 = 'rpcs3'
procName4 = 'C:\cemu_1.21.5\Cemu.exe'

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
                for process in psutil.process_iter():
                    #print(process.cmdline())
                    if procName1 in process.cmdline() or procName2 in process.cmdline() or procName3 in process.cmdline() or procName4 in process.cmdline():
                        print('Process found. Terminating it.')
                        process.terminate()
                exit()

