# retropie-pcsx2-wrapper
This is a wrapper for PCSX2, RPCS3 and Dolphin for Retropie, it uses a simple python wrapper to intercept a key combination to exit the emulator on keypress

## Installation
Copy everything but the README to /opt/retropie/configs/all
This Python script requires ```evdev``` and ```psutil``` which can both be installed using pip

`pip install evdev`

`pip install psutil`

Make the scripts executable

`chmod +x runcommand-onstart.sh`

`chmod +x runcommand-onend.sh`

`chmod +x gamepad_wrapper.py`

### runcommand-onstart.sh
This bash script is executed by RetroArch when any ROM is loaded. If the system is PS2, PS3, GC or WII then this executes the gamepad_wrapper.py script. 

If it is any other system this does not run. This should be able to be modified for any system by just updating the commands

### gamepad_wrapper.py
This Python script requires ```evdev``` and ```psutil``` which can both be installed using pip

This will start a Python listener using evdev that upon the specified key press will kill the emulators

You may need to edit the following line 

```gamepad = InputDevice('/dev/input/event15')```

And edit /dev/input/event15 with whichever one your controller is recognized as

When the specified key combo is pressed, it will kill the emulators, then RetroArch will run the runcommand-onend.sh script

### runcommand-onend.sh
This Script is executed by RetroArch when the emulator exits and is only here to cleanup the Python wrapper process

## Usage
There should be nothing additional needed as these scripts should execute each time that RetroArch uses runcommand to launch an emulator

