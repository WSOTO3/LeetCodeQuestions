class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # initializes the result variable as a list of 1s the size of the nums list

        prefix = 1 # initialize prefix variable as 1
        #function getting the prefix values of each position
        for i in range(len(nums)): # looping as much times as the length of the nums list
            res[i] = prefix #value at position i of res list is set equal to prefix variable value
            prefix *= nums[i] #prefix variable becomes equal to prefix times nums[i]
            
        postfix = 1 # postfix is initialized at 1 
        #function getting the postfix values of each position and multiplying with prefix to get final result
        for i in range(len(nums) - 1, -1, -1): #looping backwards starting from the last number 
            res[i] *= postfix # value in the position i of res list will becomes equal to itself times postfix
            postfix *= nums[i] # postfix becomes itself times the value in position i of nums list
        return res # return the result

#Time Complexity: O(n)
#Space Complexity: O(1)
