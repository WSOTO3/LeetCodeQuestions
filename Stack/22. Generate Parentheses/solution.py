class Solution:
    def generateParenthesis(self, n): 
        res = [[] for _ in range(n+1)]# result variable filled with lists for each parenthesis in n + 1
        res[0] = [""] # first list is quotes
        
        for k in range(n + 1): # for range 
            for i in range(k): # 
                for left in res[i]: # 
                    for right in res[k-i-1]: # 
                        res[k].append("(" + left + ")" + right) # 
        
        return res[-1] #
