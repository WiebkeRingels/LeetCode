class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        
        approach:
            
        build the zigzag string in a list of strings
        
        running through the string once is enough because for each letter we
        know in which row it belongs
        
        after building this list, the rows can be concatenated
        
        example:
        
        numRows -                       4
        string -                        helloworld
        row index after conversion -    1234321234
          
        """
        
        curr_row = 1
        rows = [''] * numRows
        
        # special case, one row is equal to no zigzag
        if numRows == 1:
            return s
        
        # create row array
        for (i,char) in enumerate(s):
            
            rows[(curr_row-1)] += char
            
            # zig zag
            if curr_row == 1: 
                step = 1
                
            if curr_row == numRows:         
                step = -1
                
            curr_row += step
            
        return ''.join(rows)