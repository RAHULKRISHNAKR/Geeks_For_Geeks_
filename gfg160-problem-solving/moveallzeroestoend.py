'''Given an array arr[]. 
Push all the zeros of the given array to the right end of the array 
while maintaining the order of non-zero elements.
Do the mentioned change in the array in place.'''

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	c=0
    	for i in range(len(arr)):
    	    if arr[i]!=0:
        	    arr[c]=arr[i]
        	    c+=1
        i=0
        while(c<len(arr)):
            arr[c]=0
            c+=1
        return arr
  
