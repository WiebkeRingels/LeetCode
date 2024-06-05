class Solution {
    public int maxArea(int[] height) {
    	
    	int n = height.length;
    	
    	// pointer for search
    	int left = 0;
    	int right = n - 1;
    	
    	// keep track of maximum area while running through the array
    	int max_area = 0;
    	
    	while(left < right) {
    		
    		// compute the area between the current pointers
    		int curr_area = Math.min(height[left], height[right]) * (right - left);
    		max_area = Math.max(max_area, curr_area);
    		
    		// move the pointer with the smaller height towards the center
    		if(height[left] < height[right]) {
    			
    			left += 1;
    		}
    		else {
    			
    			right -= 1;
    		}
    		
    	}
    	
		return max_area; 
    }
}