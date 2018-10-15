#!/bin/bash
# generates test report with mongoreplay
# usage: ./generate_test_replay.sh MongoStreamDirectory OPDir Name_container
if [[ $# -lt 2 ]] ; then
    echo 'missing directories ----> use ./generate_test_replay.sh <mongo_directory> <operations directory>'
    exit 0
fi

#------------->cambiare il nome del container che fa girare il database nel caso sia diverso<----------------
id_mongocontainer=$(docker ps -aqf "name="$3)
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
if [ ! -d "monitor" ]; 
then 
	mkdir "monitor"; 
fi
cd $2 #----------Questa perte può essere modificata nel caso in cui siano solo le operazioni in Operation ad essere fatte
for filename in $( ls -v *.cap ); do
	name=${filename%%.cap*}
	echo $name
	mongoreplay record -f $filename -p ../../$1/recordings/test_$name.bson
	mongoreplay play -p ../../$1/recordings/test_$name.bson --report ../../$1/reports/test-$name.json --collect json --host mongodb://$ipdb:27017 
	mongoreplay monitor -p ../../$1/recordings/test_$name.bson --report ../../$1/monitor/monitoring-$name.json --collect json
done
