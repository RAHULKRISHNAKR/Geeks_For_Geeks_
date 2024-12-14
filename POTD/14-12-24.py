'''Given a sorted and rotated array arr[] of distinct elements, the task is to find the index of a target key. Return -1 if the key is not found.'''

class Solution:
    def search(self,arr,key):
        # Complete this function
        low = 0        
        high = len(arr)-1
        
        while high >= low:
            mid = (high+low)//2
        
            if arr[mid]==key:
                return mid
                
            if arr[low]<=arr[mid]:
                if arr[low]<=key<arr[mid]:
                    high = mid-1
                else:
                    low=mid+1
            else:
                if arr[mid]<key<=arr[high]:
                    low = mid+1
                else:
                    high = mid-1
            
        return -1
