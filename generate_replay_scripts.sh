#!/bin/bash
# generates replay scripts
# usage: ./generate_replay_scripts.sh captureStreamsDirectory
cd $1
for filename in *.cap; do
	destScript=$filename"_replay.py"
    python3 ../pyshark_testMod2.py $filename $destScript
done
