class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> hashMap;

        for(int i = 0; i < nums.size(); ++i){
            if(hashMap.contains(nums[i])){
                return true;
            }
            hashMap.insert({nums[i],i});
        }
    return false;
    }
};