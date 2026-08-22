class Solution {
public:
    
    vector<int> productExceptSelf(vector<int>& nums) {
        // cant use divison because of divide by zero concern
        
        int nums_size = nums.size();
        vector<int> ans(nums_size,1);

        // do all prefix mulitplication
        int prefix = 1;
        for(int i = 0; i < nums_size; i++){
            ans[i] *= prefix;
            prefix *= nums[i];
            cout << prefix << endl;
        }

        // do all postfix multiplication
        int postfix = 1;
        for(int i = nums_size -1; i >= 0; --i){
            ans[i] *= postfix;
            postfix *= nums[i];
        }
        return ans;
    }
};
