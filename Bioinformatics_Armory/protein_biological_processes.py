# Sample Dataset
# Q5SLP9
# Sample Output
# DNA recombination
# DNA repair
# DNA replication

from Bio import ExPASy
from Bio import SwissProt

file = open('rosalind_dbpr.txt', 'r')
output = open('rosalind_dbpr_output.txt', 'w')

line = file.readline().rstrip()
print(line)

handle = ExPASy.get_sprot_raw(line)
record = SwissProt.read(handle)
# use 'dir(record) to get all the attributes of 'record'
# we are interested in record.cross_references
# it'll seem like an information overload, but it's really
# just all the same info as https://www.uniprot.org/uniprot/B5ZC00.txt
# I want the biological processes of the protein in question
# record.cross_references is all of the 'DR' lines of the file. It contains
# the biological process info that I want.
for r in record.cross_references:
    # Notice that all of the processes
    # are pre-pended by 'GO', *BUT* that the functions are too. See that processes
    # all start with 'P'? We can use the 'GO' start and 'P' pre-pend to select the
    # desired text: r[0] == "GO and r[2].startswith('P'). I cycle through all the
    # records with a for loop and use if logic to snag the processes of interest.
    if r[0] == "GO" and r[2].startswith('P'):
        # getting rid of the 'P:'
        process = r[2].split(":")[1]
        # each single line of process gets its own line in the output file
        output.write(process +"\n")
