#!/bin/bash
cd ..
./xjson < Test/1-in.json | diff -w - Test/1-out.json
./xjson < Other/2-in.json | diff -w - Other/2-out.json
./xjson < Other/3-in.json | diff -w - Other/3-out.json
./xjson < Other/4-in.json | diff -w - Other/4-out.json
./xjson < Other/5-in.json | diff -w - Other/5-out.json
./xjson < Other/6-in.json | diff -w - Other/6-out.json
echo "Done"
cd Other
