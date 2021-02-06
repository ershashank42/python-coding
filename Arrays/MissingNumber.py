'''
Given an array of size N-1 such that it can only contain distinct integers in the range of 1 to N. Find the missing element.

Example 1:

Input:
N = 5
A[] = {1,2,3,5}
Output: 4

Example 2:

Input:
N = 10
A[] = {1,2,3,4,5,6,7,8,10}
Output: 9
Your Task :
Complete the function MissingNumber() that takes array and N as input and returns the value of the missing number.
'''

def MissingNumber(array,n):
    # code here
    actsum=int(n*(n+1)/2)
    obsum=sum(array)
    return (actsum-obsum)

array=[1,2,3,5]
n=4
print(MissingNumber(array,n))