#!/bin/bash
cd $1
for filename in $( ls -v *.json ); do
	name=${filename%%.json*}
	python3 /home/luca/TesiGit/trafficReplay/readoperations.py $filename mongodb://localhost:37379
done

