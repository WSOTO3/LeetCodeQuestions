class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # create a set for the list of numbers
        longest = 0 # longest variable is set to zero 

        for num in numSet: #go through each number in the set 
            if (num - 1) not in numSet: # if the number before it on the number line isnt in the set
                length = 1 # length is 1
                while (num + length) in numSet: #while number after the current number is in the set, add to the length 
                    length += 1
                longest = max(length, longest) # longest will be compared each time and the bigger number between the lcurrent ongest and 
                                               # length variable will become the new longest 
        return longest #return longest 
