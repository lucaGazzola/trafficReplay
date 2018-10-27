#!/bin/bash
# generates test report with mongoreplay
# usage: ./generate_test_replay.sh MongoStreamDirectory Name_container
if [[ $# -lt 2 ]] ; then
    echo 'missing directories ----> use ./generate_test_replay.sh <mongo_directory> <container name>'
    exit 0
fi

#------------->cambiare il nome del container che fa girare il database nel caso sia diverso<----------------
id_mongocontainer=$(docker ps -aqf "name="$2)
inspect=$(docker inspect $id_mongocontainer | grep "IPAddress")
ipdb=${inspect%,*}     # trim everything past the last ,
ipdb=${ipdb##*,}       # ...then remove everything before the last , remaining
ipdb=$(grep -oP '(?<=").*?(?=")' <<< "$ipdb")
ipdb=${ipdb##*:}
ipdb=${ipdb##* }
ipdb="$(echo -e "${ipdb}" | tr -d '[:space:]')"
echo "ip container = "$ipdb
#Prima vado ad eseguire mongo replay per i file contenuti nella cartella
cd $1
echo $1

if [ ! -d "recordings" ]; 
then 
	mkdir "recordings"; 
fi

if [ ! -d "reports" ]; 
then 
	mkdir "reports"; 
fi

cd reports

if [ ! -d "CMDs" ]; 
then 
	mkdir "CMDs"; 
fi

if [ ! -d "Config" ]; 
then 
	mkdir "Config"; 
fi

cd ..

if [ ! -d "monitor" ]; 
then 
	mkdir "monitor"; 
fi
for filename in $( ls -v *.cap ); do
	name=${filename%%.cap*}
	echo $name
	mongoreplay record -f $filename -p ../$1/recordings/test_$name.bson
	#Creo una cartella con i report sui pacchetti di controllo ed una con i report sui pacchetti contenenti comandi per il database
	if  ! ([[ $name == *"find"* ]] || [[ $name == *"delete"* ]] || [[ $name == *"update"* ]] || [[ $name == *"insert"* ]] || [[ $name == *"count"* ]]); 		
	then
		mongoreplay play -p ../$1/recordings/test_$name.bson --report ../$1/reports/Config/test-$name.json --collect json --host mongodb://$ipdb:27017 
		 #Se il file è vuoto lo elimino
		if [ ! -s ../$1/reports/Config/test-$name.json ];
		then
        		rm -f ../$1/reports/Config/test-$name.json
		fi
	else
		mongoreplay play -p ../$1/recordings/test_$name.bson --report ../$1/reports/CMDs/test-$name.json --collect json --host mongodb://$ipdb:27017
	fi
	mongoreplay monitor -p ../$1/recordings/test_$name.bson --report ../$1/monitor/monitoring-$name.json --collect json
done
