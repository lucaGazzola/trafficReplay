# Creates file to set the response of auth-service to the service under test
# Argument: json file to read (corresponding to the .sh script to set the response)

if [[ $# -lt 1 ]] ; then 
	echo 'missing args ---> ./union_scripts.sh <namefile>'
	exit 1
fi

if [ -f "$1.sh" ]; then
	rm -f "$1.sh"
fi

echo -ne "curl -i -X POST -H 'Content-Type: application/json' http://\$1:2525/imposters --data @$1.json" > $1.sh
#filename=$1.json
#cat $filename >> $1.sh
#echo "'" >> $1.sh

