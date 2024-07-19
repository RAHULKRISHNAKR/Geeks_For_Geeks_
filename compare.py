#Given two integers, n and m. The task is to check the relation between n and m.


class Solution:
    def compareNM(self, n : int, m : int) -> str:
        # code here
        if n<m:
            return 'lesser'
        elif n>m:
            return 'greater'
        else:
            return 'equal'
