class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        res = []
        q = collections.deque()
        while r < len(nums):
            # Must clear values smaller than r
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()
            
            if (r+1) >= k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res 