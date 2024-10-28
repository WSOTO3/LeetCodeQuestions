class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index 

        for i, n in enumerate(nums): #enumerate turns nums into a list of tuples for the iteration/index(i) and the element (n)
            diff = target - n # the difference is the target number minus the current element
            if diff in prevMap: #if the difference is in the prevMap:
                return [prevMap[diff], i] #return the value at the index [diff] of prevMap and the value of i(its iteration/index)
            prevMap[n] = i # if not, prevMap value at index of current value equals i 
