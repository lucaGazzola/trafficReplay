#!/bin/bash
# generates replay scripts
# usage: ./generate_replay_scripts.sh TestDir/captureStreamsDirectory ip_list password_list
# ip_auth_service serve per ottenere token di autenticazione
# ip_list lista degli indirizzi ip dei container da tenere in considerazione (posso prenderli dal file di test creato dalla cattura)
# password_list lista delle password associate alle applicazioni i cui indirizzi ip sono specificati nella lista degli ip
if [[ $# -lt 3 ]] ; then 
	echo 'missing args ---> ./generate_replay_scripts.sh <testdir/captureStreamsDirectory> <ip_list> <password_list>'
	exit 1
fi

if [ $((($#-1)%2)) -ne 0 ]; then
	echo 'number of passwords and ip must be the same'
	exit 1
fi


#una parte del filtraggio è stata fatta durante lo split
#adesso devo specificare gli ip delle applicazioni che voglio considerare
#TODO considerare caso in cui applicazione non ha la password
cd $1
for filename in $( ls -v *.cap ); do
    	destScript=$filename"_replay.py"
    	listIP="${@:2:$((($#-1)/2))}"
	listPass="${@:$(((2+($#-1)/2))):$((($#-1)/2))}"
	listIP=$(echo ${listIP// /,})
	listPass=$(echo ${listPass// /,})
	#echo $listIP
	#echo $listPass
	#Passo come argomento unica stringa e da pyhton creo lista
    	python3 ../../pyshark_test.py $filename $destScript $listPass $listIP 
done
exit 0
