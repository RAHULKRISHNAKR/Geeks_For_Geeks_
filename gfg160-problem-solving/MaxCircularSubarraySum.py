'''Given an array of integers arr[] in a circular fashion. Find the maximum subarray sum that we can get if we assume the array to be circular.'''

def circularSubarraySum(arr):
    ##Your code here
    total,currMax,currMin,Max,Min=0,0,0,0,0
    
    for i in range(len(arr)):
        currMax = max(currMax+arr[i],arr[i])
        Max = max(currMax,Max)
        
        currMin = min(currMin+arr[i],arr[i])
        Min = min(currMin,Min)
        
        total+=arr[i]
        
    
    normalSum = Max
    circularSum = total-Min
    
    if Min==total:
        return normalSum
    
    return max(normalSum,circularSum)
