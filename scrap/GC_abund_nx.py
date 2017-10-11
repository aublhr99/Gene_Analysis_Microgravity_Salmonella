from collections import defaultdict
from glob import glob
from Bio.SeqUtils import GC ; from Bio import SeqIO
import pandas as pd ; import numpy as np
from scipy.spatial.distance import pdist
import matplotlib as mpl; mpl.use('pdf')
import matplotlib.pyplot as plt
import networkx as nx

GC_dict = defaultdict(dict)

abundances = open("abundances.txt", "r")
abundance_pairs = [(line.rstrip().split(',')) for line in abundances.readlines()]  # turns rows into lists
del abundance_pairs[0]                                  # deletes column labels: gene,fold

for file in glob("fasta_sequences/processed/*.fasta"):  # each fasta file in the folder accessed
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

#all_g = {} ; #up_reg = {} ; #down_reg = {}

#for key,value in GC_dict.items():                      # determines if up reg or down reg
#    print type(value[0]), type(value[1])               # value[0] is float, value[1] is str <- needs to be converted
#    if float(value[1]) > 1.0: up_reg[key] = value[0]   # above one added to up
#    if float(value[1]) < 1.0: down_reg[key] = value[0] # below one added to down
#    all_g[key] = value[0]

#print GC_dict ; #print up_reg ; #print down_reg ; #print all_g     # debugger

#GC_dict_dataframe = pd.DataFrame(GC_dict.items())

abundances_and_GC = ([(key, value) for key,value in GC_dict.items()])

#all_g_series = pd.Series(all_g)
#up_series = pd.Series(up_reg)
#down_series = pd.Series(down_reg)
#data = [all_g, up, down]
for abundance_and_GC in abundances_and_GC:
    print abundance_and_GC
    
    
distances = pdist(abundances_and_GC, 'euclidean')
#for distance in distances : print distance

#g = nx.Graph()

threshold = 3