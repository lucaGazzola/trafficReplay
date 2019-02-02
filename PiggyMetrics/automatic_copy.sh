
numero_test=1
for i in $(seq $1 $2); 
do
	if [ -f Test_Completo$i/SplitRest/$3_Service/TestComplete/test_complete.py ]; then
		if [ ! -d "TestSuite_$3" ]; 
		then 
			mkdir -p "TestSuite_$3"
		fi
		cd TestSuite_$3
		if [ ! -d "Test$numero_test" ]; 
		then 
			mkdir -p "Test$numero_test"
			cd Test$numero_test
			mkdir -p "reports$numero_test"
			cd ..
		fi
		cd ..
		service=$(echo $3 | awk '{print tolower($0)}')
		name=$(find Test_Completo$i/SplitMongo/ -maxdepth 1 -type d -name "*$service*" -print -quit)
		yes | cp -a  $name/reports/. TestSuite_$3/Test$numero_test/reports$numero_test/
		yes | cp Test_Completo$i/SplitRest/$3_Service/TestComplete/test_complete.py TestSuite_$3/Test$numero_test/
		numero_test=$((numero_test+1))
	fi
done
