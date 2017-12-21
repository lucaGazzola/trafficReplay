#!/bin/bash
cd $1
for filename in *.cap; do
	destScript=$filename"_replay.py"
    python3.5 ../replay_scripts_generator.py $filename $destScript
done
