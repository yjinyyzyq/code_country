# coding:utf-8
from functools import cmp_to_key


class Solution(object):
    def largestNumber(self, nums):
        key = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
        a = map(str, nums)
        print(sorted(a, key=key))
        res = "".join(sorted(map(str, nums), key=key)).lstrip('0')
        return res or '0'


Input = [3, 30, 34, 5, 9, 36]   # [9, 5, 36, 34, 3, 30]
Output = "953634330"
assert Solution().largestNumber(Input) == Output

Input = [1]
Output = "1"
assert Solution().largestNumber(Input) == Output

Input = [121, 12]
Output = "12121"
assert Solution().largestNumber(Input) == Output
# 给你一个列表，你对里面的数进行组合，组合成一个最大的数的字符串。
