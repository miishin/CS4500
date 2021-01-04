#!/bin/bash

cd ..

./xtree < Tests/1-in.json > 1-out.json
./xtree < Tests/2-in.json > 2-out.json
./xtree < Tests/3-in.json > 3-out.json

DIFF1=$(diff -w Tests/1-out.json 1-out.json)
if [ "$DIFF1" == "" ]
then
  echo "1-out.json correct"
  rm 1-out.json
fi

DIFF2=$(diff -w Tests/2-out.json 2-out.json)
if [ "$DIFF2" == "" ]
then
  echo "2-out.json correct"
  rm 2-out.json
fi


DIFF3=$(diff -w Tests/3-out.json 3-out.json)
if [ "$DIFF3" == "" ]
then
  echo "3-out.json correct"
  rm 3-out.json
fi

cd Other