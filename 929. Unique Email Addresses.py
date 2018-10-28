import re
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        a = set()
        re_comp_add = re.compile(u"\+.*@")
        re_comp = re.compile(u".*@")
        for i in emails:
            if "+" in i:
                ret = re.findall(re_comp_add, i)[0]
                i = i.replace(ret[:-1], "")
            ret = re.findall(re_comp, i)[0]
            ret1 = ret.replace(".", "")
            i = i.replace(ret, ret1)
            a.add(i)
        return a
Input = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(Solution().numUniqueEmails(Input))

