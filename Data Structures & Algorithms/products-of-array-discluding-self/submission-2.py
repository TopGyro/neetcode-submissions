class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #out = [1] * len(nums) #create a list of 1's the same length as nums
        #for i in range(len(nums)): #iterate over each set in nums
        #    for j in range(len(nums)): #Iterate over each set in nums
        #        if j != i: #if j is not equal to i
        #            out[i] *= nums[j] #output is assigned to each index that is not equal to i multiplied by j
        #return out
        out = len(nums) * [1]
        pre = 1
        for i in range(len(nums)):
            out[i] = pre
            pre *= nums[i]

        suf = 1
        for i in range(len(nums) -1 , -1, -1):
            out[i] *= suf
            suf *= nums[i]

        return out
            
        