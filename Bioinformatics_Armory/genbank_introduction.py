#!/usr/bin/env python

# Given: A genus name, followed by two dates in YYYY/M/D format.
# Return: The number of Nucleotide GenBank entries for the given genus that
# were published between the dates specified.

# Sample Dataset
# species_name='Anthoxanthum'
# min_date='2003/7/25'
# max_date='2005/12/27'

# Sample Output
# 7

from Bio import Entrez

file = open('/home/david/Downloads/rosalind_gbk.txt', 'r')
output = open('rosalind_gbk_output.txt', 'w')
# read all lines
content = file.readlines()
# grabbing lines 1-3 into the right lables (see data format)
species_name = content[0].rstrip()
min_date = content[1].rstrip()
max_date = content[2].rstrip()
# checking the labels w/ a print
print(species_name)
print(min_date)
print(max_date)
# if I'm hogging the database, they'll message me
Entrez.email = "daviqd.halvorsen@gmail.com"
# why is 'pdat' required?
# code snippet from https://github.com/Shivi91/Rosalind-1/blob/master/Armory_003_GBK.py
handle = Entrez.esearch(db="nucleotide", term=species_name+'[ORGN]' \
, mindate=min_date, maxdate=max_date, datetype='pdat')
record = Entrez.read(handle)
print(record["Count"])
count_is = record["Count"]
output.write(count_is)

# closing all files
file.close()
output.close()
