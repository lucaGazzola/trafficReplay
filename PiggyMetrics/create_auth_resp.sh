#Crea file per settare la risposta di auth-service  al servizio che stiamo testando
#L'argomento passato è il nome del file da leggere (json) che corrisponderà a quello er settare la risposta (sh)

if [[ $# -lt 1 ]] ; then 
	echo 'missing args ---> ./union_scripts.sh <namefile>'
	exit 1
fi

if [ -f "$1.sh" ]; then
	rm -f "$1.sh"
fi

echo -ne "curl -i -X POST -H 'Content-Type: application/json' http://\$1:2525/imposters --data '" > $1.sh
filename=$1.json
cat $filename >> $1.sh
echo "'" >> $1.sh

