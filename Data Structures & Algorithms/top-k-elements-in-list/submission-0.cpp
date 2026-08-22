class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> int_freq;

        // iterate through nums and order the most frequent

        for(int i = 0; i < nums.size(); ++i){
            int_freq[nums[i]]+=1;
        }

        // we will use the priority queue to store pairs with the 
        // max-heap functionality (largest at the beginning)
        priority_queue<pair<int,int>> pq;
        auto it = int_freq.begin();

        while(it != int_freq.end()){
            pq.push({it->second,it->first});
            it++;
        }
        
        vector<int> ans;
        for(int i = 0; i < k; ++i){
            pair p = pq.top();
            ans.push_back(p.second);
            pq.pop();
        }
        return ans;
    }
};
