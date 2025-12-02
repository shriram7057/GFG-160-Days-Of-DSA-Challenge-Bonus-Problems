class Solution {
  public:
    int maxSkill(vector<int> &arr) {
        // code here
        int n=arr.size();
        vector<int>nums(n+2,1);
        for(int i=0;i<n;i++) nums[i+1]=arr[i];
        
        vector<vector<int>>dp(n+2,vector<int>(n+2,0));
              
        for(int len=1; len <= n;len++)
        {
            for(int l = 1; l + len - 1 <= n; l++)
            {
                int r= l+len-1;
                for(int k=l;k<=r;k++)
                {
                    dp[l][r] = max(dp[l][r],
                                 dp[l][k-1] + dp[k+1][r]+
                                 nums[l-1] * nums[k] * nums[r+1]);
                }
            }
        }
        return dp[1][n];
    }
};





