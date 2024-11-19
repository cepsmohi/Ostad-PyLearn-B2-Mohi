"""
Triplet Sum

বাং
Problem Statement
Write a program where you will be given an array arr[] of size N and an integer P. Find the triplet in the array which sums up to the given integer P.

Input
The program will take an integer
N
N as the size of an array. Then it will take the integer values of the array
arr[]
arr[]. Finally, it will take the target value
P
P.

Output
The output will print the triplet numbers which will generate the sum.

Constraints
0 ≤ N ≤ 100000
0 ≤ arr[] ≤ 100000
0 ≤ P ≤ 100000
Example:
Enter numbers
"""
def findTriplet(arr, n, P):
    arr.sort()
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == P:
                return arr[i], arr[left], arr[right]
            elif current_sum < P:
                left += 1
            else:
                right -= 1
    return None

N = int(input())
arr = list(map(int, input().split()))
P = int(input())

result = findTriplet(arr, N, P)
if result:
    print(f"{result[0]} {result[1]} {result[2]}")