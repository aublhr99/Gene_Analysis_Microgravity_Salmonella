import numpy as np
import pandas as pd
from itertools import product
from Bio import SeqIO

amino_acids = list("ARNDCQEGHILKMFPSTWYV")
possible_kmers = [''.join(x) for x in list(product(amino_acids, repeat=1))]

gene_names = []
with open('AA_combined.fasta') as handle:
    for record in SeqIO.parse(handle, 'fasta'):
        gene_names.append(record.id)

feature_space = pd.DataFrame(np.zeros((len(possible_kmers),len(gene_names))), 
                                index=possible_kmers, columns=gene_names)

with open('AA_combined.fasta') as handle:
    for record in SeqIO.parse(handle, 'fasta'):
        g = record.id
        seq = str(record.seq)
        for kmer in feature_space.index:
            feature_space[g][kmer] = seq.count(kmer)
            
feature_space = feature_space / feature_space.sum(axis=0)
feature_space.to_csv('kmer_proportions_1.tsv', index=True, header=True, sep='\t')