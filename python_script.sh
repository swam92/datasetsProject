#!/bin/bash

for i in *.csv
do
    echo Started new CSV
    python dataRead.py $i >> result$i.out;
    mv result$i.out ../results
    echo Finished new CSV 
done