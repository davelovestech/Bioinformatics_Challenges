# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

# Sample Dataset
# 100 200
# Sample Output
# 7500
current_total = 0
def sum_odd_numbers(a, b):
    while(a < b):
