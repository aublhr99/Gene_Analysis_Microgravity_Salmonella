#!/bin/sh

for file in processed/*.fasta; do
    gene=`echo $file | cut -d . -f1 | cut -d / -f2`
    foldchange=`grep $gene ../abundances.txt | cut -d , -f2 | bc -l`
    if [ $foldchange -ge 1.0 ]; then
        cat $file >> up_regulated.fasta
    else
        #cat $file >> down_regulated.fasta
        echo hello
    fi
done


#use a python file to check if greater or less than,
#use a bash file to move the file