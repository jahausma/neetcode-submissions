class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groupMap;

        for(const auto& s : strs){

            // we want to track the frequency of each char in each string
            // anagrams will have the same frequency array
            vector<int> count(26,0);
            for(const auto& ch : s){
                count[ch - 'a']++;
            }
            string key = to_string(count[0]);
            for(int i = 1; i < 26; ++i){
                key +=','+ to_string(count[i]);
            }
            groupMap[key].push_back(s);
        }

        vector<vector<string>> ans;
        // auto it = groupMap.begin();

        // while(it != groupMap.end()){
        //     ans.push_back(it->second);
        //     ++it;
        // }
        for(const auto& pair : groupMap){
            ans.push_back(pair.second);
        }

        return ans;
    }
};
