class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] #create a list for the solution
        nums.sort() # sort the nums list

        for i, a in enumerate(nums): #go through an enumerated nums list
            if a > 0: # a num is higher than 0, break out of the for loop
                break

            if i > 0 and a == nums[i - 1]: # if index is greater than 0 and the number is equal to the number at the index prior, continue
                continue

            l, r = i + 1, len(nums) - 1 #initialize the right and left pointer 
            while l < r: # while the left pointer is to the left of the right pointer 
                threeSum = a + nums[l] + nums[r] # threeSum variable is set to current number plus the numbers at both pointers
                if threeSum > 0: # if the variable is greater than 0 
                    r -= 1 #move the right pointer to the left
                elif threeSum < 0: # if the variable is less than 0 
                    l += 1 # move the left pointer to the right 
                else:
                    res.append([a, nums[l], nums[r]]) # if equal to 0, append the three numbers as a solution to the solution list
                    l += 1 #move left pointer to the right 
                    r -= 1 #move the right pointer to the left
                    while nums[l] == nums[l - 1] and l < r: # while the number at the left pointer is equal to the number to the left of that 
                        l += 1   # pointer and left is still to the left of the right pointer, move the left pointer to the right
                        
        return res # return the solution list 
