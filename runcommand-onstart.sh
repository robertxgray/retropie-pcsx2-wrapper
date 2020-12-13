#!/bin/bash
# launch python wrapper script to catch hotkey assignments
if [ $1 = 'ps2' ] || [ $1 = 'ps3' ] || [ $1 = 'wiiu' ] || [ $1 = 'gc' ]; then
	/opt/retropie/configs/all/gamepad_wrapper_daemon.sh &
# launch dolphin wrapper script
elif [ $1 = 'wii' ]; then
	python3 /opt/retropie/configs/all/dolphin_wrapper.py &
fi
