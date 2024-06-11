class Solution {
    public int romanToInt(String s) {
    	
    	int num = 0;
    	
    	// take care of subtraction
    	boolean skip_next = false;
    	
    	for (int i = 0; i < s.length(); i++){
    		
    	    char c = s.charAt(i);
    	    char next_char = 'a';
    	    
    	    if(i < (s.length() - 1)) {
    	    	next_char = s.charAt(i + 1);
    	    }
    	    
    	    if(!skip_next) {
    	    	switch(c) {
    	    	case 'I':
    	    		if(next_char == 'V') {
                        skip_next = true;
                        num += 4;
    	    		}
                        
    	    		else if(next_char == 'X') {
                        skip_next = true;
                        num += 9;
    	    		}
                    
                    else {
                        num += 1;
                    }
    	    		continue;
    	    		
    	    	case 'V':
    	    		num += 5;
    	    		continue;
    	    		
    	    	case 'X':
    	    		if(next_char == 'L') {
                        skip_next = true;
                        num += 40;
    	    		}
                        
    	    		else if(next_char == 'C') {
                        skip_next = true;
                        num += 90;
    	    		}
                    
                    else {
                        num += 10;
                    }
    	    		continue;
    	    		
    	    	case 'L':
    	    		num += 50;
    	    		continue;
    	    		
    	    	case 'C':
    	    		if(next_char == 'D') {
                        skip_next = true;
                        num += 400;
    	    		}
                        
    	    		else if(next_char == 'M') {
                        skip_next = true;
                        num += 900;
    	    		}
                    
                    else {
                        num += 100;
                    }
    	    		continue;
    	    		
    	    	case 'D':
    	    		num += 500;
    	    		continue;
    	    		
    	    	case 'M':
    	    		num += 1000;
    	    		continue;
    	    	}
    	    	
    	    }
    	    
    	    else {
    	    	skip_next = false;
    	    }
    	}
    	
    	return num;
        
    }
}