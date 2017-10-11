import numpy as np
import pandas as pd
import matplotlib; matplotlib.use('pdf')
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist

df = pd.read_csv("../sakellarios/kmer_proportions_4.tsv", index_col=0, header=0, sep = '\t')
distances = pdist(df.T, "euclidean")

plt.hist(distances, color='pink', bins=200)
plt.title('Histogram of Pairwise Gene Distances Using Amino Acids', fontsize=12)
plt.xlabel('Euclidean Distance')
plt.ylabel('Frequency')
plt.savefig('../figures/amino_acid_hist_4.pdf')