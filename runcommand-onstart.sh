#!/bin/bash
# launch python wrapper script to catch hotkey assignments
if [ $1 = 'gc' ] || [ $1 = 'ps2' ] || [ $1 = 'ps3' ] || [ $1 = 'switch' ] || [ $1 = 'wii' ] || [ $1 = 'wiiu' ]
then
	/opt/retropie/configs/all/gamepad_wrapper_daemon.sh &
fi
# launch dolphin wrapper script
#if [ $1 = 'wii' ]; then
#	(sleep 10 && python3 /opt/retropie/configs/all/dolphin_wrapper.py) &
#fi
