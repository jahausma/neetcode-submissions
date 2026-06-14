class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groupMap;

        for(const auto& str : strs){
            string temp = str;
            sort(temp.begin(), temp.end());
            groupMap[temp].push_back(str);
        }

        vector<vector<string>> ans;

        for(const auto& pair : groupMap){
            ans.push_back(pair.second);
        }

        return ans;
    }
};
