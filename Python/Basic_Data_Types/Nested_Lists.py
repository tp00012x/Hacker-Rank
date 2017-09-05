# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
#
# Input Format
#
# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.
#
# Constraints
#
# There will always be one or more students having the second lowest grade.
# Output Format
#
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

if __name__ == '__main__':
    n = int(input())
    marks = [[input(), float(input())] for _ in range(n)]
    scores = sorted({s[1] for s in marks})
    result = sorted(s[0] for s in marks if s[1] == scores[1])
    print('\n'.join(result))