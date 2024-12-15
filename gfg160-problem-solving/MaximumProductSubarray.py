'''Given an array arr[] that contains positive and negative integers (may contain 0 as well). 
Find the maximum product that we can get in a subarray of arr[].
Note: It is guaranteed that the output fits in a 32-bit integer.'''

class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		n=len(arr)
		lr,rl=1,1
		mp = float('-inf')
		
		for i in range(n):
		    if lr==0:
		        lr=1
		    if rl==0:
		        rl=1
		        
		    lr *= arr[i]
		    rl*= arr[n-i-1]
            
            mp = max(lr,rl,mp)
            
        return mp
