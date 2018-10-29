# 931. Minimum Falling Path Sum
class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        return sum([min(i) for i in A])

Input = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().minFallingPathSum(Input))