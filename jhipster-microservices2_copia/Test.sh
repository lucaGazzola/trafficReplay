#!/bin/bash
# Exec python script for REST comunication and MongoReplay Report for the response of mockupmongo
# ./Test.sh path_pyscript.py path_DirMongoReport Name_container
#Passo lo script python che permette di inviare istruzioni REST all'applicazione e la cartella contenente i Report
	#per identificare richiesta e risposta da parte del mockup mongo

#TODO possibilità di passare elenco di file ed elenco di cartelle per fare più test in modo automatico

id_mongocontainer=$(docker ps -qf "name="$3)

#Passo 1: copio sul mockup la cartella contenente i report mongo con le risposte alle richieste inviate
#Per ora non terrà in considerazione dei comandi di configurazione perchè già impostati con inizializzazione
echo $id_mongocontainer
echo "copia"
docker cp $2 $id_mongocontainer:/

#Passo 2: Mando in esecuzione lo script che manda comandi REST
echo "script"
python3 $1




