class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            seen_prev = {}
            for i,n in enumerate(nums):
                diff = target - nums[i]
                if diff in seen_prev:
                    return[seen_prev[diff],i]
                else:
                    seen_prev[n] = i 
                

                


                

