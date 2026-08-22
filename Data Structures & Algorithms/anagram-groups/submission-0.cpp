class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string,vector<string>> groupMap;
        vector<vector<string>> ans;

        for(int i = 0; i < strs.size(); ++i){
            string temp = strs[i];
            sort(temp.begin(), temp.end());
            groupMap[temp].push_back(strs[i]);
            cout << "String Index = " << temp << endl;
            cout << "String Vector Insert = " << strs[i] << endl;
        }

        auto it = groupMap.begin();

        while(it != groupMap.end()){
            ans.push_back(it->second);
            ++it;
        }
        return ans;
    }
};
