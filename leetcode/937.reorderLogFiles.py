class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        a, b = [], []
        [b.append(i) if i.split(" ")[1].isdigit() else a.append(i) for i in logs]
        a = sorted(a, key=lambda x: x.split(" ")[1:])
        return a + b


a = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
print(Solution().reorderLogFiles(a))
b = ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
