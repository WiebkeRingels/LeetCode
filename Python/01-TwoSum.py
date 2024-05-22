class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        ---------------------------------------------------------------
        
        approach:
        
        to keep the time complexity small, following equality is used:
        
        target = a + b (with a,b elements of nums)
        <=> 0  = target - a - b
        
        first difference is computed with first loop
        second difference is (indirectly) computed with second loop
        
        ---------------------------------------------------------------
        
        time complexity:
        
        first for loop: O(n)
        - run through n elements ~ O(n)
        - append function ~ O(1)
        
        second for loop: O(n)
        - run through n elements -> O(n)
        - index function ~ O(n)
        
        total: O(n) + O(n) = O(n)
        
        """

        # compute difference for each number in nums to target
        diffs = []
        
        for n in nums:
            diffs.append(target - n)
            
        # since one solution exists, one of the computed differences 
        # must be in the nums list as well
        for di, d in enumerate(diffs):
    
            if diffs[di] in nums:
        
                i = di
                j = nums.index(diffs[di])
                
                if i != j:
                    break
                
        return [i,j]