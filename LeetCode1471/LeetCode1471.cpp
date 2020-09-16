class Solution {
public:
    vector<int> getStrongest(vector<int>& arr, int k) {
        sort(arr.begin(), arr.end());
        int m = arr[(arr.size() - 1) / 2];
        int left = 0;
        int right = arr.size() - 1;
        vector<int> ans;
        while (k--)
        {
            if (abs(arr[left] - m) > abs(arr[right] - m))
                ans.push_back(arr[left++]);
            else if (abs(arr[left] - m) < abs(arr[right] - m))
                ans.push_back(arr[right--]);
            else
            {
                if (arr[left] > arr[right])
                    ans.push_back(arr[left++]);
                else
                    ans.push_back(arr[right--]);
            }
        }
        return ans;
    }
};