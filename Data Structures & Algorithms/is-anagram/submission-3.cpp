class Solution {
public:
    bool isAnagram(string s, string t) {
        std::map<char, int> hashMap1;
        std::map<char, int> hashMap2;

        if(s.size() != t.size()){
            return false;
        }

        for(int i = 0; i < s.size(); ++i){
            if(hashMap1.contains(s[i])){
                hashMap1[s[i]] += 1;
            }else{
                hashMap1.insert({s[i],1});
            }
            if(hashMap2.contains(t[i])){
                hashMap2[t[i]] +=1;
            }else{
                hashMap2.insert({t[i],1});
            }
        }

        auto it1 = hashMap1.begin();
        auto it2 = hashMap2.begin();
        bool bool_anagram = true;
        while(it1 != hashMap1.end() || it2 != hashMap2.end()){
            if(it1->first == it2->first){
                if(it1->second == it2->second){
                    ++it1;
                    ++it2;
                    continue;
                }
            }
            bool_anagram = false;
            return bool_anagram;
        }

        return bool_anagram;
        
    }
};
