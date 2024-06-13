import java.util.Arrays;

class Solution {
    public String longestCommonPrefix(String[] strs) {
    	
    	// sort lexicographically
    	Arrays.sort(strs);
    	
    	// read-out first and last string in sorted array
    	String first = strs[0];
    	String last = strs[strs.length - 1];
    	
    	// find the longest common prefix between first and last
    	// due to lexicographic order, this prefix holds true for all other entries as well
    	for(int i = 0; i < Math.min(first.length(), last.length()); i++) {
    		
    		// increase i until chars are not equal anymore
    		if(!(first.charAt(i) == last.charAt(i))) {
    			return first.substring(0, i);
    		}
    	}
    	
    	// in this case, the complete string is the longest prefix
    	return first;
    }
}