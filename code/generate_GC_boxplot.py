from glob import glob
from Bio.SeqUtils import GC
from Bio import SeqIO
from collections import defaultdict
import pandas as pd
import numpy as np
import matplotlib as mpl; mpl.use('pdf')
import matplotlib.pyplot as plt

GC_dict = defaultdict(dict)
abundances = open("../data/abundances.txt", "r")
abundance_pairs = [(line.rstrip().split(',')) for line in abundances.readlines()]  # turns rows into lists
del abundance_pairs[0]                                  # deletes column labels: gene,fold

for file in glob("../fasta_sequences/processed/*.fasta"):  # each fasta file in the folder accessed
                                                        ## file = "fasta_sequences/processed/adhE.fasta"
    gene_name = file.split('/')[-1].split('.')[0]       # generates gene_name from filename
    seq_generator = SeqIO.parse(file, "fasta")          # generator object for sequence parser
    seq_record = seq_generator.next()                   # generator object
    GC_content = GC(seq_record.seq)                     # generates GC_content for sequence
    GC_dict[gene_name] = [GC_content]                   # creates gene_name (key) in GC_dict and assign GC_content list(value) 
    
for abundance_pair in abundance_pairs:                  # for each pair
    for key,value in GC_dict.items():                   # for each item in the dict
        if abundance_pair[0] == key:                    # if the gene name is same
            value.append(abundance_pair[1])             # group the abundance to the GC value

up_reg = {}; down_reg = {}
for key,value in GC_dict.items():                       # determines if up reg or down reg
    #print type(value[0]), type(value[1])               # value[0] is float, value[1] is str <- needs to be converted
    if float(value[1]) > 1.0:
        up_reg[key] = value[0]
    if float(value[1]) < 1.0:
        down_reg[key] = value[0]

all_g = {}
for key, value in GC_dict.items():
    all_g[key] = value[0]

all_g = pd.Series(all_g)
up = pd.Series(up_reg)
down = pd.Series(down_reg)
data = [all_g, up, down]
#xlabels = ['all','up','down']

plt.figure()
plt.boxplot(data)
plt.xticks( range(1,4), ('All Genes', 'Up-Regulated', 'Down-Regulated') )
plt.ylabel("GC Percentage")
plt.title("GC Content")
plt.show()
plt.savefig("../figures/GC_boxplot.pdf")

######
## if there was a large salmonella.fasta file with  ALL genes

# seq_generator = SeqIO.parse("salmonella.fasta", "fasta")
# for seq_record in seq_generator:
#   GC_list[gene_name] = GC(seq_record.seq)
