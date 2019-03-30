#!/bin/bash
for dirname in $( find * -type d -name 'Versione*' ); do
	sudo chmod 777 $dirname/Test*
done
