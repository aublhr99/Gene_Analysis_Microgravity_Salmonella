from glob import glob

abundances = open("abundances.txt", "r")
abundance_pairs = [(line.rstrip().split(',')) for line in abundances.readlines()]  # turns rows into lists
del abundance_pairs[0]

f = open('up_reg.fasta', 'w')
z = open('down_reg.fasta', 'w')

dixie_cup = []
fire_cracker = []

for file in glob("fasta_sequences/processed/*.fasta"):
    for pair in abundance_pairs:
        if float(pair[1]) > 1:
            if ('fasta_sequences/processed' + str(pair[0]) + '.fasta')  == file:
                dixie_cup.append(file.read())
        if float(pair[1]) < 1:
            if ('fasta_sequences/processed' + str(pair[0]) + '.fasta')  == file:
                fire_cracker.append(file.read())
f.write(dixie_cup)
f.close()
z.write(fire_cracker)
z.close()