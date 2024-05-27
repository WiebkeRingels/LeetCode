class Solution {
    public int reverse(int x) {
    	
    	long x_rev = 0;
    	
    	// remember if negative
    	boolean neg = false;
    	if(x < 0) {
    		
    		neg = true;
    		x *= (-1);
    	}
    	
    	// extract digits with modulo 10
    	while(x != 0) {
    		
    		long digit = x % 10;
    		x_rev = x_rev * 10 + digit;
    		x /= 10;
    	}
    	
    	// take care of negative numbers
    	if(neg) {
    		
    		x_rev *= (-1);    			
    	}
    	
    	if(-Math.pow(2,31) > x_rev || (Math.pow(2, 31) - 1) < x_rev) {
    		
    		return 0;
    	}
    	

    	return (int)x_rev;
        
    }
}
