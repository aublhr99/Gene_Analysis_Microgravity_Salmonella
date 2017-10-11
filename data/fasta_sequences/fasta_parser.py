

#from Bio.SeqUtils import GC
from Bio import SeqIO

filename = 'processed/dps.fasta'

for seq_record in SeqIO.parse(filename, 'fasta'):
    #print seq_record.id #sequence section
    print len(seq_record.seq) #sequence one-line
    #print GC(seq_record.seq) #GC percentage
