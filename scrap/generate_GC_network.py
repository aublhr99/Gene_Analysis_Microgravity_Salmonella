from glob import glob
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib as mpl; mpl.use('pdf')
import matplotlib.pyplot as plt
from Bio.SeqUtils import GC 
from Bio import SeqIO
from collections import defaultdict
from itertools import combinations as itercom
from scipy.spatial.distance import pdist

GC_dict = {}
abundances = open("abundances.txt", "r")
abundance_pairs = [(line.rstrip().split(',')) for line in abundances.readlines()]  # turns rows into lists
del abundance_pairs[0]                              # deletes column labels: gene,fold

for file in glob("fasta_sequences/processed/*.fasta"):  # each fasta file in the folder accessed
    gene_name = file.split('/')[-1].split('.')[0]   # generates gene_name from filename
    seq_generator = SeqIO.parse(file, "fasta")      # generator object for sequence parser
    seq_record = seq_generator.next()               # generator object
    GC_content = GC(seq_record.seq)                 # generates GC_content for sequence
    GC_dict[gene_name] = [GC_content]               # creates gene_name (key) in GC_dict and assign GC_content list(value) 

for abundance_pair in abundance_pairs:              # for each pair
    for key,value in GC_dict.items():               # for each item in the dict
        if abundance_pair[0] == key:                # if the gene name is same
            value.append(abundance_pair[1])         # group the abundance to the GC value

up_reg = {} ; down_reg = {} ; all_g = {}

for key,value in GC_dict.items():                   # determines if up reg or down reg
    # print type(value[0]), type(value[1])          # value[0] is float, value[1] is str <- needs to be converted
    if float(value[1]) > 1.0:
        up_reg[key] = value[0]
    if float(value[1]) < 1.0:
        down_reg[key] = value[0]
    all_g[key] = value[0]

abundances_and_GC = ([value for key,value in GC_dict.items()])
gene_list = [key for key, value in GC_dict.items()]


g = nx.Graph()
g.add_nodes_from(gene_list)
threshold = 57
for key, value in all_g.items():
    g.add_node(key)
    if value > threshold:
        g.add_edge()
        
    
#specific_array = np.array(pd.read_csv("abundances.txt", index_col=0, header=0)["fold"])


pos = nx.spring_layout(g)
nx.draw(g, pos) #nodelist=gene_list,cmap=plt.cm.Reds
plt.savefig("network_test.pdf")