#!/bin/bash
# Exec python script for REST comunication and MongoReplay Report for the response of mockupmongo
# ./Test.sh Test_Suite_Dir ID_Container
# Passo la cartella dei casi di test da eseguire (sottocartelle contenenti script python per istruzioni rest e cartella con report)
#Il nome del container deve essere quello del container dove è eseguito il mockup

id_mongocontainer=$2

#Eseguo un test alla volta, copiando la rispettiva cartella dei report nel container del mockup ed eseguendo
	#lo script per le istruzioni REST
cd $1
number_test=1
fail_test=0
exec_test=0
incomplete_test=0
for dir in $( ls -vd */ ); do
	echo "----------------------- INIZIO TEST $number_test -------------------------------------"
	exec_test=$((exec_test+1))
	correct=0
	#-------------controllo che ci siano almeno due elementi nella cartella (script python + cartella dei report)--------------#
	number=$(ls -1 $dir | wc -l)
	if [ "$number" -lt "2" ] ; then
		echo "$dir non ha tutti i file necessari per il test"
		echo "----------------------- TEST $number_test FALLITO DIRECTORY $dir -------------------------------------"
		printf "\n\n"
		number_test=$((number_test+1))
		incomplete_test=$((incomplete_test+1))
		continue
	fi
	#-------------controllo se è presente la directory con i report--------------------- #
	cd $dir
	if  ! [ -d */ ] ; then
	  	echo "in $dir non è presente la directory con i report"
		cd ..
		echo "----------------------- TEST $number_test FALLITO DIRECTORY $dir -------------------------------------"
		printf "\n\n"
		number_test=$((number_test+1))
		incomplete_test=$((incomplete_test+1))
		continue	
	else
		#Copia della cartella
		for subdir in $( ls -vd */ ); do
			echo "subdir = $subdir"
			number=$(ls -1 $subdir | wc -l)
			#Controllo abbia i file di report
			if [ "$number" -lt "1" ] ; then
				echo "$subdir non ha tutti i file necessari per il test"
			else
				#Passo 1: copio sul mockup la cartella contenente i report mongo con le risposte alle richieste inviate
				#Per ora non terrà in considerazione dei comandi di configurazione perchè già impostati con inizializzazione
				if [ "$correct" -ne "1" ];then
					echo $subdir > 'ActualFileTest.txt'
				else
					echo $subdir >> 'ActualFileTest.txt'
				fi
				correct=1
				break 1
			fi
		done
		#Se non sono presenti i file necessari per il test
		if [ "$correct" -ne "1" ] ; then
		 	echo "file di report non presenti in $dir"
			cd ..
			echo "----------------------- TEST $number_test FALLITO DIRECTORY $dir -------------------------------------"
			printf "\n\n"
			number_test=$((number_test+1))
			incomplete_test=$((incomplete_test+1))
			continue
		#Altrimenti posso procedere con la copia del file di test sul container con il mockup mongo
		else
		   docker cp 'ActualFileTest.txt' $id_mongocontainer:/
		   docker cp $subdir $id_mongocontainer:/
		   sleep 10
		fi
	fi
	#-------------controllo che sia presente lo script python per le istruzioni REST----------------#
	echo $( ls *.py | wc -l )
	if [ $( ls *.py | wc -l ) -ne 0 ]; then
		for file in $( ls *.py ); do
			#Passo 2: Mando in esecuzione lo script che manda comandi REST
			python3 $file
			ret=$?
			if [ $ret -ne 0 ]; then
			     	echo "----------------------- TEST $number_test FALLITO DIRECTORY $dir -------------------------------------"
				#exit 1
				fail_test=$((fail_test+1))
			fi
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
#Aggiunta 
docker cp $id_mongocontainer:/log_file.out .

echo "REPORT:"
echo "TEST ESEGUITI: $exec_test"
echo "TEST FALLITI: $fail_test"
echo "TEST NON ESEGUITI PER MANCANZA DEI FILE NECESSESSARI: $incomplete_test"







