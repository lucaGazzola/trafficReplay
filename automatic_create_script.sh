#!/bin/bash
export CONFIG_SERVICE_PASSWORD="conf_serv"
export NOTIFICATION_SERVICE_PASSWORD="not_serv"
export STATISTICS_SERVICE_PASSWORD="stat_serv"
export ACCOUNT_SERVICE_PASSWORD="acc_serv"
export MONGODB_PASSWORD="mongo"


for i in $(seq $1 $2); 
do	
	
	unset IFS
	docker rm -f $(docker ps -a -q)

	docker rmi -f $(docker images -q)

	yes | docker system prune

	cd Versione$i\_*/
	
	if [ -z "$( find * -type d -name 'Test*' )" ]; then
		echo "nessun test per questa cartella"
		exit 1
	fi	
	echo $PWD
	unset name
	ls -d Test* -v
	for name in $( ls -d Test* -v ); do
		echo "-----------------------"
		echo $name
		echo "-----------------------"
		./split.sh $name/interaction.pcap $name/SplitRest	
		./split_mongo.sh $name/interaction.pcap $name/SplitMongo
	done
	./CreateTestPy.sh 1 25
	./automatic_union.sh 1 25
	
	cd piggymetrics

	mvn package -DskipTests
	
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d &
	
	ipstat=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps | grep piggymetrics_statistics-service | awk '{print $1}'))
	count=1



	while [ -z "$ipstat" ]
	do
		count=$((count+1))
		if (( $count > 50 )); then
			ipstat="non_connesso"
		else
	      		sleep 20
			ipstat=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps | grep piggymetrics_statistics-service | awk '{print $1}'))
			count=$((count+1))
		fi
	done



	
	ipnot=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps | grep piggymetrics_notification-service | awk '{print $1}'))
	count=1



	while [ -z "$ipnot" ]
	do
		if (( $count > 50 )); then
			ipnot="non_connesso"
		else
		      	sleep 20
			ipnot=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps | grep piggymetrics_notification-service | awk '{print $1}'))
			count=$((count+1))
		fi
	done




	ipacc=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps | grep piggymetrics_account-service | awk '{print $1}'))
	count=1



	while [ -z "$ipacc" ]
	do
		if (( $count > 50 )); then
			ipacc="non_connesso"
		else
		      	sleep 20
			ipacc=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps | grep piggymetrics_account-service | awk '{print $1}'))
			count=$((count+1))
		fi
	done



	ipauth=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps | grep piggymetrics_auth-service | awk '{print $1}'))
	count=1

	
	while [ -z "$ipauth" ]
	do
		if (( $count > 50 )); then
			ipauth="non_connesso"
		else
		      	sleep 20
			ipauth=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps | grep piggymetrics_auth-service | awk '{print $1}'))
			count=$((count+1))
		fi
	done


	if [ "$ipstat" != "non_connesso" ]; then
		printf 'try to connect...'
		until [ $(curl -s -o /dev/null -w "%{http_code}" $ipstat:7000) != "000" ]; do
		    printf '.'
		    sleep 20
		done
		printf "connect to statistics service \n"
	fi


	if [ "$ipacc" != "non_connesso" ]; then
		printf 'try to connect...'
		until [ $(curl -s -o /dev/null -w "%{http_code}" $ipacc:6000) != "000" ]; do
		    printf '.'
		    sleep 20
		done
		printf "connect to account service \n"
	fi


	if [ "$ipnot" != "non_connesso" ]; then
		printf 'try to connect...'
		until [ $(curl -s -o /dev/null -w "%{http_code}" $ipnot:8000) != "000" ]; do
		    printf '.'
		    sleep 20
		done
		printf "connect to notification service \n"
	fi


	if [ "$ipauth" != "non_connesso" ]; then
		printf 'try to connect...'
		until [ $(curl -s -o /dev/null -w "%{http_code}" $ipauth:5000) != "000" ]; do
		    printf '.'
		    sleep 20
		done
		printf "connect to auth service \n"
	fi
	
	sleep 10
	cd ..
	unset name
	for name in  $( ls -d Test* -v ); do
		echo "-----------------------"
		echo $name
		echo "-----------------------"
		./generate_test_replay.sh SplitMongo $name
	done

	cd piggymetrics

	docker-compose stop
	echo $PWD
	cd ..
	unset name
	#for dirname in $( find * -type d -maxdepth 1 -name 'Test*'  | sort -z  ); do
	for name in  $( ls -d Test* -v ); do
		echo "-----------------------"
		echo $name
		echo "-----------------------"
		while read mongo_cont; do
			IFS=';'
			read -ra mongo_info <<< "$mongo_cont"
			if [[ ${mongo_info[0]} == *"piggymetrics_notification-service"* ]]; then
				old_ip_not=${mongo_info[1]}
			fi
			if [[ ${mongo_info[0]} == *"piggymetrics_statistics-service"* ]]; then
				old_ip_stat=${mongo_info[1]}
			fi
			if [[ ${mongo_info[0]} == *"piggymetrics_auth-service"* ]]; then
				old_ip_auth=${mongo_info[1]}
			fi
			if [[ ${mongo_info[0]} == *"piggymetrics_account-service"* ]]; then
				old_ip_acc=${mongo_info[1]}
			fi
		done < "$name/name_ip_mongo.txt"
		echo $old_ip_auth $old_ip_acc
		echo $old_ip_auth $old_ip_stat
		echo $old_ip_auth $old_ip_not
		echo $name
		python3 extract_http_data.py $name/interaction.pcap $old_ip_auth $old_ip_acc auth-mock-response-acc.json
		python3 extract_http_data.py $name/interaction.pcap $old_ip_auth $old_ip_stat auth-mock-response-stat.json
		python3 extract_http_data.py $name/interaction.pcap $old_ip_auth $old_ip_not auth-mock-response-not.json
	done
	./create_auth_resp.sh auth-mock-response-acc
	./create_auth_resp.sh auth-mock-response-stat
	./create_auth_resp.sh auth-mock-response-not
	chmod +x auth-mock-response-acc.sh
	chmod +x auth-mock-response-stat.sh
	chmod +x auth-mock-response-not.sh
	./automatic_copy.sh 1 25 Account
	./automatic_copy.sh 1 25 Statistics
	./automatic_copy.sh 1 25 Notification
	cd ..
	unset IFS
done
