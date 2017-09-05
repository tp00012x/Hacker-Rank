# Task
# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format
#
# A single line containing a positive integer, .
#
# Constraints
#
# Output Format
#
# Print Weird if the number is weird; otherwise, print Not Weird.
#
# Sample Input 0
#
# 3
# Sample Output 0
#
# Weird
# Sample Input 1
#
# 24
# Sample Output 1
#
# Not Weird
# Explanation
#
# Sample Case 0:
#  is odd and odd numbers are weird, so we print Weird.
#
# Sample Case 1:
#  and  is even, so it isn't weird. Thus, we print Not Weird.

if __name__ == '__main__':
    n = int(raw_input())

    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n > 1 and n < 6:
        print("Not Weird")
    elif n % 2 == 0 and n > 5 and n < 21:
        print("Weird")
    elif n % 2 == 0 and n >= 20:
        print("Not Weird")