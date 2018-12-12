#!/bin/bash
# generates replay scripts
# usage: ./generate_replay_scripts.sh TestDir/captureStreamsDirectory port_gateway ports_list 
# port_gateway per ora ci server per autenticazione
# tutte le porte elencate sono porte su localhost ---> mappate su porte del localhost
if [[ $# -lt 3 ]] ; then 
	echo 'missing args ---> ./generate_replay_scripts.sh <testdir/captureStreamsDirectory> <test_directory> <port_gateway> <ports_list>'
	exit 1
fi
#una parte del filtraggio è stata fatta durante lo split
#adesso devo specificare i numeri di porta esposti dalle applicazioni che voglio considerare
cd $1
for filename in $( ls -v *.cap ); do
    	destScript=$filename"_replay.py"
    	list="${@:3:$(($#-2))}"
    	python3 ../../pyshark_test.py $filename $destScript $list $2
done
exit 0
