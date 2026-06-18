class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {} #Hashmap of the previous set of elements and indexes
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in prev:
                return [prev[diff], i]
            else:
                prev[nums[i]] = i