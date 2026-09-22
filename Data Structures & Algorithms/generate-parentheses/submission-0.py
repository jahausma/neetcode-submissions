class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        close_p = open_p = 0
        res = []
        curr = []

        def dfs(op, cl):
            if op == cl == n:
                res.append("".join(curr))   # we need them to
                return 
            
            # add open parentheses
            if op < n: # op cant be greater than n
                curr.append("(")
                dfs(op+1, cl)
                curr.pop() # must pop to clean up shared curr state

            # add close parentheses
            if cl < op: # we want cl to line up with op
                curr.append(")")
                dfs(op, cl+1)
                curr.pop() # must pop to clean up shared curr state
        
        dfs(open_p, close_p)

        return res
