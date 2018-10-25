# coding:utf-8
class Solution(object):
    def maxProduct(self, nums):
        maximum = big = small = nums[0]
        for n in nums[1:]:
            big, small = max(n, n * big, n * small), min(n, n * big, n * small)
            maximum = max(maximum, big)
        return maximum

assert Solution().maxProduct([2, 3, -2, 4]) == 6
assert Solution().maxProduct([-2, 0, -1]) == 0
assert Solution().maxProduct([-3, -4]) == 12
assert Solution().maxProduct([0, 2]) == 2
assert Solution().maxProduct([3, -1, 4]) == 4
assert Solution().maxProduct([2, -5, -2, -4, 3]) == 24

# 这个和maxSubArray的区别在于，它是求列表里面连续部分的数值等于乘积最大。


class Solution(object):
    def maxProduct(self, nums):
        res = -float("inf")
        pre_max = 1
        pre_min = 1
        for a in nums:
            if a > 0:
                cur_max = pre_max * a
                cur_min = pre_min * a
                if cur_max > res:
                    res = cur_max
            elif a == 0:
                if 0 > res:
                    res = 0
                cur_max = 1
                cur_min = 1
            else:
                if pre_min < 0:
                    cur_max = pre_min * a
                    cur_min = min(a, pre_max * a)
                    if cur_max > res:
                        res = cur_max
                else:
                    cur_max = 1
                    cur_min = pre_max * a
                    if cur_min > res:
                        res = cur_min
            pre_max, pre_min = cur_max, cur_min
        return res