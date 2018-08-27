#!/bin/bash
# generates replay scripts
# usage: ./generate_replay_scripts.sh captureStreamsDirectory
cd $1
for filename in *.cap; do
    destScript=$filename"_replay.py"
    python3 ../pyshark_test_mod.py $filename $destScript
done
