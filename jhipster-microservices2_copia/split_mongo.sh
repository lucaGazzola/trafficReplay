#usage: ./split_mongo.sh pcapfile.pcap savedir
if [ ! -d "$2" ]; 
then 
	mkdir $2; 
fi
count_op=0
elements=$(tshark -r $1  -T fields -e mongo.element.name -e mongo.opcode -e mongo.request_id -E separator=';')
#echo $elements
echo "Split..."
for element in $elements
do
	op=${element%%;*}
	op=${op%%,*}
	codeop=$(grep -oP '(?<=;).*?(?=;)' <<< "$element")
	if [ -z "$op" ] || [ "$codeop" != "2004" ]; then #|| [ "$op" == ";;" ]	
		caso=1
	else
		seqnum=${element##*;}
		tshark -r $1 -w $2/operation-$count_op-$op.cap -Y "mongo.request_id==$seqnum"
		count_op=$((count_op+1))
	fi
done
echo "Done!"
