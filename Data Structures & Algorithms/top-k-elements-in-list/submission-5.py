class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for num in nums:
            count[num] = 1 + count.get(num,0)
        arr = list(count.items())
        arr.sort(key=lambda x:x[1])
        while len(res) < k:
            res.append(arr.pop()[0])
        return res
        
        
        


            
            
        
        