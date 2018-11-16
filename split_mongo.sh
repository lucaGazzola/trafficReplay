#usage: ./split_mongo.sh pcapfile.pcap savedir

if [[ $# -lt 2 ]] ; then 
	echo 'missing args ---> ./split_mongo.sh <pcapfile.pcap> <savedir> [<list_of_containers_ip>]'
	exit 1
fi

if [ ! -d "$2" ]; 
then 
	mkdir $2; 
fi
count_op=0

#Se ho passato come argomenti i nomi dei container allora effettuo il filtraggio
#Considerare che è già filtrato leggendo solo i pacchetti mongo--- serve solo per specificare quale applicazione ascoltare
if [[ $# -gt 2 ]] ; then 
	i=2
	condizione=""
	list=${@:3:$(($#-2))}
	echo $list
	for container_ip in $list; do
		#passo direttamente gli ip perchè in questo caso non è detto che siano ancora in esecuzione
		echo "ip dell'applicazione $container_ip"
		i=$((i+1))
		if [[ $i -eq $# ]] ; then
			condizione="$condizione ip.addr==$container_ip"
		else
			condizione="$condizione ip.addr==$container_ip or"
		fi
	done
	echo $condizione
	elements=$(tshark -r $1 -T fields -e mongo.element.name -e mongo.opcode -e mongo.request_id -E separator=';' -Y "$condizione")
else
	elements=$(tshark -r $1  -T fields -e mongo.element.name -e mongo.opcode -e mongo.request_id -E separator=';')
fi
#echo $elements
echo "Split..."
for element in $elements
do
	#echo $element
	op=${element%%;*}
	op=${op%%,*}
	codeop=$(grep -oP '(?<=;).*?(?=;)' <<< "$element")
	if [ ! -z "$op" ]; then
		echo "codice operazione = $codeop"
		echo "operazione = $op"
	fi
	if [ ! -z "$op" ] && ( [ "$codeop" == "2004" ] || [ "$codeop" == "2013" ] ); then
		seqnum=${element##*;}
		tshark -r $1 -w $2/operation-$count_op-$op.cap -Y "mongo.request_id==$seqnum"
		count_op=$((count_op+1))
	fi
done
echo "Done!"
