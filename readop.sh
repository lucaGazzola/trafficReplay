#./readop.sh MongoTrafficReplay/reports/Test/
#!/bin/bash
cd $1
for filename in $( ls -v *.json ); do
	echo "inizio esecuzione test..."
	name=${filename%%.json*}
	python3 /home/luca/TesiGit/trafficReplay/readoperations.py $filename mongodb://localhost:37379&
	python3 /home/luca/TesiGit/trafficReplay/servermongo.py $filename 
	echo "termina esecuzione test..."
done

