class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        
        Manacher's algorithm
            
        """
        
        # for Manacher's algorithm to work, each character must be separated 
        # with a special character
        # this makes it also work for palindromes of odd length
        s = '#' + '#'.join(s) + '#'
        
        # store the lengths of palindromic substrings
        lp = [0 for _ in range(len(s))]
        
        # store center and rightmost position of palindromic substring
        center = 0
        right = 0
        
        # store max length and the corresponding palindromic substring
        max_len = 0
        p_substr = ""
        
        for i in range(len(s)):
            
            # get the mirrored index of the current char
            mirrored_i = 2 * center - i
            
            # if the current char is within the palindromic substring
            if i < right:
                lp[i] = min(right - i, lp[mirrored_i])
                 
            # expansion around center
            while i - lp[i] - 1 >= 0 and i + lp[i] + 1 < len(s) and s[i + 1 + lp[i]] == s[i - 1 - lp[i]]:                
                lp[i] += 1
                
            if i + lp[i] > right:
                center = i
                right = i + lp[i]
                
            # keep track of max value
            if lp[i] > max_len:
                max_len = lp[i]
                p_substr = s[i - lp[i] : i + lp[i] + 1].replace('#','')
                
        return p_substr