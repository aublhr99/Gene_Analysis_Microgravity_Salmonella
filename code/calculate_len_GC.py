from collections import defaultdict
from glob import glob
from Bio.SeqUtils import GC ; from Bio import SeqIO


GC_dict = defaultdict(dict)
for file in glob("../fasta_sequences/processed/*.fasta"):   # each fasta file in the folder accessed
    ## file = "fasta_sequences/processed/adhE.fasta"
    gene_name = file.split('/')[-1].split('.')[0]           # generates gene_name from filename
    seq_generator = SeqIO.parse(file, "fasta")              # generator object for sequence parser
    seq_record = seq_generator.next()                       # generator object
    seq_length = len(seq_record.seq)                        #
    GC_content = GC(seq_record.seq)                         # generates GC_content for sequence
    GC_dict[gene_name] = GC_content                         # creates gene_name (key) in GC_dict and assign GC_content list(value) 
    print "name", gene_name, "length", seq_length
    
for key, value in GC_dict.items():
    print "name",key,"GC",value