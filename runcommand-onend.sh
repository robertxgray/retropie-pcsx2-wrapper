#!/bin/bash
# kill python wrapper scripts
if [ $1 = 'ps2' ] || [ $1 = 'ps3' ] || [ $1 = 'wiiu' ] || [ $1 = 'gc' ]; then
	PROCS=$(ps aux | grep gamepad_wrapper | awk '{ print $2 }')
	for PROC in ${PROCS[@]}
	do
		kill "$PROC"
	done
elif [ $1 = 'wii' ]; then
	PROCS=$(ps aux | grep dolphin_wrapper | awk '{ print $2 }')
	for PROC in ${PROCS[@]}
	do
		kill "$PROC"
	done
fi
