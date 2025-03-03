class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures) #n is the amount of temperatures there are
        res = [0] * n # result will start as an array of 0s for each temperature

        for i in range(n - 2, -1, -1): # start at (n-2) stop at -1 and go down by 1
            j = i + 1 # j is equal to i + 1
            while j < n and temperatures[j] <= temperatures[i]: # while j is less than the total temps and temp at j is less or equal to 
                                                                # temp at i 
                if res[j] == 0: # if the temp at res[j] is equal to 0  
                    j = n # j equals n 
                    break # break
                j += res[j] # j equals j plus res[j]
            
            if j < n: # if j is less than total num of temps 
                res[i] = j - i # result at i equals j - i
        return res # return result array
