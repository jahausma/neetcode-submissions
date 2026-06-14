class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        map<string,vector<string>> groupMap;

        for(const auto& s : strs){

            vector<int> cnt(26,0);

            for(const auto& ch : s){
                cnt[ch - 'a']++;
            }

            // we use a string to store the key because it is much more efficient than using vector as key
            string key = to_string(cnt[0]);
            for(int i = 1; i < 26; ++i){
                key += ',' + to_string(cnt[i]);
            }
            groupMap[key].push_back(s);
        }
        
        vector<vector<string>> result;
        for(const auto& pair : groupMap){
            result.push_back(pair.second);
        }
        return result;
    }
};
