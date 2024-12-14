'''Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.'''

class Solution:
    def mergeArrays(self, a, b):
        # code here
        n=len(a)
        m=len(b)
        
        i=n-1
        j=0
        
        while i>=0 and j<m:
            if a[i]>b[j]:
                a[i],b[j]=b[j],a[i]
                i-=1
                j+=1
            else:
                break
        
        a.sort()
        b.sort()
