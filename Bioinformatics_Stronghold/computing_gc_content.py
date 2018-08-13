#!/usr/bin/env python

'''
Rosalind Bioinformatics Stronghold Computing GC Content
http://rosalind.info/problems/gc/
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in all
decimal answers unless otherwise stated; please see the note on absolute error
below.
Sample Dataset
    >Rosalind_6404
    CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
    TCCCACTAATAATTCTGAGG
    >Rosalind_5959
    CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
    ATATCCATTTGTCAGCAGACACGC
    >Rosalind_0808
    CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
    TGGGAACCTGCGGGCAGTAGGTGGAAT
Sample Output
    Rosalind_0808
    60.919540
'''
# this is how the fasta files are parsed
from Bio import SeqIO
# this is where the GC calculator comes from
from Bio.SeqUtils import GC
# setting the GC content and GCname to 0
# IF the computed GC content is higher, during the below for loop,
# these values get replaced
GCcont = 0
GCname = ""
# open the Rosalind dataset file
file = open("/home/david/Downloads/rosalind_gc.txt", "r")
# cycle through the fasta records in the Rosalind dataset
for record in SeqIO.parse(file, "fasta"):
    # if the current GC content is higher than the last highest,
    # then replace the GC content and GC record name
    if GCcont < GC(record.seq):
        GCcont = GC(record.seq)
        GCname = record.id
# print out the solution
print GCname
print round(GCcont,2), "%"
