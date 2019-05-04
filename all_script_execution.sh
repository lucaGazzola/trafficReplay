#!/bin/bash

for i in $(seq $1 $2); 
do
	docker rm -f $(docker ps -a -q)

	docker rmi -f $(docker images -q)

	yes | docker system prune

	cd Versione$i\_*/

	yes | cp -a  ../Scripts/.  .

	cd ..
done
./automatic_create_capture.sh $1 $2 
./automatic_permission.sh
./automatic_create_script.sh $1 $2
./automatic_Test.sh $1 $2
