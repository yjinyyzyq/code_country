class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        ysforx = defaultdict(set)
        for x, y in points:
            ysforx[x].add(y)
        print(ysforx)
        ans = 10 ** 100
        keys = sorted(ysforx)
        n = len(keys)
        for i in range(n):
            for j in range(i + 1, n):
                ps = ysforx[keys[i]] & ysforx[keys[j]]
                ps = sorted(ps)
                mindiff = 10 ** 100
                for x, y in zip(ps, ps[1:]):
                    mindiff = min(mindiff, y - x)
                if mindiff < 10 ** 100:
                    ans = min(ans, (keys[j] - keys[i]) * mindiff)

        return ans if ans < 10 ** 100 else 0


a = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
b = [[1, 1], [1, 3], [1, 5]]
print(Solution().minAreaRect(b))
