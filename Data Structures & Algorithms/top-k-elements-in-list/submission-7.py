class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        #build dictionary
        for num in nums:
            if num not in count:
                count[num] = 1
                continue
            count[num] += 1
        
        for key,v in count.items():
            res.append((key,v))
        
        res.sort(key=lambda res: res[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(res[i][0])
        return ans
        
        
        
        


            
            
        
        