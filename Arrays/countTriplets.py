'''
Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.
 
Example 1:

Input:
N = 4
arr[] = {1, 5, 3, 2}
Output: 2
Explanation: There are 2 triplets: 
1 + 2 = 3 and 3 +2 = 5 
â€‹Example 2:

Input: 
N = 3
arr[] = {2, 3, 4}
Output: 0
Explanation: No such triplet exits
'''

def countTriplet(arr, n):
    # code here
    c=0
    arr.sort()
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]==arr[k]:
                    c+=1
    return c
arr=[1,5,3,2]
n=4
print(countTriplet(arr,n))