class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        rev = 0
        y = x
        
        # build reverse of number x
        while y > 0:
            rev = (rev * 10) + (y % 10)
            y = int(y / 10)

        return rev == x