'''Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. '''


class Solution:
    def countFreq(self, arr, target):
        #code here
        c=0
        for i in arr:
            if i==target:
                c+=1
                
        return c
