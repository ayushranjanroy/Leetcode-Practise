class Solution {
public:
    int solve(TreeNode* root,int curMax){
        if (root){
            int count=solve(root->left, max(curMax,root->val)) + solve(root->right, max(curMax,root->val));
            if (root->val>=curMax){
                count++;
            }
            return count;
        }
        return 0;
    }
    int goodNodes(TreeNode* root) {
        return solve(root,INT_MIN);
    }
};