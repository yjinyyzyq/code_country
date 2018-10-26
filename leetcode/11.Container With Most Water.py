# coding:utf-8
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height) - 1
        a = 0
        b = l
        max_left = height[a]
        max_right = height[b]
        contain_water = min(max_left, max_right) * b
        while a < b:
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1
            if min(height[a], height[b]) * (b - a) >= contain_water:
                contain_water = min(height[a], height[b]) * (b - a)
            else:
                pass
        return contain_water



Input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(Input))


class Solution(object):
    def maxArea(self, height):
        head, tail = 0, len(height) - 1
        max_solu = 0
        while head < tail:
            l, r = height[head], height[tail]
            if l < r:
                solu = (tail - head) * l
                head += 1
                while height[head] <= l:
                    head += 1
            else:
                solu = (tail - head) * r
                tail -= 1
                while tail and height[tail] <= r:
                    tail -= 1
            if solu > max_solu:
                max_solu = solu
        return max_solu

# 下面这种方法速度较快，因为它多做了一个判断，如果l<r了，那么再小于l的肯定是不符合要求的。