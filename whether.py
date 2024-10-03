'''
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
Input format:
The input containing an integer 'n' which denotes the given number.
Output format:
If the given number is factorial, print "Yes". Otherwise, print "No".
Refer the sample output for formatting.
Sample Input:
6
Sample Output:
Yes
'''

n = int(input())  # Input the number

# Initialize variables
factorial = 1
i = 1

# Loop to calculate factorials
while factorial < n:
    i += 1
    factorial *= i

# Check if n is a factorial number
if factorial == n:
    print("Yes")
else:
    print("No")
