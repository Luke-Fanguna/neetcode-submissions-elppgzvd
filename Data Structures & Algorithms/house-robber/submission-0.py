class Solution:
    def rob(self, nums: List[int]) -> int:
        # [0, 2, 9, 8, 3, 6]
        # res = [0, 2] curr = 9
        # steal = 9
        # no_steal = 2

        # [0, 2, 9, 8, 3, 6]
        # res = [0, 2, 9] curr = 8
        # steal = 10
        # no_steal = 9

        # [0, 2, 9, 8, 3, 6]
        # res = [0, 2, 9, 10] curr = 3
        # steal = 12
        # no_steal = 10

        # [0, 2, 9, 8, 3, 6]
        # res = [0, 2, 9, 10, 12] curr = 6
        # steal = 16
        # no_steal = 12
        res = [0, nums[0]]

        for i in range(1, len(nums)):
            steal = res[i-1] + nums[i]
            no_steal = res[i]
            if no_steal > steal:
                # print("dont STEAL")
                res.append(no_steal)
            else:
                # print("STEAL")
                res.append(steal)
            # print(steal, no_steal, res, nums[i])
        return res[-1]


