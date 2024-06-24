class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        n = len(nums)
        
        # sort array to avoid redundant solutions
        nums.sort()
        
        for i, curr_num in enumerate(nums):
            
            # skip equal numbers to avoid redundant solutions
            if i > 0 and curr_num == nums[i - 1]:
                continue
            
            # create left and right pointer to run through remaining nums
            l,r = i + 1, n - 1
            while l < r:
                
                curr_sum = curr_num + nums[l] + nums[r]
                
                if curr_sum < 0:
                    l += 1
                
                elif curr_sum > 0:
                    r -= 1
                    
                else: # == 0
                    res.append([curr_num, nums[l], nums[r]])
                    l += 1
                    
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    
        return res