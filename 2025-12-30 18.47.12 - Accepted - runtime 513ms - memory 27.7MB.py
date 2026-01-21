class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        from collections import deque
        MOD = 10**9 + 7
        n = len(nums)
        
        # dp[i] = number of ways to partition nums[0:i]
        dp = [0] * (n + 1)
        dp[0] = 1
        
        # prefix sum of dp for range queries
        prefix = [0] * (n + 2)
        prefix[1] = 1
        
        # Use two monotonic deques to track max and min in sliding window
        max_dq = deque()  # decreasing
        min_dq = deque()  # increasing
        
        left = 0
        for right in range(n):
            # Add current element to deques
            while max_dq and nums[max_dq[-1]] <= nums[right]:
                max_dq.pop()
            max_dq.append(right)
            
            while min_dq and nums[min_dq[-1]] >= nums[right]:
                min_dq.pop()
            min_dq.append(right)
            
            # Shrink window until valid
            while max_dq and min_dq and nums[max_dq[0]] - nums[min_dq[0]] > k:
                left += 1
                while max_dq and max_dq[0] < left:
                    max_dq.popleft()
                while min_dq and min_dq[0] < left:
                    min_dq.popleft()
            
            # dp[right+1] = sum of dp[left:right+1]
            dp[right + 1] = (prefix[right + 1] - prefix[left]) % MOD
            prefix[right + 2] = (prefix[right + 1] + dp[right + 1]) % MOD
        
        return dp[n]