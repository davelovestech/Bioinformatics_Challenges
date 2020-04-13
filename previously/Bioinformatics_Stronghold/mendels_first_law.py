#!/usr/bin/env python

'''
Given: Three positive integers k, m, and n, representing a population containing
k+m+n organisms: k individuals are homozygous dominant for a factor, m are
heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will
produce an individual possessing a dominant allele (and thus displaying the
dominant phenotype). Assume that any two organisms can mate.
Sample Dataset
    2 2 2
Sample Output
    0.78333
'''

# read in the sample dataset and create my answer file
file = open('/home/david/Downloads/rosalind_iprb.txt', 'r')
output = open('/media/david/Linux/Rosalind/My_Answer_Submissions/\
rosalind_iprb_answer.txt', 'w')

# this data only has one line
line = file.readline()
# print(line)
# print(line.split())
# get the 3 numbers individually
separate_numbers = line.split()
# it was silly to create these names
# they were too ugly in the calculation down below
homozygous_dominant = separate_numbers[0]
heterozygous = separate_numbers[1]
homozygous_recessive = separate_numbers[2]
# let the user know what's up
print("homozygous_dominant: " + str(homozygous_dominant))
print("heterozygous: " + str(heterozygous))
print("homozygous_recessive: " + str(homozygous_recessive))
# saving the input dataset intot he right names
k = int(separate_numbers[0])
m = int(separate_numbers[1])
n = int(separate_numbers[2])
# we'll need the sum of k, m, n for the formula
tot = float(k+m+n)
# compute it!
print (1 - (n/tot)*((n-1)/(tot-1)) - (n/tot)*(m/(tot-1)) - (m/tot)*((m-1)/(tot-1))*0.25)
