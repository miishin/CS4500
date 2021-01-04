#!/bin/bash

cd ctests
python3 ../ctest.py 2-in.json
python3 ../ctest.py 3-in.json
python3 ../ctest.py 4-in.json
python3 ../ctest.py 5-in.json
python3 ../ctest.py 6-in.json
python3 ../ctest.py 7-in.json

diff 2-in-output.json 2-out.json -w
if [ $? -eq 0 ]; then
  echo "2-in.json output good"
fi

diff 3-in-output.json 3-out.json -w
if [ $? -eq 0 ]; then
  echo "3-in.json output good"
fi

diff 4-in-output.json 4-out.json -w
if [ $? -eq 0 ]; then
  echo "4-in.json output good"
fi

diff 4-in-output.json 4-out.json -w
if [ $? -eq 0 ]; then
  echo "4-in.json output good"
fi

diff 5-in-output.json 5-out.json -w
if [ $? -eq 0 ]; then
  echo "5-in.json output good"
fi

diff 6-in-output.json 6-out.json -w
if [ $? -eq 0 ]; then
  echo "6-in.json output good"
fi

diff 7-in-output.json 7-out.json -w
if [ $? -eq 0 ]; then
  echo "7-in.json output good"
fi