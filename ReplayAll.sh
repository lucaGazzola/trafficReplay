#!/bin/bash

Directory=$1
#Contiene il file temporaneo con il contenuto della cartella
Fileuno=/home/luca/Tesi/trafficReplay/$1/temp

cd $Directory
if [ -e temp ]
then
	rm temp
fi

touch temp
ls >> temp

Match=temp
(IFS='
';
for riga in `cat $Fileuno`
do
	if ( ! [[ $riga == $Match ]] ) && ( [[ $riga == *.py ]] )
	then
		echo ""
		echo "----------------------Esecuzione Replay--------------------------------------"
		echo $riga
		python3 $riga
		echo "-----------------------------------------------------------------------------"
	fi 
done

)
