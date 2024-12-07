'''You are given an array of integers arr[]. Your task is to reverse the given array.'''

class Solution:
    def reverseArray(self, arr):
        # code here
        n=len(arr)
        i=0
        j=n-1
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        return arr
      
