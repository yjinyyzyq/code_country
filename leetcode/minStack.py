class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min_current = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.s:
            self.min_current = x
        elif self.min_current > x:
            self.min_current = x
        self.s.append(x)

    def pop(self):
        """
        :rtype: void
        """
        last = self.s.pop()
        # if self.s is already empty or self.min_current has not been popped out, there is not need for a loop
        if self.s and last == self.min_current:
            self.min_current = self.s[0]
            for i in self.s:
                if i < self.min_current:
                    self.min_current = i

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.s:
            return self.min_current
        else:
            return None

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(12)
obj.push(3)
obj.push(10)
obj.push(1)
obj.pop()
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)
