class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int       
    
        """
        
        n = len(height)
        
        # left pointer to the beginning of the array
        left = 0
        
        # right pointer to the end of the array 
        right = n - 1
        
        # keep track of maximum area while running through the array
        max_area = 0
        
        while left < right:

            # compute the area between the current pointers
            curr_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, curr_area)
            
            # move the pointer towards the center that has the smaller height
            # (which maximizes the area)
            if height[left] < height[right]:
                
                left += 1
                
            else:
                
                right -= 1
                
        return max_area