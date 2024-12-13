'''Given a array arr[] and positive integer k denoting heights of towers, you have to modify the height of each tower either by increasing or decreasing them by k only once.

Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.

'''
class Solution:
    def getMinDiff(self,arr,k):
        # code here
        arr.sort()
        d = arr[-1]-arr[0]
        for i in range(len(arr)-1):
            lower= min(arr[0]+k,arr[i+1]-k)
            upper = max(arr[-1]-k,arr[i]+k)
            d = min(d,upper-lower)
            
        return d

