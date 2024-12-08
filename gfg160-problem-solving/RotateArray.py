'''
Given an unsorted array arr[]. 
Rotate the array to the left (counter-clockwise direction) by d steps, 
where d is a positive integer. Do the mentioned change in the array in place
'''

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
     #Your code here
        d = d%len(arr)
        arr[:d]=reversed(arr[:d])
        arr[d:]=reversed(arr[d:])
        arr[:] = reversed(arr)
        return arr
