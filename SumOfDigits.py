'''
Given a number, N. Find the sum of all the digits of N
 
'''

class Solution:
    def sumOfDigits (self, N):
        # code here
        l=[]
        s=str(N)
        for char in s:
            l.append(int(char))
        return sum(l)
