class Solution {
public:
    vector<int> lastChar;
    string encode(vector<string>& strs) {
        // go through vector, append sub strs to total str, store index of last char of each str
        string s;
        for(auto& word : strs){
            lastChar.push_back(word.size());
            s += word;
            cout << word << endl;
            
        }
        cout << s << endl;
        return s;
    }

    vector<string> decode(string s) {
        
        vector<string> str_vec;
        int first_index = 0;
        for (auto& num : lastChar){
            str_vec.push_back(s.substr(first_index,num));
            first_index += num;
        }

        for (auto& i : str_vec){
            cout << i << endl;
        }

        return str_vec;
    }
};
