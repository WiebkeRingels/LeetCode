import java.util.HashMap;
import java.util.Map;

class Solution {
    public int lengthOfLongestSubstring(String s) {
    	
    	// length of longest substring
    	int max_len = 0;
    	
    	// index of current substring whose length is counted
    	int substring_start = 0;
    	
    	// hash table containing char:index pairs
    	Map<String, Integer> used = new HashMap<>();
    	
    	int n = s.length();
    	for(int i = 0; i < n; i++) {
    		
    		String si = s.substring(i,i+1);
    		
    		// if a repeated character occurs, new substring starts one
            // index after the last occurrence
    		if (used.containsKey(si) && substring_start <= used.get(si)) {
				substring_start = used.get(si) + 1;
			}
    		else {
    			
    			// only updated maximum length if the new substring is longer
    			max_len = Math.max(max_len, i - substring_start + 1);
    		}
    		
    		// fill hash table until solution is found
    		used.put(si, i);
    		
    	}
		return max_len;
        
    }
}