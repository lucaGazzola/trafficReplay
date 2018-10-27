#usage: ./split_mongo.sh pcapfile.pcap savedir
if [ ! -d "$2" ]; 
then 
	mkdir $2; 
fi
count_op=0
elements=$(tshark -r $1  -T fields -e mongo.element.name -e mongo.opcode -e mongo.request_id -E separator=';')
#echo $elements
for element in $elements
do
	#echo $element
	op=${element%%;*}
	op=${op%%,*}
	codeop=$(grep -oP '(?<=;).*?(?=;)' <<< "$element")
	#echo "codeop="$codeop
	if [ -z "$op" ] || [ "$codeop" != "2004" ]; then #|| [ "$op" == ";;" ]	
		caso=1
	    	#echo "op is empty or not query operation"
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
		tshark -r $1 -w $2/operation-$count_op-$op.cap -Y "mongo.request_id==$seqnum"
		count_op=$((count_op+1))
		echo "----------------------------------------------------------"
	fi
done
