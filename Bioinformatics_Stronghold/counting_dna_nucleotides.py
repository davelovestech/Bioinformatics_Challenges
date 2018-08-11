#!/usr/bin/env python
'''
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of
times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''

'''
SAMPLE DATASET: AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTC
TGATAGCAGC
SAMPLE OUTPUT: 20 12 17 21
'''

file = open('/home/david/Downloads/rosalind_dna.txt', 'r')
output = open('rosalind_dna_answer.txt', 'w')
# this is a temporary line to test output with provided sample
# line = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

# added .rstrip() because dictionary had '\n' entry
line = file.readline().rstrip()
# print(line)

characters = list(line)
# print(characters)
nucleotide_dictionary = {}
for nucleotide in characters:
    # print nucleotide
    if nucleotide in nucleotide_dictionary:
        nucleotide_dictionary[nucleotide] = nucleotide_dictionary[nucleotide] + 1
    else:
        nucleotide_dictionary[nucleotide] = 1
print("dictionary is: ")
print(nucleotide_dictionary)
A_count = str(nucleotide_dictionary['A'])
C_count = str(nucleotide_dictionary['C'])
G_count = str(nucleotide_dictionary['G'])
T_count = str(nucleotide_dictionary['T'])
print("rosalind output format: ")
print(A_count + ' ' + C_count + ' ' + G_count + ' ' + T_count)
