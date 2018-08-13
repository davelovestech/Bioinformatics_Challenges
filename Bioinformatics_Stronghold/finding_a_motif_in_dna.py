#!/usr/bin/env python

'''
Rosalind Finding a Motif in DNA
Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
Sample Dataset
    GATATATGCATATACTT
    ATAT
Sample Output
    2 4 10
http://rosalind.info/problems/subs/
'''
# read in the Rosalind data and prepare my answer file
file = open("/home/david/Downloads/rosalind_subs.txt", "r")
output = open("/media/david/Linux/Rosalind/My_Answer_Submissions/\
rosalind_subs_answer.txt", "w")
# read in the Rosalind Dataset
lines = file.readlines()
# testing things
# print(lines)
# print(lines[0])
# print(lines[1])
# reading in DNA and motif. used strip cause of new line characters
DNA = lines[0].strip()
motif = lines[1].strip()
# let the user know what the DNA and motif are
print("DNA is: ")
print(DNA)
print("motif is: ")
print(motif)
# initialize empty list to store positions
locations_of_motif = []
# get lengths of DNA and motif
length_of_DNA = len(DNA)
length_of_motif = len(motif)
# initialize counters. i is for DNA string (starts at 0)
# j is for human-readable list position (starts at 1)
i = 0
j = 1
print("length of motif is: " + str(length_of_motif))
# cycle through each individual item of the DNA (see i is just +=1)
while i < length_of_DNA:
    # print(i)
    # I'm testing every single position for + length_of_motif for motif
    current_string = DNA[i:i+length_of_motif]
    # print("current string")
    # print(current_string)
    # if motif is found, store j position (j is human-readable #)
    if current_string == motif:
        print("Match found!")
        locations_of_motif.append(j)
    else:
        pass
    # bump those iterables up
    i += 1
    j += 1
# this is a list and the question asks for no commas ... more code needed
print(locations_of_motif)
# initialize empty string to store positions and re-initalize j
string_of_locations = ''
j = 1
# for every human-readable position in the list, add to a string with just spaces
for location in locations_of_motif:
    # I don't want a space before the first entry, so this is for 1st
    if j == 1:
        string_of_locations = string_of_locations + str(location) + ' '
    # all other entries have spaces on either side
    else:
        string_of_locations = string_of_locations + ' ' + str(location) + ' '
print(string_of_locations)
# save the answers in a text file
output.write(string_of_locations)
