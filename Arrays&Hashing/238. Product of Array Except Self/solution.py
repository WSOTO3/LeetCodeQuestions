class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # initializes the result variable as multiple lists of 1s the size of the nums list

        prefix = 1 # initialize prefix variable as 1
        for i in range(len(nums)): # looping as much times as the length of the nums list
            res[i] = prefix #result 
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
