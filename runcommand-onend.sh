#!/bin/bash
#only if for ps2, kill python wrapper script
if [ $1 = 'ps2' ] || [ $1 = 'ps3' ] || [ $1 = 'wii' ] || [ $1 = 'wiiu' ] || [ $1 = 'gc' ]; then
	PROCS=$(ps aux | grep gamepad_wrapper | awk '{ print $2 }')
	for PROC in ${PROCS[@]}
	do
		kill "$PROC"
	done
fi
