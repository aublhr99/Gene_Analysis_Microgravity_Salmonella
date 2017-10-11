import shutil
from glob import glob

abundances = open("abundances.txt", "r")
abundance_pairs = [(line.rstrip().split(',')) for line in abundances.readlines()]  # turns rows into lists
del abundance_pairs[0]

for file in glob("fasta_sequences/processed/*.fasta"):
    for pair in abundance_pairs:
        if float(pair[1]) > 1:
            if ('fasta_sequences/processed' + str(pair[0]) + '.fasta')  == file:
                shutil.move('fasta_sequences/processed' + str(pair[0]) + '.fasta', 'fasta_sequences/up_regulated' + str(pair[0]) + '.fasta')
        if float(pair[1]) < 1:
            if ('fasta_sequences/processed' + str(pair[0]) + '.fasta')  == file:
                shutil.move('fasta_sequences/processed' + str(pair[0]) + '.fasta', 'fasta_sequences/down_regulated' + str(pair[0]) + '.fasta')