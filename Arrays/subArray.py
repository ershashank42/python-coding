'''
Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

Example 1:

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.
 

Example 2:

Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements 
from 1st position to 5th position
is 15.
'''

def subarray(arr,n,s):
    su,l,r=arr[0],0,1
    if su==s:
        return [1,1]
    while r<n:
        su+=arr[r]
        while su>s and l<r:
            su-=arr[l]
            l+=1
        if su==s:
            return [l+1, r+1]
        r+=1
    return [-1]

arr =[1,2,3,7,6]
n=5
s=12
print(subarray(arr,n,s))