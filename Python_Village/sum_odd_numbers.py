# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

# Sample Dataset
# 100 200
# Sample Output
# 7500

def sum_odd_numbers(a, b):
    current_total = 0
    while(a <= b):
        print("a is currently: " + str(a))
        if a % 2 == 1:
            current_total = current_total + a
            print(str(a) + " is an odd number!")
        a = a + 1
    print("Sum of odd numbers between " + str(a) + " and " + str(b))
    print("Is equal to: " + str(current_total))
a = 4305
b = 8525
sum_odd_numbers(a, b)
