import pandas        as pd
import numpy         as np
import networkx      as nx
import scipy.spatial as sps
import matplotlib    as mpl; mpl.use('pdf')
import matplotlib.pyplot as plt
from itertools import combinations as itercom

def pair_distance(pair):
    distance = np.abs(pair[0][1] - pair [1][1])
    return distance

df = pd.read_csv("../data/abundances.txt", header=0)
genes = df['gene']
folds = []

for fold in df['fold']: folds.append(float(fold))

named_genes = zip(genes,folds)
named_gene_pairs = itercom(named_genes, 2)

distances = []
for pair in named_gene_pairs:
    dist = pair_distance(pair)
    distances.append(dist)

plt.hist(distances, color='red', bins=100)
plt.title('Difference of Abundances for Each Pair of Genes',fontsize=12)
plt.xlabel('distance value'); plt.ylabel('instances')
plt.savefig('../figures/abundance_hist.pdf')