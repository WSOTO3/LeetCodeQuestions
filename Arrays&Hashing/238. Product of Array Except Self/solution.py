class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # initializes the result variable as multiple lists of 1s the size of the nums list

        prefix = 1 # initialize prefix variable as 1
        for i in range(len(nums)): # looping as much times as the length of the nums list
            res[i] = prefix #result 
            prefix *= nums[i] #prefix variable becomes equal to prefix times the whats in nums[i]
        postfix = 1 # postfix is initialized at 1 
        for i in range(len(nums) - 1, -1, -1): #looping backwards starting from the last number 
            res[i] *= postfix # value in the position i of res list will becomes eaul to itself times postfix
            postfix *= nums[i] # postfix becomes itself times the value in position i of nums list
        return res # return the result
