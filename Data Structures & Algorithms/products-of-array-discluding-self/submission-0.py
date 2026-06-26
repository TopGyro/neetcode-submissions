class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * (len(nums))
        l = 1
        for i in range(len(nums)):
            out[i] = l
            l *= nums[i]
        r = 1
        for i in range(len(nums) -1 , -1, -1):
            out[i] *= r
            r *= nums[i]
        return out


        
            
        