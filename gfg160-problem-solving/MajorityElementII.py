# You are given an array of integer arr[] where each number represents a vote to a candidate.
# Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array.
# Note: The answer should be returned in an increasing format.

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        cp = len(arr)/3
        e1,e2 = -1,-1
        c1,c2 = 0,0
        
        for e in arr:
            if e == e1:
                e1=e
                c1+=1
            elif e == e2:
                e2=e
                c2+=1
            elif c1 == 0:
                e1=e
                c1+=1
            elif c2 == 0:
                e2=e
                c2+=1
            else:
                c1-=1
                c2-=1
            
        c1,c2=0,0
        
        for e in arr:
            if e == e1:
                c1+=1
            elif e == e2:
                c2+=1
        
        l=[]        
        if c1>cp:
            l.append(e1)
        if c2>cp:
            l.append(e2)
        
        if len(l)==2 and e1>e2:
            l[0],l[1] = l[1],l[0]
        
        return l
