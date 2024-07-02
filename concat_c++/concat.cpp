class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        const int n = nums.size();
        nums.resize(2*n);

        for (int i = 0; i<n; ++i){
            nums[n+i] = nums[i];
        }
        return nums;
        
    }
};