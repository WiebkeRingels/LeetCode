class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # build integer in this variable
        num = 0
        
        # remember sign of number
        sign = 1
        
        # declare variables
        int_max_val = pow(2,31)-1
        int_min_val = -pow(2,31)
        
        # check when the digits start
        start = 0
        
        for i in range(len(s)):
            
            if(s[i] == " " and not start):
                i += 1
                
            elif(s[i] == "-" and not start):
                sign = -1
                i += 1
                start = 1
                
            elif(s[i] == "+" and not start):
                i += 1
                start = 1
                
            elif(s[i] <= "9" and s[i] >= "0"):
                start = 1
                num = num * 10 + int(s[i])
                
            else:
                if sign == 1:
                    return min((sign * num), int_max_val)
                        
                if sign == -1:
                    return max((sign * num), int_min_val)
                        
                else:
                    return 0
                
        if sign == 1:
            return min((sign * num), int_max_val)
                
        if sign == -1:
            return max((sign * num), int_min_val)
                
        else:
            return 0