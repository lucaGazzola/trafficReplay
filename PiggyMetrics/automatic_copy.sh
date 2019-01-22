
if [ -f $1/SplitRest/$3_Service/TestComplete/test_complete.py ]; then
	cd TestSuite_$3
	if [ ! -d $2 ]; 
	then 
		mkdir -p $2; 
	fi
	cd ..
	yes | cp $1/SplitRest/$3_Service/TestComplete/test_complete.py TestSuite_$3/$2/
else 
	echo "non presente nessun file di test"
fi
