from glob import glob
from Bio import SeqIO
import pandas as pd
import time
start = time.time()

dataset = {}
for file in glob("fasta_sequences/processed/*.fasta"):
    gene_name = file.split('/')[-1].split('.')[0]
    seq_generator = SeqIO.parse(file, "fasta")
    seq_record = seq_generator.next()
    dataset[gene_name] = seq_record.seq

hit_counts = {}
nucleotides = ['A','C','G','T']
for pos1 in nucleotides:
    for pos2 in nucleotides:
        for pos3 in nucleotides:
            for pos4 in nucleotides:
                for pos5 in nucleotides:
                    for pos6 in nucleotides:
                        for pos7 in nucleotides:
                            for pos8 in nucleotides:
                                for pos9 in nucleotides:
                                    for pos10 in nucleotides:
                                        num_hits = 0
                                        motif = pos1 + pos2 + pos3 + pos4 + pos5 + pos6 + pos7 + pos8 + pos9 + pos10
                                        for gene, sequence in dataset.items():
                                            if str(sequence).find(motif) > -1:
                                                num_hits += 1
                                                print gene, motif
                                        hit_counts[motif] = num_hits

for key, value in hit_counts.items():
    #print key, value
    if value > 1:   #//any hit_count 0 is useless, any hit_count 1 means only in one, insignificant
        print key, value
    #if value > 30:
    #    print "present in", value, key
        
end = time.time()
print "Required {0} sec".format(end-start)








## observations:

## 'CAGG' is present in all 55.
## length 7 motif takes 05 sec.
## length 8 motif takes 20 sec.
## length 9 motif takes 85 sec.

#present in GAAAA 46                                                                                                                                                                                        
#present in CTGGA 48                                                                                                                                                                                        
#present in CTGGC 46                                                                                                                                                                                        
#present in AAAAA 47                                                                                                                                                                                        
#present in TGGCG 46                                                                                                                                                                                        
#present in GCAGG 46                                                                                                                                                                                        
#present in GGCGC 49 

#present in TGGCGC 31                                                                                                                                                                                       
#present in CTGGCG 35                                                                                                                                                                                       
#present in GCGCTG 36                                                                                                                                                                                       
#present in GCTGAA 33                                                                                                                                                                                       
#present in GAAAAA 31 

