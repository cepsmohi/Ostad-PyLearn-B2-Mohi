"""
Simple Summation

Problem Statement
Write a program that calculates and prints the sum of two numbers entered by the user.

Input
The input consists of two integers.

Output
Output a single line containing the sum of two integers.

Constraints
-2 31 ≤ |S| ≤ 231 - 1
Example:
Enter two numbers

Input:
5 2
Output:
7
"""
a, b = map(int, input().split())
sum = a + b
print(sum)