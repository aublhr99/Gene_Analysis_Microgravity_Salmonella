import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist
import networkx as nx
import matplotlib as mpl; mpl.use('pdf')
import matplotlib.pyplot as plt
from itertools import combinations as itercom

print "running"
def pair_dist(pair):
    return float(pdist(np.vstack(pair), 'euclidean'))

gene_list = list(pd.read_csv('gene_list.txt', index_col=0, header=0).index)
gene_abundance = np.array(pd.read_csv("abundances.txt", index_col=0, header=0))
df = pd.read_csv("sakellarios/kmer_proportions_3.tsv", sep='\t', index_col=0, header=0) 
df = df.T
gene_length = np.array(pd.read_csv("gene_length.csv", index_col=0, header=0))

threshold = 0.008
for AA_to_include in df.columns:

    total_pairs_strings = list(itercom(df.T, 2))
    #for each in total_pairs_strings: 
    #    print each
    
    g = nx.Graph()

    for gene in df.index:
        g.add_node(gene)

    for pair_string in total_pairs_strings:
        gene_pair_arrays = (df.ix[pair_string[0], AA_to_include], df.ix[pair_string[1], AA_to_include])
        distance = pair_dist(gene_pair_arrays)
        if distance > threshold:
            g.add_edge(pair_string[0], pair_string[1])
        #print "distance", distance, pair_string[0], pair_string[1]
        
    positions = nx.spring_layout(g) ## don't forget the k=float argument here
    plt.axis('off')
    nx.draw_networkx_nodes(g, pos=positions,alpha=0.7, nodelist=gene_list, node_color=np.log(1+gene_abundance), node_size= (np.log(gene_length)) ** 2.5, cmap=plt.cm.seismic)
    nx.draw_networkx_labels(g, pos=positions, font_size=6)
    nx.draw_networkx_edges(g, pos=positions, alpha=0.2)
    plt.savefig("test_figures/combined/network_{0}_{1}.pdf".format(''.join(AA_to_include), threshold))
    plt.clf()
    print "done"        
