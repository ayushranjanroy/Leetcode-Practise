class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> ans(nums.size(),0);
        int cur = 0; int nex = 1;int i=0;
        for(auto it:nums){
            if(it<0){
                ans[nex]=it;
                nex+=2;
            }
            else if(it>0){
                ans[cur]=it;
                cur+=2;
            }
        }
        return ans;
    }
};