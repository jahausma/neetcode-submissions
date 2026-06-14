class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        map<vector<int>,vector<string>> groupMap;

        for(const auto& s : strs){

            vector<int> cnt(26,0);

            for(const auto& ch : s){
                cnt[ch - 'a']++;
            }

            groupMap[cnt].push_back(s);
        }
        
        vector<vector<string>> result;
        for(const auto& pair : groupMap){
            result.push_back(pair.second);
        }
        return result;
    }
};
