'''
You are given an integer N, reverse the digits of given number N, 
ensuring that the reversed number has no leading zeroes.
Return the resulting reversed number.
'''

class Solution:
	def reverse_digit(self, n):
		# Code here
        return (int(str(n)[::-1]))
        
