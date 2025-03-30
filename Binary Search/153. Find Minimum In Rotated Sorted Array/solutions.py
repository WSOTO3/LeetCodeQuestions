class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 #initializing the left and right pointers
        while l < r: #while left pointer is still to the left of the right pointer 
            m = l + (r - l) // 2 # midpoint variable is equal to value at left pointer plus (value at right minus value at left) divided by 2
            if nums[m] < nums[r]: #if value at m is less than the value at right pointer 
                r = m #right pointer is set to the m value
            else:
                l = m + 1 # if not, left pointer is set to the value of m plus 1
        return nums[l] # return the value at the left pointer 
