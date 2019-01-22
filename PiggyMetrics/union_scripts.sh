#Per unire tutti gli script python di test in un unico test
#./union_scripts TestDir SplitRest

if [[ $# -lt 1 ]] ; then 
	echo 'missing args ---> ./union_scripts.sh <TestDir/SplitRest/AppRestDir>'
	exit 1
fi

cd $1

if [ -f "test_complete.py" ]; then
	rm -f "test_complete.py"
fi

if [ ! -d "TestComplete" ]; 
then 
	mkdir -p "TestComplete"; 
fi
echo $( ls -v *.py | wc -c )
if [ $( ls -v *.py | wc -c ) -ne 0 ]; then 
  	echo "import requests" > ./TestComplete/test_complete.py
	echo "import json" >> ./TestComplete/test_complete.py
	echo "import time" >> ./TestComplete/test_complete.py
	echo "import re" >> ./TestComplete/test_complete.py
	echo "import sys" >> ./TestComplete/test_complete.py
	echo "from bson.json_util import loads" >> ./TestComplete/test_complete.py
	echo "import os.path" >> ./TestComplete/test_complete.py
	echo "" >> ./TestComplete/test_complete.py
	echo "" >> ./TestComplete/test_complete.py
	for filename in $( ls -v *.py ); do
		cat $filename >> ./TestComplete/test_complete.py
	done
else
	echo "vuoto"
fi



