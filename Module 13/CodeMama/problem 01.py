"""
Lone Zeroes

বাং
Problem Statement
Write a program to create a function which counts how many lone 0s appear in a given number. Lone means the number doesn't appear twice or more in a row.Previous and next numbers are not zeroes. For example - countLoneZeroes(10101) ➞ 2

Input
The program will take an integer
N
N as input

Output
The output will print the number of lone 0's in the integer.

Constraints
0 ≤ N ≤ 100000
Example:
Enter number
"""

def countLoneZeroes(n):
    count = 0
    n_str = str(n)
    for i in range(len(n_str)):
        if n_str[i] == '0':
            if n_str[i-1] != '0' and n_str[i+1] != '0':
                count += 1
    return count
# Input
N = int(input())
# Output
print(countLoneZeroes(N))