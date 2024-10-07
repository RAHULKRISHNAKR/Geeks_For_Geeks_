#You are given an integer n. You need to convert all zeroes of n to 5.

class Solution:
    def convertFive(self, n):
        # Code here
        k=str(n)
        k=k.replace("0","5")
        m=int(k)
        return m
