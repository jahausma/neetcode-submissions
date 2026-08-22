class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> sumDiffMap;
        vector<int> ans;
        
        
        for(int i = 0; i < nums.size(); ++i){
            sumDiffMap[nums[i]] = i;
        }

        for(int i = 0; i < nums.size();++i){
           int diff = target - nums[i];

            if(sumDiffMap.contains(diff) && sumDiffMap.find(diff)->second != i){
                cout << "First = " << sumDiffMap.find(diff)->second << endl;
                if(sumDiffMap.find(diff)->second < i){
                    ans.push_back(sumDiffMap.find(diff)->second);
                    ans.push_back(i);
                    return ans;
                }else{
                    ans.push_back(i);
                    ans.push_back(sumDiffMap.find(diff)->second);
                    return ans;
                }
            }
        }
        return ans;
    }
};
