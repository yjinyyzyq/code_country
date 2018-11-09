import bisect


class RecentCounter:

    def __init__(self):
        self.nums = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.nums.append(t)
        cur_pos = len(self.nums)
        prev_pos = bisect.bisect_left(self.nums, t - 3000)
        return cur_pos - prev_pos

a = RecentCounter()
print(a.ping(1))
print(a.ping(1000))
print(a.ping(6001))
