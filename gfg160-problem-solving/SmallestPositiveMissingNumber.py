'''You are given an integer array arr[]. 
Your task is to find the smallest positive number missing from the array.
Note: Positive number starts from 1. The array can have negative integers too.'''

class Solution:
    
    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        n = len(arr)
        
        # Place elements in their correct positions.
        for i in range(n):
            while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
        
        # Identify the first missing positive.
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
        
        return n + 1
