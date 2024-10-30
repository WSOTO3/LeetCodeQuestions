class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # create a dictionary for the counts for each element/number 
        freq = [[] for i in range(len(nums) + 1)] # create a list of lists that is as long as the length of the list of nums

        for num in nums: # for every number in the list of numbers: 
            count[num] = 1 + count.get(num, 0) # increase the count of the specific number by one by getting the value of the number  
                                               # from the dictionary and adding one 
        for num, cnt in count.items(): # for every number and count(key and value) in the count dictionary 
            freq[cnt].append(num) # add the current number to the specific list that represents the specific count 
        
        res = [] # create a list for the result/solution
        for i in range(len(freq) - 1, 0, -1): # going through the freq list backwards( starting from the most frequent and going down)
            for num in freq[i]: 
                res.append(num)  # append the number to the result/solution
                if len(res) == k:  #if the result is as long as k
                    return res # return the current result
