import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
    	
    	List<List<Integer>> res = new ArrayList<List<Integer>>();
    	int n = nums.length;
    	
    	// sort array to avoid redundant solutions
    	Arrays.sort(nums);
    	
    	for(int i = 0; i < n; i++) {
    		
    		int curr_num = nums[i];
    		
    		if(i > 0 && curr_num == nums[i-1]) continue;
    		
    		// left and right pointer to find three sum
    		int l = i + 1;
    		int r = n - 1;
    		
    		while(l < r) {
    			
    			int curr_sum = curr_num + nums[l] + nums[r];
    			
    			// move pointer 
    			l = (curr_sum < 0)? l+1 : l;
    			r = (curr_sum > 0)? r-1 : r;
    			
    			// three sum found
    			if(curr_sum == 0) {
    				res.add(Arrays.asList(curr_num, nums[l], nums[r]));
    				l += 1;
    				
    				while(nums[l] == nums[l - 1] && l < r) l+=1 ;
    			}
    		}
    	}
    	
		return res;
    }
}