class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
		approach:
		
		use hash table to store numbers and their indices in the array
		 
		while filling the hash table, check if the difference to the
		target number is already stored in the hash table
		
		if the difference is already in the hash table, there is a 
		number x in nums[i] for that is true:
		- target = diff + x
		 
		-----------------------------------------------------------------------
		 
		time complexity:
		 
		hash table storage ~ O(1)
		loop through array ~ O(n)
		total: O(1) + O(n) = O(n)

        """
        
        # create hash table (dictionary with pairs) that will store elements
        # of nums with the corresponding index
        hashTable = {}
        
        for ni,n in enumerate(nums):
            diff = target - n
            
            # if the difference is already in the hash table,
			# there is a number x for that is true:
			# - target = diff + x
			# - (x,i_x) is in hash table
            if str(diff) in hashTable:
                return [hashTable[str(diff)], ni]
            
            # fill hash table until solution is found
            hashTable[str(n)] = ni
        
        # no solution
        return []