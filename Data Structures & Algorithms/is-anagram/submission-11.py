class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hs1 = {}
        hs2 = {}

        for let in s:
            if let not in hs1:
                hs1[let] = 1
            else:
                hs1[let] += 1

        for let2 in t:
            if let2 not in hs2:
                hs2[let2] = 1
            else:
                hs2[let2] += 1

        if hs1 == hs2:
            return True
        else:
            return False
        