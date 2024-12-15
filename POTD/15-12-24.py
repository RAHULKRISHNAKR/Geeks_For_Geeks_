'''Given an array arr[] where no two adjacent elements are same, find the index of a peak element. 
An element is considered to be a peak if it is greater than its adjacent elements (if they exist). 
If there are multiple peak elements, return index of any one of them. 
The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".
Note: Consider the element before the first element and the element after the last element to be negative infinity.'''

class Solution:   
    def peakElement(self,arr):
        # Code here
        n = len(arr)
    
        if n == 1:
            return 0
        if arr[0] > arr[1]:
            return 0
        if arr[n - 1] > arr[n - 2]:
            return n - 1
        
        low, high = 1, n - 2  
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] > arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1  
