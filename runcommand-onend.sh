#!/bin/bash
# kill python wrapper scripts
if [ $1 = 'gc' ] || [ $1 = 'ps2' ] || [ $1 = 'ps3' ] || [ $1 = 'switch' ] || [ $1 = 'wii' ] || [ $1 = 'wiiu' ]
then
	PROCS=$(ps aux | grep gamepad_wrapper | awk '{ print $2 }')
	for PROC in ${PROCS[@]}
	do
		kill "$PROC"
	done
fi
if [ $1 = 'wii' ]; then
	PROCS=$(ps aux | grep dolphin_wrapper | awk '{ print $2 }')
	for PROC in ${PROCS[@]}
	do
		kill "$PROC"
	done

	# Workaround to restore bluetooth
	#sudo modprobe -r btusb
	#sudo modprobe btusb
fi
