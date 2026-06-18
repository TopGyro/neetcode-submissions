class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> keyS;
        unordered_map<char,int> keyT;
        if (s.length() != t.length()){
            return false;
        }
        for (auto itS = s.begin(), itT = t.begin() ; itS != s.end(); itS++,itT++){
            keyS[*itS]++;
            keyT[*itT]++;
        }
        return keyS == keyT;
    }
};
