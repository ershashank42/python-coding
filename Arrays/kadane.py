'''
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Example 1:

Input:
N = 5
arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.

Example 2:

Input:
N = 4
arr[] = {-1,-2,-3,-4}
Output:
-1
Explanation:
Max subarray sum is -1 
of element (-1)
'''

def maxSubArraySum(a,size):
    ##Your code here
    eh=0
    sf=0
    for i in range(0,size):
        eh+=a[i]
        if eh<0:
            eh=0
        if sf<eh:
            sf=eh
    if sf>=0:
        return sf
    else:
        return -1
    
a=[1,2,3,-2,5]
size=len(a)
print(maxSubArraySum(a,size))