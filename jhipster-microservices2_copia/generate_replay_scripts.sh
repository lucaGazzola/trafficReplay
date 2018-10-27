#!/bin/bash
# generates replay scripts
# usage: ./generate_replay_scripts.sh captureStreamsDirectory
cd $1
for filename in $( ls -v *.cap ); do
    destScript=$filename"_replay.py"
    python3 ../pyshark_test.py $filename $destScript
done
