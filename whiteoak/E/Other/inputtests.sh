#!/bin/bash

./xtcp.py a
if [ $? -eq 2 ]; then 
	echo "String instead of port number caught"
else
	echo "String instead of port number not caught"
fi

./xtcp.py 1 2
if [ $? -eq 2 ]; then
	echo "Multiple arguments caught"
else
	echo "Multiple arguments not caught"
fi

./xtcp.py 10
if [ $? -eq 2 ]; then
  echo "Port number < 1024 caught"
else
  echo "Port number < 1024 not caught"
fi

./xtcp.py 65536
if [ $? -eq 2 ]; then
  echo "Port number > 65535 caught"
else
  echo "Port number > 65535 not caught"
fi