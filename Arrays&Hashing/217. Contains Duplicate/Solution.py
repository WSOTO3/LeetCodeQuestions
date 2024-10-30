class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
# set removes all duplicates in a list so if the length of the set is shorter than the length of the regular list, 
# it is TRUE that a duplicate exists, which is the Bool that the statement will return

# Time Complexity: O(n)
# Space Complexity: O(n)
# Hash Set Length
