# Read an integer .
#
# Without using any string methods, try to print the following:
#
#
# Note that "" represents the values in between.
#
# Input Format
# The first line contains an integer .
#
# Output Format

if __name__ == '__main__':
    n = int(input())
    l = [str(i) for i in range(1, n + 1)]
    print(''.join(l))