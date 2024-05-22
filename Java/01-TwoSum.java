package two_sum;
import java.util.HashMap;
import java.util.Map;

public class Solution {
	public int[] twoSum(int[] nums, int target) {
		
		/*
		 *  approach:
		 *  
		 *  use hash table to store numbers and their indices in the array
		 *  
		 *  while filling the hash table, check if the difference to the
		 *  target number is already stored in the hash table
		 *  
		 *  if the difference is already in the hash table, there is a 
		 *  number x in nums[i] for that is true:
		 *  - target = diff + x
		 *  
		 *  --------------------------------------------------------------
		 *  
		 *  time complexity:
		 *  
		 *  hash table storage ~ O(1)
		 *  loop through array ~ O(n)
		 *  total: O(1) + O(n) = O(n)
		 *  
		 */

		// create hash table that will store elements of n with the
		// corresponding index
		Map<Integer, Integer> hashTable = new HashMap<>();
		int n = nums.length;

		for (int i = 0; i < n; i++) {
			int diff = target - nums[i];
			
			// if the difference is already in the hash table,
			// there is a number x for that is true:
			// - target = diff + x
			// - (x,i_x) is in hash table
			if (hashTable.containsKey(diff)) {
				return new int[]{hashTable.get(diff), i};
			}
			
			// fill hash table until solution is found
			hashTable.put(nums[i], i);
		}

		// no solution
		return new int[]{};

	}
}
