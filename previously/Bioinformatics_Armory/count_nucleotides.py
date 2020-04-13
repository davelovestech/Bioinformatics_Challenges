# Given: A DNA string s of length at most 1000 bp.
# Return: Four integers (separated by spaces) representing the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s. Note: You must provide your answer in the format shown in the sample output below.

# Sample Dataset
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
#Sample Output
# 20 12 17 21

rosalind_file = open("rosalind_ini.txt", "r")
answer_submission = open("rosalind_ini_answer.txt", "w")
nucleotide_dictionary = {}
line = rosalind_file.readline()
# print(line)
line_characters = list(line)
# print(line_characters)
for character in line_characters:
    if character in nucleotide_dictionary:
        nucleotide_dictionary[character] = nucleotide_dictionary[character] + 1
    else:
        nucleotide_dictionary[character] = 1
A_count = str(nucleotide_dictionary['A'])
T_count = str(nucleotide_dictionary['T'])
G_count = str(nucleotide_dictionary['G'])
C_count = str(nucleotide_dictionary['C'])
# The Sample Output is uncecessarily confusing ... tell me the nucleotides
# Made this print statement to figure out which one goes where
print('A: ' + A_count + ' C: ' + C_count + ' G: ' + G_count + ' T: ' + T_count)
answer_submission.write(A_count + ' ' + C_count + ' ' + G_count + ' ' + T_count)
