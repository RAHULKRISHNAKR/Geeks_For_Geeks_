'''Given an array arr[] denoting heights of N towers and a positive integer K.
For each tower, you must perform exactly one of the following operations exactly once.
Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.
Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.'''

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        n=len(arr)
        arr.sort()
        res = arr[n-1]-arr[0]
        
        minn=arr[0]
        maxx=arr[n-1]
        
        for i in range(1,n):
            if arr[i]<k:
                continue
            minn = min(arr[0]+k,arr[i]-k)
            maxx = max(arr[i-1]+k,arr[n-1]-k)
            
            res = min(res,maxx-minn)
        
        return res
