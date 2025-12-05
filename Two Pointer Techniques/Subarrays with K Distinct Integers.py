#User function Template for python3

class Solution:
    def exactlyK(self, arr, k):
        # Code here
        from collections import defaultdict
        def atMost(k):
            if k < 0:
                return 0
            cnt = defaultdict(int)
            left = 0
            res = 0
            distinct = 0
            
            for right,val in enumerate(arr):
                if cnt[val] == 0:
                    distinct += 1
                cnt[val] += 1
                
                while distinct > k:
                    cnt[arr[left]] -= 1
                    if cnt[arr[left]] == 0:
                        distinct -= 1
                    left += 1
                res += right - left + 1
            return res
        return atMost(k) - atMost(k-1)