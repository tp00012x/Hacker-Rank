# You are given  numbers. Store them in a list and find the second largest number.
#
# Input Format
# The first line contains . The second line contains an array [] of  integers each separated by a space.

if __name__ == '__main__':
    N=int(input())
    list=list(set(map(int,input().strip().split(" "))))
    list.sort(reverse=True)
    print(list[1])