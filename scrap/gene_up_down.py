from glob import glob
from os.path import join
from shutil import shutil
#import subprocess
#import shlex
import subprocess
#subprocess.call("cat")

abundances = open("abundances.txt", "r")
abundance_pairs = [(line.rstrip().split(',')) for line in abundances.readlines()]  # turns rows into lists
del abundance_pairs[0]

fire = []
for pair in abundance_pairs:
    if float(pair[1]) > 1:
        src = join('fasta_sequences/processed', str(pair[0]), '.fasta')
        subprocess.call("cat src >> up_regulated.fasta")
    else:
        src = join('fasta_sequences/processed', str(pair[0]), '.fasta')
        subprocess.call("cat src >> down_regulated.fasta")
dst = "fasta_sequences/processed/up_regulated/"


for src in fire:
    dst = join("fasta_sequences/processed/up_regulated/",'src')
    shutil.move(src, dst)