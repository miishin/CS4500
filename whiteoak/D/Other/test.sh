#!/bin/bash

python2 xgui.py
if [ $? -eq 2 ]; then 
	echo "Proper response to blank argument" 
else
	echo "Inproper response to blank argument"
fi

python2 xgui.py 0 
if [ $? -eq 2 ]; then
	echo "Proper response to "0" argument"
else 
	echo "Inproper response to "0" argument"
fi 

python2 xgui.py -1
if [ $? -eq 2 ]; then
	echo "Proper response to negative size"
else
	echo "Inproper response to negative size"
fi

python2 xgui.py "xd"
if [ $? -eq 2 ]; then
	echo "Proper response to string argument"
else
	echo "Inproper response to string argument"
fi

python2 xgui.py 100 100
if [ $? -eq 2 ]; then
	echo "Proper response to multiple command line arguments"
else
	echo "Inproper response to multiple command line arguments"
fi

python2 xgui.py 100
if [ $? -eq 0 ]; then
	echo "GUI opened and closed successfully"
else 
	echo "GUI error"
fi

