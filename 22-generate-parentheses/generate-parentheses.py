class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        def backtrack(path, open_count, close_count):
            # Base case: if we have used n pairs (2n characters)
            if len(path) == 2 * n:
                res.append(path)
                return
            
            # Add opening parenthesis if we haven't used n opening ones yet
            if open_count < n:
                backtrack(path + "(", open_count + 1, close_count)
            
            # Add closing parenthesis if we have more open than closed
            if close_count < open_count:
                backtrack(path + ")", open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return res