"""
Greetings

Problem Statement
Write a program that asks the user for their name and then prints a personalized greeting.

Input
The input consists of a string
S
S

Output
Output a single line containing the personalized greeting.

Constraints
1 ≤ S ≤ 1000
Example:
What is your name?

Input:
Alice
Output:
Hello, Alice! Nice to meet you.
Notes:
In the example, the user's name is "Alice". The program prints a greeting message, combining the user's name with the predefined message.
"""
name = input()
print("Hello, " + name + "! Nice to meet you.")