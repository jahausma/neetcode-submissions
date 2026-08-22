class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> int_freq;

        // iterate through nums and order the most frequent

        for(int i = 0; i < nums.size(); ++i){
            int_freq[nums[i]]+=1;
        }

        // we will use the priority queue to store the pairs with min-heap
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

        for(auto& entry : int_freq){
            pq.push({entry.second,entry.first});

            // keep the queue only 4 long
            if(pq.size() > k){
                pq.pop();
            }
        }
        
        vector<int> ans;
        for(int i = 0; i < k; ++i){
            ans.push_back(pq.top().second);
            pq.pop();
        }
        return ans;
    }
};
