'''
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.
'''

class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if arr==[]:
            return -1
        
        a = set(arr)
        b = list(a)
        b = sorted(b,reverse=True)
        if len(b)<2:
            return -1
        else:
            return b[1]
        
