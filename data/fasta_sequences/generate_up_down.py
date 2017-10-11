
from glob import glob
import subprocess

data = open("../abundances.txt", "r")
abundance_pairs = [(line.rstrip().split(',')) for line in data.readlines()]
del abundance_pairs[0]

for file in glob("processed/*.fasta"): ## file = "fasta_sequences/processed/*.fasta"
    gene_name = file.split('/')[-1].split('.')[0]
    for pair in abundance_pairs:
        if pair[0] == gene_name:
            if float(pair[1]) > 1:
                subprocess.Popen('cat ' + str(file) + '>> up_regulated.fasta', shell=True)
            else:
                subprocess.Popen('cat ' + str(file) + '>> down_regulated.fasta', shell=True)
    #for x in range(88):
        #for i, row in df.iterrows():
            #if gene_name == df.irow(x)['gene']:
                #if df.irow(x)['fold']  > 1:
                    #subprocess.Popen('cat ' + str(file) + '>> up_regulated.fasta', shell=True)
                #subprocess.call(["cat", file, ">>", "up_regulated.fasta"])
                #subprocess.call(["echo","done"])
                #else:
                    #subprocess.Popen('cat ' + str(file) + '>> down_regulated.fasta', shell=True)
                #subprocess.call(["cat", file, ">>", "down_regulated.fasta"])
                #subprocess.call(["echo","done"])
