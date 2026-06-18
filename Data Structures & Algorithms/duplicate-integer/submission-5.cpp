class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> map;
        for (auto it = nums.begin(); it != nums.end(); ++it){
            if (map.count(*it)){
                return true;
            }
            map.insert(*it);
            
        }
        return false;
    }
};