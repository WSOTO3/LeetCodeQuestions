class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

#Time Complexity: O(n)
#Space Complexity: O(n)
