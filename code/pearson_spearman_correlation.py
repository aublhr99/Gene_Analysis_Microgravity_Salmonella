from scipy.stats import pearsonr 
from scipy.stats import spearmanr
import numpy as np
import pandas as pd

df = pd.read_csv('../data/gene_length.csv', header=0)

df2 = pd.read_csv('../data/abundances.txt', header=0)

print 'Pearson correlation =', pearsonr(np.array(df['length']), np.array(np.log(df2['fold'])))

print 'Spearman correlation =', spearmanr(np.array(df['length']), np.array(np.log(df2['fold'])))


#Pearson correlation = (0.62282438052262401, 2.2989250620792021e-07)                                         
#Spearman correlation = (0.62649509061664943, 1.8593446834654803e-07) 