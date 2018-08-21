#usage: ./split.sh pcapfile.pcap savedir
if [ -d "$2" ]; 
then 
	rm -Rf $2; 
fi
mkdir $2
count_insert=0
count_delete=0
count_update=0
count_others=0
elements=$(tshark -r $1 -T fields -e mongo.element.name -e mongo.request_id -E separator=',' | sort -n)
echo $elements
#for element in $(tshark -r $1 -T fields -e mongo.element.name | sort -n)
for element in $elements
do
	op=${element%%,*}
	if [ -z "$op" ]; then
	    echo "op is empty"
	else
		seqnum=${element##*,}
		case "$op" in
			insert)
				tshark -r $1 -w $2/insert-$count_insert.cap -Y "mongo.request_id==$seqnum"
				count_insert=$((count_insert+1))
		    		;;
			update)
				tshark -r $1 -w $2/update-$count_update.cap -Y "mongo.request_id==$seqnum"
				count_update=$((count_update+1))
		    		;;
			delete)
				tshark -r $1 -w $2/delete-$count_delete.cap -Y "mongo.request_id==$seqnum"
				count_delete=$((count_delete+1))
		    		;;
			*)
				tshark -r $1 -w $2/others-$count_others.cap -Y "mongo.request_id==$seqnum"
				#tshark -r $1 -w $2/$op-$count_others.cap -Y "mongo.request_id==$seqnum"
				count_others=$((count_others+1))
		    		;;
		esac
	fi
done
