class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # create stack to track open brackets
        stack = []
        
        for char in s:
            
            if char in '([{':
                
                stack.append(char)
                
            else: # closing bracket
                
                if not stack or \
                    stack[-1] == '(' and char != ')' or \
                    stack[-1] == '[' and char != ']' or \
                    stack[-1] == '{' and char != '}': 
                        return False
                else:
                    stack.pop()
                
        # if stack is empty (all brackets were matching), this returns true
        # else this returns false
        return not stack