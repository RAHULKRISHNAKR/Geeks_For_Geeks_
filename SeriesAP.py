class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        # code here
        difference=a2-a1
        #calculating nth ternm
        nthTerm=a1+(n-1)*difference
        return nthTerm
