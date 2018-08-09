# Given: A string s of length at most 10000 letters.
# Return: The number of occurrences of each word in s, where words are
# separated by spaces. Words are case-sensitive, and the lines in the
# output can be in any order.

# Sample Dataset
# We tried list and we tried dicts also we tried Zen
# Sample Output
# and 1
# We 1
# tried 3
# dicts 1
# list 1
# we 2
# also 1
# Zen 1
# note 'We' and 'we' are counted separately!

file = open('rosalind_ini6.txt', 'r')
output = open('rosalind_ini6_output.txt', 'w')
dictionary = {}
line = file.readline()
# print(line)
# There is no punctuation (only spaces), so I can split on ' '
# print(line.split())
split_line = line.split()
for word in split_line:
    #print(word)
    if word in dictionary:
        dictionary[word] = dictionary[word] + 1
    else:
        dictionary[word] = 1

# print(dictionary)
for item in dictionary:
    # print(item + ' ' + str(dictionary[item]))
    output.write(item + ' ' + str(dictionary[item]) + '\n')
file.close()
output.close()
