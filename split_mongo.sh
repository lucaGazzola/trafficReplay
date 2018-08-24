#usage: ./split_mongo.sh pcapfile.pcap savedir
if [ ! -d "$2" ]; 
then 
	mkdir $2; 
fi
if [ ! -d "$2/Operation" ]; 
then 
	mkdir "$2/Operation"; 
fi
#if [ ! -d "$2/Reply" ]; 
#then 
#	mkdir "$2/Reply"; 
#fi
count_insert=0
count_delete=0
count_update=0
count_others=0
count_op=0
count_find=0
#count_reply=0
elements=$(tshark -r $1  -T fields -e mongo.element.name -e mongo.opcode -e mongo.request_id -E separator=';')
#echo $elements
for element in $elements
do
	echo $element
	op=${element%%;*}
	op=${op%%,*}
	codeop=$(grep -oP '(?<=;).*?(?=;)' <<< "$element")
	#echo "codeop="$codeop
	if [ -z "$op" ] || [ "$codeop" != "2004" ]; then #|| [ "$op" == ";;" ]	
	    	echo "op is empty or not query operation"
		#Nel caso dovessi considerare anche le reply <------------------------------------------
		#if [ "$codeop" == "1" ]; then
		#	tshark -r $1 -w $2/Reply/reply-$op-$count_reply.cap -Y "mongo.request_id==$seqnum"
		#	count_reply=$((count_reply+1))
		#fi
	else
		seqnum=${element##*;}
		echo "----------------------------------------------------------"
		echo $(($seqnum))
		echo "seqnum="$seqnum
		echo "op="$op
		case "$op" in
			insert)
				tshark -r $1 -w $2/insert-$count_insert.cap -Y "mongo.request_id==$seqnum"
				#questo nel caso in cui si volesse l'elenco delle operazioni in ordine di esecuzione originale
				tshark -r $1 -w $2/Operation/operation-$count_op.cap -Y "mongo.request_id==$seqnum"
				count_insert=$((count_insert+1))
				count_op=$((count_op+1))
		    		;;
			update)
				tshark -r $1 -w $2/update-$count_update.cap -Y "mongo.request_id==$seqnum"
				tshark -r $1 -w $2/Operation/operation-$count_op.cap -Y "mongo.request_id==$seqnum"
				count_update=$((count_update+1))
				count_op=$((count_op+1))
		    		;;
			delete)
				tshark -r $1 -w $2/delete-$count_delete.cap -Y "mongo.request_id==$seqnum"
				tshark -r $1 -w $2/Operation/operation-$count_op.cap -Y "mongo.request_id==$seqnum"
				count_delete=$((count_delete+1))
				count_op=$((count_op+1))
		    		;;
			find)
				tshark -r $1 -w $2/find-$count_find.cap -Y "mongo.request_id==$seqnum"
				tshark -r $1 -w $2/Operation/operation-$count_op.cap -Y "mongo.request_id==$seqnum"
				count_find=$((count_find+1))
				count_op=$((count_op+1))
		   		;;
			*)
				echo "others="$op
				tshark -r $1 -w $2/others-$count_others.cap -Y "mongo.request_id==$seqnum"
				#nel caso volessi considerare anche le operazioni di questo tipo devo aggiungerle al conteggio delle op
				#tshark -r $1 -w $2/operation-$count_op.cap -Y "mongo.request_id==$seqnum" <-----------------------
				#tshark -r $1 -w $2/$op-$count_others.cap -Y "mongo.request_id==$seqnum"
				count_others=$((count_others+1))
		    		;;
		esac
		echo "----------------------------------------------------------"
	fi
done
