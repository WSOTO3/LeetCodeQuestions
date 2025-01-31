class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # create a dictionary for the counts for each element/number 
        freq = [[] for i in range(len(nums) + 1)] # create a big list, the size of "nums", with lists as the items

        for num in nums: # for every number in "nums": 
            count[num] = count.get(num, 0) + 1 # increase the count of the specific number by one by getting the value of the number(key) 
                                               # from the dictionary and adding one; if number is not already a key, will default at 0 then
                                               # add 1
        for num, cnt in count.items(): # for every number and count(key and value) in the count dictionary 
            freq[cnt].append(num) # add the current number to the specific list that represents the specific count 
        
        res = [] # create a list for the result/solution
        
        for i in range(len(freq) - 1, 0, -1): # going through the freq list backwards( starting from the most frequent and going down)
            for num in freq[i]: 
                res.append(num)  # append the number to the result/solution
                if len(res) == k:  #if the result is as long as k
                    return res # return the current result



# Time Complexity: O(n) 
# Space Complexity: O(n) 
# Bucket Sort
