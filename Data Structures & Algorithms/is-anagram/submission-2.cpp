class Solution {
public:
    bool isAnagram(string s, string t) {
        std::map<char, int> hashMapS;
        std::map<char, int> hashMapT;

        // instantly return false if s and t are not the same size
        if (s.size() != t.size()){
            return false;
        }
        // populate both ordered maps for s and t strings
        for(int i = 0; i < s.size(); ++i){
            if(hashMapS.contains(s[i])){
                hashMapS[s[i]] +=1;
            }
            else{
                hashMapS.insert({s[i], 1});
            }
            if(hashMapT.contains(t[i])){
                hashMapT[t[i]] +=1;
            }
            else{
                hashMapT.insert({t[i], 1});
            }
        }

        auto its = hashMapS.begin();
        auto itt = hashMapT.begin();
        // std::cout << "sMap its = " << its << std::endl;
        // std::cout << "tMap itt = " << itt << std::endl;

        bool bool_anagram = true;
        //
        while(its != hashMapS.end() && itt != hashMapT.end()){
            if(its->first == itt->first){
                if(its->second == itt->second){
                    ++its;
                    ++itt;
                    continue;
                }
            }
            bool_anagram = false;
            break;
        }
        return bool_anagram;
        
    }
};
