class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        let = sorted([x for x in logs if not x.split()[1].isdigit()], key=lambda x: x.split()[1:])
        print(let)
        dig = [x for x in logs if x.split()[1].isdigit()]
        print(dig)
        return let + dig



a = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
print(Solution().reorderLogFiles(a))
b = ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
