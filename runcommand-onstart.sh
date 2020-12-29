#!/bin/bash
# launch python wrapper script to catch hotkey assignments
if [ $1 = 'ps2' ] || [ $1 = 'ps3' ] || [ $1 = 'wiiu' ] || [ $1 = 'wii' ] || [ $1 = 'gc' ]; then
	/opt/retropie/configs/all/gamepad_wrapper_daemon.sh &
fi
# launch dolphin wrapper script
if [ $1 = 'wii' ]; then
	python3 /opt/retropie/configs/all/dolphin_wrapper.py &
fi
