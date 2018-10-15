#./readop.sh MongoTrafficReplay/reports/Test/
#!/bin/bash
cd $1
for filename in $( ls -v *.json ); do
	echo "inizio esecuzione test..."
	name=${filename%%.json*}
	addr=$ADD_VAR
	python3 ../../../readoperations.py $filename $addr
	#python3 ../../../servermongo.py $filename 
	echo "termina esecuzione test..."
done

