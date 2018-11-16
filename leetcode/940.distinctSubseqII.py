class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        from collections import defaultdict
        mod = 10 ** 9 + 7
        seen = defaultdict(lambda: -1)
        subseq = [0 for _ in S] + [0]
        subseq[0] = 1
        for i, c in enumerate(S):
            last = seen[c]
            if last == -1:
                subseq[i + 1] = subseq[i] * 2 % mod
            else:
                subseq[i + 1] = (subseq[i] * 2 - subseq[last - 1] + mod) % mod
            seen[c] = i + 1

        return (subseq[-1] + mod - 1) % mod


S = "aba"
print(Solution().distinctSubseqII(S))