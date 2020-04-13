#!/usr/bin/env python
# coding: utf-8
# ^That utf-8 line is to let the interpreter know about the weird utf-8
# character in the text string below.
'''
Rosalind Rabbits and Recurrence Relations
Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n months,
if we begin with 1 pair and in each generation, every pair of reproduction-age
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
http://rosalind.info/problems/fib/
Sample Dataset
    5 3
Sample Output
    19
'''
# read in the sample Dataset & prepare answer file
file = open('/home/david/Downloads/rosalind_fib.txt', 'r')
output = open('rosalind_fib_answer', 'w')

# read the line, cut off the trailing '\n'
line = file.readline().rstrip()
# splt on spaces
split_line = line.split()
# During testing, I commented out the months and litter so I could use
# the provided sample dataset.
# test case
# months = 5
# litter = 3
# this grabs the month and litter info from the Rosalind dataset
months = int(split_line[0])
litter = int(split_line[1])
# lett you know what's going down
print("months are: " + str(months))
print("litter is: " + str(litter))
# implementing Fn = Fn-1 + Fn-2 * k
# I start the loop on the second month, so Fn-1 (previous 1) and
# Fn-2 (previous2) are both equal to 1
previous1 = 1
previous2 = 1
for i in range(2, months):
    # this is that fibonacci formula from above
    current = previous1 + litter * previous2
    # bumping conditions ahead for the next generation
    previous2 = previous1
    previous1 = current
print("Current number of rabbits: " + str(current))
output.write(str(current))
