#!/usr/bin/env python
'''
Rosalind Bioinformatics Armory Data Formats
http://rosalind.info/problems/frmt/
Given: a collection of <10 GenBank entry IDs
Return: The shortest of the strings in FASTA format
'''
from Bio import Entrez
from Bio import SeqIO

'''
provided example code of how to
Entrez.email = "daviqd.halvorsen@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=["FJ817486, JX069768, JX469983"], \
rettype="fasta")
records = handle.read()
print records
'''

'''
from Bio import Entrez
from Bio import SeqIO
Entrez.email = "daviqd.halvorsen@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=["FJ817486", "JX069768", "JX46998X"], \
rettype="fasta")
records = list (SeqIO.parse(handle, "fasta")) # this spits out everything in FASTA
print records[0].id # first record
print len(records[-1].seq)
'''

#print records[0].seq
file = open('/home/david/Downloads/rosalind_frmt.txt', 'r')
output = open('rosalind_frmt_answer.txt', 'w')
# file is a single line
line = file.readline()
individual_ids = line.split()
#print(individual_ids)
comma_separated_ids = ",".join(individual_ids)
Entrez.email = "daviqd.halvorsen@gmail.com"
# blocked for occasionala testing
handle = Entrez.efetch(db="nucleotide", id=[comma_separated_ids], \
rettype="fasta")
# this was used to test the provided sample input
# handle = Entrez.efetch(db="nucleotide", id=["FJ817486", "JX069768", "JX469983"], \
# rettype="fasta")
records = list (SeqIO.parse(handle, "fasta"))
# start shortest length as first record entry
length_shortest_length = len(records[0].seq)
id_shortest_length = records[0].id

for record in records:
    print(record.id + " length is: ")
    print(len(record))
    if len(record) < length_shortest_length:
        shortest_length = len(record)
        record_shortest_length = record
        id_shortest_length = record.id
print("shortest_length is: " + str(length_shortest_length))
print("id of shortest_length is: " + id_shortest_length)
#print(record_longest_length)
#output.write(record_longest_length)
fasta_handle = Entrez.efetch(db="nucleotide", id=id_shortest_length, rettype="fasta")
fasta_shortest_length = fasta_handle.read()
output.write(fasta_shortest_length)
file.close()
output.close()
