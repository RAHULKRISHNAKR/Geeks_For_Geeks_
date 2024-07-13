'''Print numbers from 1 to n without the help of loops. You only need to complete the function printNos() 
that takes N as parameter and prints number from 1 to N recursively.'''

class Solution:    
    def printNos(self,N):
        if N>1:
            self.printNos(N-1)
        print(N,end=" ")
