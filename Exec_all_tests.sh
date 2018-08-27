#!/bin/bash

cd $1
for filename in $( ls -v *.py ); do
	python3 $filename
done
