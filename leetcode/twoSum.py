# coding:utf-8
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = 0
        b = len(numbers)
        while a < b:
            if numbers[a] + numbers[b] == target:
                return [a, b]
            elif numbers[a] + numbers[b] < target:
                a += 1
            else:
                b -= 1

# 这个题是在一个有序的列表里面找两个值，两个值的和等于目标值。