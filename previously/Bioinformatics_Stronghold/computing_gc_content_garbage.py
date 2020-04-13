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
# read in the test data & create the answer submission file
file = open('/home/david/Downloads/rosalind_gc.txt', 'r')
output = open('/media/david/Linux/Rosalind/My_Answer_Submissions/ \
rosalind_gc_answer.txt', 'w')
# this data is multi-lined, so it needs readlines
lines = file.readlines()
print(lines)
# Wow! There are 10 DNA strings and new line characters (see print)
# this solution will be complicated ...
# for item in lines:
    # This yielded 10 '<' items, so it'll be a good way of splitting
    # if '>' in item:
        # print("'>' character found!")
# each file starts with '>Rosalind_NUMBER\n'. Once I split into the individual
# DNA strings I could do BUCKET_NAME[1] as the start (to skip Rosalind), OR
# I could just ignore cause there's no G or C in it :P
# there's gotta be a way of iteratively creating buckets, but I don't necessarily
# need to do that cause I know there's only going to be 10, so here they are:
DNA_Bucket_1 = ''
DNA_Bucket_2 = ''
DNA_Bucket_3 = ''
DNA_Bucket_4 = ''
DNA_Bucket_5 = ''
DNA_Bucket_6 = ''
DNA_Bucket_7 = ''
DNA_Bucket_8 = ''
DNA_Bucket_9 = ''
DNA_Bucket_10 = ''
# ^if there are less than 10 reads it'll still work cause those'll be blank
# I'll bump up this each time there's a new '>' character to store things in!
current_bucket = 0
for DNA_string in lines:
    if '>' in DNA_string:
        current_bucket += 1
    print("A '>' character was found!")
    print("Current bucket is: " + str(current_bucket))
    # don't want 'Rosalind' messing with my letter counts
    if 'Rosalind' in DNA_string:
        print("Rosalind found!")
        continue
    elif current_bucket == 1:
        DNA_Bucket_1 += DNA_string
    elif current_bucket == 2:
        DNA_Bucket_2 += DNA_string
    elif current_bucket == 3:
        DNA_Bucket_3 += DNA_string
    elif current_bucket == 4:
        DNA_Bucket_4 += DNA_string
    elif current_bucket == 5:
        DNA_Bucket_5 += DNA_string
    elif current_bucket == 6:
        DNA_Bucket_6 += DNA_string
    elif current_bucket == 7:
        DNA_Bucket_7 += DNA_string
    elif current_bucket == 8:
        DNA_Bucket_8 += DNA_string
    elif current_bucket == 9:
        DNA_Bucket_9 += DNA_string
    elif current_bucket == 10:
        DNA_Bucket_10 += DNA_string
    # this else'll run if there's more than 10 '>'
    else:
        print("I haz too many buckets!")
# Awesome! This gets individual characters (can count for GC)
# for item in DNA_Bucket_1:
    # print("'"+item.strip()+"'")
# doing this one at a time ... I'll create functions next
# this is the working GC calculator (pre-function)
'''
nucleotides = 0
GC_nucleotides = 'GC'
G_or_C = 0
for item in DNA_Bucket_1:
    print("'"+item.strip()+"'")
    if item.isalpha():
        nucleotides += 1
        if item in GC_nucleotides:
            G_or_C += 1
        else:
            pass
    else:
        print("non-alpha detected!")
G_or_C = float(G_or_C)
nucleotides = float(nucleotides)
GC_1 = 100 * G_or_C / nucleotides
print(G_or_C)
print(nucleotides)
print(GC_1)
'''
def GC_calculator(dna_bucket):
    nucleotides = 0
    GC_nucleotides = 'GC'
    G_or_C = 0
    for item in dna_bucket:
        print("'"+item+"'")
        if item.isalpha():
            nucleotides += 1
            if item in GC_nucleotides:
                G_or_C += 1
            else:
                pass
        else:
            print("non-alpha detected!")
    G_or_C = float(G_or_C)
    nucleotides = float(nucleotides)
    GC_percent = 100 * G_or_C / nucleotides
    # print(G_or_C)
    # print(nucleotides)
    # print(GC_percent)
    return GC_percent
# need to store as many as 10 GC concentrations
GC_1 = GC_calculator(DNA_Bucket_1)
GC_2 = GC_calculator(DNA_Bucket_2)
GC_3 = GC_calculator(DNA_Bucket_3)
GC_4 = GC_calculator(DNA_Bucket_4)
GC_5 = GC_calculator(DNA_Bucket_5)
#GC_6 = GC_calculator(DNA_Bucket_6)
#GC_7 = GC_calculator(DNA_Bucket_7)
#GC_8 = GC_calculator(DNA_Bucket_8)
# this becomes a divide by zero, so get rid of it
#GC_9 = GC_calculator(DNA_Bucket_9)
#GC_10 = GC_calculator(DNA_Bucket_10)

# I think I could cycle through these if I'd created them in a dict
print(GC_1)
print(GC_2)
print(GC_3)
print(GC_4)
print(GC_5)
#print(GC_6)
#print(GC_7)
#print(GC_8)
#print(GC_9)
#print(GC_10)

file.close()
output.close()

# HAHAHA, this garbage code solved the problem!
