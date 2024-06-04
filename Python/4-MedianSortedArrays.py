class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        
        """
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        # making sure that nums1 is the smaller array
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        n_total = n1 + n2
        n_half = (n_total + 1) // 2
        
        # pointers for binary search
        left = 0
        right = n1
        
        # binary search on smaller array nums1
        while left <= right:
            
            # create first partition
            m1 = (left + right) // 2 # nums1
            m2 = n_half - m1         # nums2
            
            # check the boundaries of the partitions
            left1 = nums1[m1 - 1] if (m1 - 1) >= 0 else float("-infinity")
            right1 = nums1[m1] if m1 < n1 else float("infinity")
            left2 = nums2[m2 - 1] if (m2 - 1) >= 0 else float("-infinity")
            right2 = nums2[m2] if m2 < n2 else float("infinity")
            
            # partition correct
            if left1 <= right2 and left2 <= right1:
                
                # compute median depending on total number of elements
                if n_total % 2: # odd
                    
                    return(max(left1, left2))
                
                else: # even
                
                    return((max(left1, left2) + min(right1, right2)) / 2.0)
                
            elif left1 > right2: # too many elements from nums1 in partition
                
                right = m1 - 1
                
            else: # too many elements from nums2 in partition
                
                left = m1 + 1