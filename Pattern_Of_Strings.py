'''Q.Given a string S of length N, find the pattern of the strings as shown below in the examples.
Input: S = "GeeK"
Output: Geek
        Gee
        Ge
        G
Explanation: Decrease one character 
after each line
'''
def pattern(self, S):
		# code here
		n=len(S)
		l=[]
		for i in range(n,0,-1):
		    l.append(S[:i])
		return l
