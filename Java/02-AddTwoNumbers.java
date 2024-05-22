package add_two_numbers;

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    	
    	/*
    	 * approach:
    	 * 
    	 * loop through given ListNodes l1 and l2:
    	 * read out the digit
    	 * sum the digits and take-care of carryover
    	 * create new ListNode that is added to the result ListNode
    	 */
    	
    	// head is a dummy to be able to access first ListNode of result
    	ListNode head = new ListNode(0);
    	ListNode current = head;
    	int carryover = 0;
    	
    	while(l1 != null || l2 != null || carryover != 0) {
    		
    		// read out digits
    		int d1 = (l1 != null)? l1.val : 0;
    		int d2 = (l2 != null)? l2.val : 0;
    		
    		// sum with carryover
    		int sum = d1 + d2 + carryover;
    		int d = sum % 10;
    		carryover = sum / 10;
    		
    		// connect ListNodes
    		current.next = new ListNode(d);
    		current = current.next;
    		
    		// go to next ListNodes of inputs
    		l1 = (l1 != null)? l1.next : null;
    		l2 = (l2 != null)? l2.next : null;
    	}
    	
    	// skip first dummy ListNode with value 0 and return result
        ListNode result = head.next;
    	return result;
    }
}