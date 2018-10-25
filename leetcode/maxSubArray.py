# coding:utf-8
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return sum(nums)
        ret, k = nums[0], nums[0]
        for value in range(1, len(nums)):
            ret += nums[value]
            if ret >= 0:
                ret = max(ret, nums[value])
                k = max(k, ret)
            else:
                ret = nums[value]
                k = max(k, nums[value])
        return k


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# 找一个数组里面最大的一个连续求和。使得这个和最大。
