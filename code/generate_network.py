#!/usr/bin/python

import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist
import networkx as nx
import matplotlib as mpl; mpl.use('pdf')
import matplotlib.pyplot as plt
from itertools import combinations as itercom
import argparse

one_liner='generate bacterial gene networks using amino acid sequence similarity'
parser = argparse.ArgumentParser(description=one_liner)
parser.add_argument('-k','--kmer-length', help='length of AA kmers to use', required=True)
parser.add_argument('-t','--threshold', help='distance cutoff for drawing an edge', required=True)
parser.add_argument('-v','--verbose', help='enable print statements', action='store_true')
args = vars(parser.parse_args())

if args['verbose']:
    print "running for k={0}, threshold={1}".format(args['kmer_length'], args['threshold'])

def pair_dist(pair): 
    return float(pdist(np.vstack(pair), 'euclidean'))

gene_list = list(pd.read_csv('../data/gene_list.txt', index_col=0, header=0).index)
gene_abundance = np.array(pd.read_csv('../data/abundances.txt', index_col=0, header=0))
gene_length = np.array(pd.read_csv("../data/gene_length.csv", index_col=0, header=0))
df = pd.read_csv("../sakellarios/kmer_proportions_{0}.tsv".format(args['kmer_length']), 
                    sep='\t', index_col=0, header=0).T

g = nx.Graph()
total_pairs_strings = itercom(df.T, 2)

for gene in df.index: 
    g.add_node(gene)

for pair_string in total_pairs_strings:
    gene_pair_arrays = (df.ix[pair_string[0]], df.ix[pair_string[1]])
    distance = pair_dist(gene_pair_arrays)
    if distance < float(args['threshold']):
        g.add_edge(pair_string[0], pair_string[1])

positions = nx.spring_layout(g)
plt.axis('off')
nx.draw_networkx_nodes(g, pos=positions, alpha=0.5, nodelist=gene_list, 
        node_color=np.log(gene_abundance), node_size=gene_length/3, cmap=plt.cm.seismic)
nx.draw_networkx_edges(g, pos=positions, alpha=0.2)
nx.draw_networkx_labels(g, pos=positions, font_size=6)
plt.savefig("../figures/kmer_{0}_{1}.pdf".format(args['kmer_length'], args['threshold']))

if args['verbose']:
    print "done"