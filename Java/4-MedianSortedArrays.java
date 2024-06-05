class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    	
    	int n1 = nums1.length;
    	int n2 = nums2.length;
    	
    	// making sure that nums1 is the smaller array
    	if(n1 > n2) {
    		return this.findMedianSortedArrays(nums2, nums1);
    	}
    	
    	int n_total = n1 + n2;
    	int n_half = (int)Math.ceil(n_total / 2.0);
    	
    	// pointers for binary search
    	int left = 0;
    	int right = n1;
    	
    	// binary search on smaller array nums1
    	while(left <= right) {
    		
    		// create partition
    		int m1 = (left + right) / 2;
    		int m2 = n_half - m1;
    		
    		// check boundaries of the partition   		
    		int left1 = ((m1 - 1) >= 0)? nums1[m1 - 1] : (int)Double.NEGATIVE_INFINITY;
    		int right1 = (m1 < n1)? nums1[m1] : (int)Double.POSITIVE_INFINITY;
    		int left2 = ((m2 - 1) >= 0)? nums2[m2 - 1]: (int)Double.NEGATIVE_INFINITY;
    		int right2 = (m2 < n2)? nums2[m2] : (int)Double.POSITIVE_INFINITY;
    		
    		// partition correct
    		if(left1 <= right2 && left2 <= right1) {
    			
    			// compute median depending on total number of elements
    			if(n_total % 2 == 1) { // odd
    				
    				return Math.max(left1, left2);
    			}
    			else { // even
    				
    				return (double)((Math.max(left1, left2) + Math.min(right1, right2)) / 2.0);
    			}
    		}
    		
    		else if (left1 > right2) { // too many elements from nums1 in partition
    			
    			right = m1 - 1;    			
    		}
    		
    		else { // too many elements from nums2 in partition
    			
    			left = m1 + 1;
    		}	
    	}
    	
    	// should never reach this statement
		return Double.POSITIVE_INFINITY;
    }
}
