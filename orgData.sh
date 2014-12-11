#! /bin/bash 

for i in {1..20}
do 
    cur_dir="data$i"
    mkdir $cur_dir
    cp python_script.sh $cur_dir
    cp dataRead.py $cur_dir
done


	