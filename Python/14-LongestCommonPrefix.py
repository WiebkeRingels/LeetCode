class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # sort lexicographically
        strs.sort()
        
        # read-out first and last string of sorted array
        first = strs[0]
        last = strs[-1]
        min_len = min(len(first), len(last))
        
        # find the longest common prefix between first and last
    	# due to lexicographic order, this prefix holds true for all 
        # other entries as well
        for i in range(min_len):
            
            # increase i until chars are not equal anymore
            if not first[i] == last[i]:
                
                return first[0:i]
        
        # in this case, the complete string is the longest prefix
        return first