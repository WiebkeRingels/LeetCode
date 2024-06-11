class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        num = 0
        
        # for subtraction cases
        skip_next = False
        
        for i, char in enumerate(s):
            
            if i < len(s) - 1:
                next_char = s[i + 1]
            else:
                next_char = ""
            
            if not skip_next:
                if char == "I":
                    if next_char == "V":
                        skip_next = True
                        num += 4
                        
                    elif next_char == "X":
                        skip_next = True
                        num += 9
                    
                    else:
                        num += 1
                    
                elif char == "V":
                    num += 5
                    
                elif char == "X":
                    if next_char == "L":
                        skip_next = True
                        num += 40
                        
                    elif next_char == "C":
                        skip_next = True
                        num += 90
                    
                    else:
                        num += 10
                    
                elif char == "L":
                    num += 50
                    
                elif char == "C":
                    if next_char == "D":
                        skip_next = True
                        num += 400
                        
                    elif next_char == "M":
                        skip_next = True
                        num += 900
                    
                    else:
                        num += 100
                    
                elif char == "D":
                    num += 500
                    
                elif char == "M":
                    num += 1000
                    
            else:
                skip_next = False
            
        return num