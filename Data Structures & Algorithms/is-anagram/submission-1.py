class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1= {}
        hashmap2 = {}
        for l1 in s:
            if l1 in hashmap1:
                hashmap1[l1] += 1
            else:
                hashmap1[l1] = 1
        
        for l2 in t:
            if l2 in hashmap2:
                hashmap2[l2] += 1
            else:
                hashmap2[l2] = 1
        
        if hashmap1 == hashmap2:
            return True
        else:
            return False