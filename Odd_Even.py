# Given a positive integer N, determine whether it is odd or even.

class Solution:
    def oddEven (ob,N):
        res=""
        if N%2==0:
            res="even"
        else:
            res="odd"
        return res
