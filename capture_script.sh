#!/bin/bash
#Devono essere passati almeno un argomento: il nome dell'interfaccia sulla quale ascoltare
#Se viene passato anche il secondo argomento indica la lista lista dei nomi delle applicazioni da monitorare
echo $#
#Mancano gli argomenti obbligatori
if [[ $# -lt 2 ]] ; then 
	echo 'missing args ---> ./capture_script.sh <name_pcap_file> <interface> [<list_of_container>]'
	exit 1
fi

#C'è solo interfaccia quindi catturo tutto il traffico sull'interfaccia specificata
if [[ $# -eq 2 ]] ; then 
	echo "c'è solo l'interfaccia quindi catturo tutto"
	sudo tcpdump -i $2 -w $1.pcap
	exit 0
fi

#C'è un solo nome di container quindi catturo pacchetti solo che comprendono questo container negli ip di dst o src
if [[ $# -eq 3 ]] ; then 
	echo "c'è interfaccia e 1 container"
	id_application=$(docker ps -aqf "name="$3)
	inspect=$(docker inspect $id_application | grep "IPAddress")
	ipapp=${inspect%,*}     # trim everything past the last ,
	ipapp=${ipapp##*,}       # ...then remove everything before the last , remaining
	ipapp=$(grep -oP '(?<=").*?(?=")' <<< "$ipapp")
	ipapp=${ipapp##*:}
	ipapp=${ipapp##* }
	ipapp="$(echo -e "${ipapp}" | tr -d '[:space:]')"
	echo "ip dell'applicazione $container_name : $ipapp"
	sudo tcpdump -i $2 -n "dst host $id_application or src host $id_application" -w $1.pcap
	exit 0
#Lista di container --> devo catturare solo interazioni tra questi specificati ed i loro database
#Se voglio catturare anche nterazione con i loro database devo passare anche nome dei loro container (dei db)
else
	echo "c'è interfaccia e lista di container"
	i=2
	condizione="( "
	list=${@:3:$(($#-2))}
	echo $list
	for container_name in $list; do
		echo $container_name
		id_application=$(docker ps -aqf "name="$container_name)
		inspect=$(docker inspect $id_application | grep "IPAddress")
		ipapp=${inspect%,*}     # trim everything past the last ,
		ipapp=${ipapp##*,}       # ...then remove everything before the last , remaining
		ipapp=$(grep -oP '(?<=").*?(?=")' <<< "$ipapp")
		ipapp=${ipapp##*:}
		ipapp=${ipapp##* }
		ipapp="$(echo -e "${ipapp}" | tr -d '[:space:]')"
		echo "id dell'applicazione $container_name : $ipapp"
		i=$((i+1))
		if [[ $i -eq $# ]] ; then
			condizione="$condizione host $ipapp )"
		else
			condizione="$condizione host $ipapp or"
		fi
	done
	sudo tcpdump -i $2 -n "$condizione" -w $1.pcap
	echo "condizione finale = $condizione"
	exit 0
fi
