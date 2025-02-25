class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1 #Initialize the left and right pointers
        res = 0 # result initialized at 0 

        while l < r: # while left pointer is to the left of the right pointer:
            area = min(heights[l], heights[r]) * (r - l) # area variable is equal to the smallest number between the two pointers times 
                                                         # the difference between the number at both pointers
            res = max(res, area) # the result is set to the bigger number between the current result and current area
            if heights[l] <= heights[r]: # if number at left pointer is less than or equal to the number at the right pointer: 
                l += 1 # move the left pointer to the right 
            else: # if left pointer is greater: 
                r -= 1 # move the right pointer to the left 
        return res # return the result 
