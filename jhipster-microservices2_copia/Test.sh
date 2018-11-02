#!/bin/bash
# Exec python script for REST comunication and MongoReplay Report for the response of mockupmongo
# ./Test.sh Test_Suite_Dir Name_container
# Passo la cartella dei casi di test da eeguire (sottocartelle contenenti script python per istruzioni rest e cartella con report)

#TODO possibilità di passare elenco di file ed elenco di cartelle per fare più test in modo automatico

id_mongocontainer=$(docker ps -qf "name="$2)
echo "id del container $2 : $id_mongocontainer"

#Eseguo un test alla volta, copiando la rispettiva cartella dei report nel container del mockup ed eseguendo
	#lo script per le istruzioni REST
cd $1
number_test=1
for dir in $( ls -vd */ ); do
	echo "----------------------- INIZIO TEST $number_test -------------------------------------"
	correct=0
	#-------------controllo che ci siano almeno due elementi nella cartella--------------#
	number=$(ls -1 $dir | wc -l)
	if [ "$number" -lt "2" ] ; then
		echo "$dir non ha tutti i file necessari per il test"
		echo "----------------------- FINE TEST $number_test -------------------------------------"
		printf "\n\n"
		number_test=$((number_test+1))
		continue
	fi
	#-------------controllo se è presente la directory con i report--------------------- #
	cd $dir
	if  ! [ -d */ ] ; then
	  	echo "in $dir non è presente la directory con i report"
		cd ..
		echo "----------------------- FINE TEST $number_test -------------------------------------"
		printf "\n\n"
		number_test=$((number_test+1))
		continue	
	else
		#Copia della cartella
		for subdir in $( ls -vd */ ); do
			number=$(ls -1 $subdir | wc -l)
			if [ "$number" -lt "1" ] ; then
				echo "$subdir non ha tutti i file necessari per il test"
			else
				#Passo 1: copio sul mockup la cartella contenente i report mongo con le risposte alle richieste inviate
				#Per ora non terrà in considerazione dei comandi di configurazione perchè già impostati con inizializzazione
				echo $subdir > 'ActualFileTest.txt'
				docker cp 'ActualFileTest.txt' $id_mongocontainer:/
				docker cp $subdir $id_mongocontainer:/
				correct=1
				break 1
			fi
		done
		if [ "$correct" -ne "1" ] ; then
		 	echo "file di report non presenti in $dir"
			cd ..
			echo "----------------------- FINE TEST $number_test -------------------------------------"
			printf "\n\n"
			number_test=$((number_test+1))
			continue
		fi
	fi
	#-------------controllo che sia presente lo script python per le istruzioni REST----------------#
	if [ -e *.py ]; then
		for file in $( ls *.py ); do
			#Passo 2: Mando in esecuzione lo script che manda comandi REST
			python3 $file
			break 1
		done
	else
		echo "in $dir non è presente lo script python"
	fi	
	echo "----------------------- FINE TEST $number_test -------------------------------------"
	printf "\n\n"
	cd ..
	number_test=$((number_test+1))
done







