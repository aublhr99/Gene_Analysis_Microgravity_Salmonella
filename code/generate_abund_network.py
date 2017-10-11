import pandas        as pd
import numpy         as np
import networkx      as nx
import scipy.spatial as sps
import matplotlib    as mpl; mpl.use('pdf')
import matplotlib.pyplot as plt
from itertools import combinations as itercom

def pair_distance(pair):
    distance = ((pair[0][1] - pair [1][1])**2)
    return distance

df = pd.read_csv("abundances.txt", header=0)
genes = df['gene']
folds = []

for fold in df['fold']:
    folds.append(float(fold))

named_genes = zip(genes,folds)
named_gene_pairs = itercom(named_genes, 2)
threshold = 0.0005

g = nx.Graph()

for pair in named_gene_pairs:
    dist = pair_distance(pair)
    if dist < threshold:
        g.add_edge(pair[0][0], pair[1][0])


nx.spring_layout(g)
nx.draw(g)
plt.savefig("abundance_network_{0}.pdf".format(threshold))