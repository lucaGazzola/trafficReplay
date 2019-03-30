raw=1
for i in $(seq $1 $2); 
do
	id=$(head -"$raw" version_id.txt | tail -1)
	mkdir Versione$i\_$id
	echo $id
	cd Versione$i\_$id
	git clone https://github.com/sqshq/piggymetrics.git
	cd piggymetrics/
	git checkout $id
	cd ..
	cd ..
	raw=$((raw+1))
done
