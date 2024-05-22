# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # create ListNode of first node
        [sum,carryover] = self.listNodeSum(l1, l2, 0)
        result = ListNode(sum)
        
        # create pointer for current node
        current_node = result
           
        while (l1.next is not None) or (l2.next is not None):
            
            if l1.next is not None:
                l1 = l1.next
            else:
                l1 = ListNode(0)
                
            if l2.next is not None:
                l2 = l2.next
            else:
                l2 = ListNode(0)
            
            [sum,carryover] = self.listNodeSum(l1, l2, carryover)
            
            # link to the next node
            current_node.next = ListNode(sum)
            current_node = current_node.next
          
        # add aditional node if last sum returns a carryover
        if carryover == 1:
            current_node.next = ListNode(carryover)
            current_node = current_node.next
            
        return result
    
    
    # helper function
    def listNodeSum(self, l1, l2, carryover):
        """
        :type l1: ListNode
        :type l2: ListNode
        :type carryover: int
        :rtype: list
        """
  
        sum = carryover + l1.val + l2.val
                
        # update carryover
        carryover = 0   
        if sum >= 10:      
            carryover = 1
            sum -= 10

        return [sum,carryover]
