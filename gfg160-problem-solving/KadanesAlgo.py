'''Given an integer array arr[]. You need to find the maximum sum of a subarray.'''

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        res = maxx = arr[0]
        
        
        for i in range(1,len(arr)):
            maxx = max(maxx+arr[i],arr[i])
            res = max(res,maxx)
            
        return res
