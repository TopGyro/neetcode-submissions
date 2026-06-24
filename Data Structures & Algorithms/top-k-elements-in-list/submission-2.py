import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        HT = {}
        for i in nums:
            if i in HT: 
                HT[i] += 1
            else:
                HT[i] = 1
        #print(HT)
        pq = []
        for key,value in HT.items():
            heapq.heappush(pq,(-value,key))
        ans = []
        for e in range(k):
            _,key = heapq.heappop(pq)
            ans.append(key)
        return(ans)
        
        
        


            
            
        
        