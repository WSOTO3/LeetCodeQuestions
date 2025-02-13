class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1 #initiaalize left and right pointers

        while l < r: # while left pointer hasnt reached right pointer 
            curSum = numbers[l] + numbers[r] #current sum is value at left pointer plus the value at right pointer

            if curSum > target: # if current sum is greater than the target sum
                r -= 1 # move the right pointer to the left by one
            elif curSum < target: # if current sum is less than target sum
                l += 1 # move left pointer to the right 
            else: 
                return [l + 1, r + 1] # return the right pointer and left pointer indices, but remember, its a 1-indexed array which means 
                                      # the first index is indexed at 1 and not 0 how it usually is
        
