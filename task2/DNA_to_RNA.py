with open('rosalind_rna.txt', 'r') as dna_file:
    res = dna_file.read().replace('T', 'U')
print(res)