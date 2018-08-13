#!/usr/bin/env python

'''
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
Sample Dataset
    GAGCCTACTAACGGGAT
    CATCGTAATGACGGCCT
Sample Output
    7
'''
# reading in the Rosalind dataset and preparing my answer file
file = open('/home/david/Downloads/rosalind_hamm.txt', 'r')
output = open('/media/david/Linux/Rosalind/My_Answer_Submissions/\
rosalind_hamm_answer.txt', 'w')

# multi-lined file read in the lines
lines = file.readlines()
# I can separate both lines with this
'''
print("first: ")
print(lines[0])
print("second: ")
print(lines[1])
'''
DNAone = lines[0]
DNAtwo = lines[1]
differences = 0
# they're the same length
# print(len(DNAone))
# print(len(DNAtwo))

i = 0
while i <= len(DNAone)-1:
    # print(i)
    current_DNA_one = DNAone[i]
    current_DNA_two = DNAtwo[i]
    # print(current_DNA_one)
    # print(current_DNA_two)
    if current_DNA_one == current_DNA_two:
        pass
    else:
        differences += 1
    i += 1
# print the differences to the screen
print(differences)
# save the differences # to the output file
output.write(str(differences))


# closing all files
file.close()
output.close()
