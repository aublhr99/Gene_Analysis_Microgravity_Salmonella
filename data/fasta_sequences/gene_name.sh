
#!/usr/bin

for file in processed/*.fasta; do
    gene=`echo $file | cut -d . -f1 | cut -d / -f2`
    echo $file
    sed -i 1s/".*"/'>'$gene/g $file 
done


# WARNING: -- only RUN from RUN function, alt+f5
# otherwise will replace ALL first lines in EVERY file
# ../gene_name.sh