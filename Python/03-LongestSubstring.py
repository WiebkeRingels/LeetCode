class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # length of longest substring
        max_len = 0
        
        # index of current substring whose length is counted
        substring_start = 0
        
        # dictionary containing char:index pairs
        used = {}
        
        for i, char in enumerate(s):
            
            # if a repeated character occurs, new substring starts one
            # index after the last occurence
            if char in used and substring_start <= used[char]:
                substring_start = used[char] + 1
                
            # only updated maximum length if the new substring is longer
            else:
                max_len = max(max_len, i-substring_start+1)
                
            used[char] = i

        return max_len