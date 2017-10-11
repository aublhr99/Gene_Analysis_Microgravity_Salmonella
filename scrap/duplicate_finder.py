
from glob import glob
f=open('gene_list.txt')

for file in glob("processed/*.fasta"): ## file = "fasta_sequences/processed/*.fasta"
    gene_name = file.split('/')[-1].split('.')[0]
    for gene in f.readlines():
        print 'gene', gene
        if gene_name == gene:
            print gene_name, "found"
        if gene_name != gene:
            print gene_name, "this"
