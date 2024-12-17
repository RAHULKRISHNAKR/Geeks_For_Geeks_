'''Given a string s consisting of lowercase Latin Letters. Return the first non-repeating character in s. If there is no non-repeating character, return '$'.
Note: When you return '$' driver code will output -1.
'''

class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        #code here
        d={}
        for x in s:
            if x in d.keys():
                d[x]+=1
            else:
                d[x]=1
        
        for x in s:
            if d[x]==1:
                return x
                
        return '$'
