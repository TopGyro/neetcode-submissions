class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pM = {}
        for i,n in enumerate(nums):
            if target - n in pM:
                return [pM[target - n],i]
            else:
                pM[n] = i
        