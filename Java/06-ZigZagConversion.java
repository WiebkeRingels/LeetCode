import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class Solution {
    public String convert(String s, int numRows) {
        
        /*approach:
         * 
         * build the zigzag string in a list of string
         * 
         * running through the string once is enough because for each
         * letter we know in which row it belongs
         * 
         * after building this list, the rows can be concatenated
         * 
         * exmaple:
         * 
         * numRows                    - 4
         * s                          - "helloworld"
         * row index after conversion - 1234321234
         * 
         */
    	
    	// special case
    	if(numRows == 1) {
    		return s;
    	}
        
    	// declare variables
        int curr_row = 1;
        int step = 1;
        int n = s.length();
        
        // zigzag row array
        // 2nd dimension with length n too long, delete nulls later
        String[][] rows = new String[numRows][n];
        
        // for each row, track until which index it was filled
        int[] row_idcs = new int[numRows];
        Arrays.fill(row_idcs, 0);
        
        // create row array
        for(int i = 0; i < n; i++) {
        	
        	String curr_char = s.substring(i,i+1);
        	rows[curr_row-1][row_idcs[curr_row-1]] = curr_char;
        	row_idcs[curr_row-1] += 1;
        	
        	if(curr_row == 1) {
        		step = 1;
        	} else if (curr_row == numRows) {
        		step = -1;
        	}
        	
        	curr_row += step;
        }
        
        // flatten the array
        String result = Stream.of(rows)  			// 2d array -> 2d stream
                .flatMap(Stream::of) 				// flatten the stream
                .filter(x -> x != null) 			// delete nulls of 2nd dimension
                .collect( Collectors.joining(""));	// join single characters to one string
        		
    	return result;
        
    }
}