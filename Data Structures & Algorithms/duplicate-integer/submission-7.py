class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        t = {}
        for num in nums:
            if num in t:
                return True
            else:
                t[num] = 1
        return False
