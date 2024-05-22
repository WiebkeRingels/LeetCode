class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        max_signed_int = 2147483647
        x_reversed = 0
        
        # remember if negative number
        neg = False
        if x < 0:
            neg = True
            x *= (-1)
        
        # extract digits with modulo 10
        while x != 0:
            
            digit = x % 10
            x_reversed = x_reversed * 10 + digit
            x = int(x / 10)
         
        # only 32-bit integers supported
        if x_reversed > max_signed_int:
            return 0
        
        # take care of negative numbers
        if neg:
            x_reversed *= (-1)
            
        # return x_reversed
        return x_reversed
        