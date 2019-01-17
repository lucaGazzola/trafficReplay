#Per unire tutti gli script python di test in un unico test
#./union_scripts TestDir SplitRest

if [[ $# -lt 2 ]] ; then 
	echo 'missing args ---> ./split_mongo.sh <TestDir> <SplitRest>'
	exit 1
fi

cd $1

if [ -f "test_complete.py" ]; then
	rm -f "test_complete.py"
fi

echo "import requests" > test_complete.py
echo "import json" >> test_complete.py
echo "import time" >> test_complete.py
echo "import re" >> test_complete.py
echo "import sys" >> test_complete.py
echo "from bson.json_util import loads" >> test_complete.py
echo "import os.path" >> test_complete.py
echo "" >> test_complete.py
echo "" >> test_complete.py

cat ./$2/*.py >> test_complete.py
