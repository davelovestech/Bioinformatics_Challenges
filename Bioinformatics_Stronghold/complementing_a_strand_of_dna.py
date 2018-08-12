#!/usr/bin/env python
'''
Rosalind Complementing a Strand of DNA
Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.
http://rosalind.info/problems/revc/
Sample Dataset
    AAAACCCGGT
Sample Output
    ACCGGGTTTT
'''
file = open('/home/david/Downloads/rosalind_revc.txt', 'r')
output = open('rosalind_revc_answer.txt', 'w')
# line = 'AAAACCCGGT'
line = file.readline().rstrip()
complement = ''
nucleotides = list(line)
for nucleotide in nucleotides:
    if nucleotide == 'A':
        complement += 'T'
    if nucleotide == 'T':
        complement += 'A'
    if nucleotide == 'G':
        complement += 'C'
    if nucleotide == 'C':
        complement += 'G'
print(complement)
# need to reverse it
reversed_complement = complement[::-1]
print(reversed_complement)
