class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> sumDiffMap;
        vector<int> ans;
        
        
        for(int i = 0; i < nums.size(); i++){
            int diff = target - nums[i];
            if(sumDiffMap.contains(diff)){
                int first = sumDiffMap.find(diff)->second;
                std::cout << " First = " << first << std::endl;
                ans.push_back(first); ans.push_back(i);
            }
            sumDiffMap.insert({nums[i], i});
            std::cout << "Diff = " << diff << std::endl;
        }
    return ans;
    }
};
