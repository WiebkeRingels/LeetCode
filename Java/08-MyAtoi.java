class Solution {
	public int myAtoi(String s) {

		// build integer in this variable
		long num = 0;

		// remember sign of number
		int sign = 1;

		int s_len = s.length();
		int i = -1;
		while(i < s_len) {

			i++;
			if(i < s_len) { // special case: only white spaces
				
				// read out current position
				char curr_char = s.charAt(i);

				// skip white spaces
				if(curr_char == ' ') continue;

				// convert digits to number
				if(Character.isDigit(curr_char) || curr_char == '+' || curr_char == '-') {

					// take care of signed numbers
					sign = (curr_char == '-')? -1 : 1;
					if(curr_char == '+' || curr_char == '-') i++;

					if (i < s_len) { // special case: only sign without number
						curr_char = s.charAt(i);

						while(Character.isDigit(curr_char)) {
							num = num * 10 + (curr_char - '0');
							if((sign * num) > Integer.MAX_VALUE) return Integer.MAX_VALUE;
							if((sign * num) < Integer.MIN_VALUE) return Integer.MIN_VALUE;
							i++;
							if(i >= s_len) break;
							curr_char = s.charAt(i);
						}    			
						break;
					} else break; 
				} else break; // do not consider numbers after the first number occurrence
			}
		}

		return (int)(sign * num);
	}
}