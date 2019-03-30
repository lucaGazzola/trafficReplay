
for i in $(seq $1 $2); 
do
	./union_scripts.sh Test$i/SplitRest/Notification_Service/
	./union_scripts.sh Test$i/SplitRest/Statistics_Service/
	./union_scripts.sh Test$i/SplitRest/Account_Service/
done
